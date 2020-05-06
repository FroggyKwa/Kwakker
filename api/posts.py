from flask_restful import Resource, abort, reqparse
from flask import jsonify, render_template
from data import db_session
from data.posts import *
from data.tags import Tag, extract_hash_tags


class PostResource(Resource):
    def __init__(self):
        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument('content', required=True)
        self.post_parser.add_argument('user_id', required=True)

        self.delete_parser = reqparse.RequestParser()
        self.delete_parser.add_argument('post_id', required=True)

        self.get_parser = reqparse.RequestParser()
        self.get_parser.add_argument('post_id', required=True)

    def post(self):
        from api.users import abort_if_user_not_found
        session = db_session.create_session()
        args = self.post_parser.parse_args()
        user_id = args['user_id']
        content = args['content']
        post = Post()
        abort_if_user_not_found(user_id)
        post.content = content
        from data.users import User
        post.user = session.query(User).get(user_id)
        hash_tags = extract_hash_tags(post.content)
        for hash_tag in hash_tags:
            tag = Tag()
            tag.content = hash_tag
            tag.post = post
            post.tags.append(tag)
            session.add(tag)
        session.add(post)
        session.commit()
        return jsonify({'success': 'OK'})

    def delete(self):
        post_id = self.delete_parser.parse_args()['post_id']
        abort_if_post_not_found(post_id)
        session = db_session.create_session()
        post = session.query(Post).get(post_id)
        session.delete(post)
        session.commit()
        return jsonify({'success': 'OK'})

    def get(self):
        post_id = self.get_parser.parse_args()['post_id']
        abort_if_post_not_found(post_id)
        session = db_session.create_session()
        post = session.query(Post).get(post_id)
        return jsonify(
            post.to_dict(only=('id', 'tags.content', 'likes', 'content', 'user.name',
                               'user.surname', 'user.id', 'created_at')))


class PostListResource(Resource):
    def __init__(self):
        self.get_parser = reqparse.RequestParser()
        self.get_parser.add_argument('post_id')
        self.get_parser.add_argument('tag')

    def get(self):
        args = self.get_parser.parse_args()
        print(args)
        post_id = int(args['post_id'])
        tag = args['tag']
        session = db_session.create_session()
        cnt = len(session.query(Post).all()) if post_id == -1 else post_id
        left_border = cnt - 20
        right_border = cnt
        if not tag:
            posts = session.query(Post).filter(left_border <= Post.id, Post.id <= right_border)[::-1]
            for i in posts:
                print(i.id)
        else:
            try:
                posts = session.query(Tag).filter(Tag.content.like('%' + tag + '%')).first().posts
            except AttributeError:  # posts not found
                posts = []
        return render_template('post_wall.html', posts=posts)


def abort_if_post_not_found(post_id):
    from data.db_session import create_session
    session = create_session()
    post = session.query(Post).get(post_id)
    if not post:
        abort(404, message=f"Post {post_id} not found")
