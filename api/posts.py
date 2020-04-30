from flask_restful import Resource, abort
from flask import jsonify, render_template
from data import db_session
from data.posts import *


class PostResource(Resource):
    def post(self, post_id, tags, likes, content, author, created_at):
        session = db_session.create_session()
        post = Post()
        post.id = post_id
        post.tags = tags
        post.likes = likes
        post.content = content
        post.author = author
        post.created_at = created_at
        session.add(post)
        session.commit()
        return jsonify({'success': 'OK'})

    def delete(self, post_id):
        abort_if_post_not_found(post_id)
        session = db_session.create_session()
        post = session.query(Post).get(post_id)
        session.delete(post)
        session.commit()
        return jsonify({'success': 'OK'})

    def get(self, post_id):
        session = db_session.create_session()
        try:
            post = session.query(Post).get(post_id)
            return jsonify(
                post.to_dict(
                    only=('id', 'tags', 'likes', 'content', 'user.name', 'user.surname', 'user.id', 'created_at')))
        except AttributeError:
            return jsonify({'error': 404})  # post not found


class PostListResource(Resource):
    def get(self, post_id):
        post_id = int(post_id)
        session = db_session.create_session()
        posts = session.query(Post)[-20:post_id]
        for post in posts:
            print(post.user)
        return render_template('post_wall.html', posts=posts)


def abort_if_post_not_found(post_id):
    from data.db_session import create_session
    session = create_session()
    user = session.query(Post).get(post_id)
    if not user:
        abort(404, message=f"Post {post_id} not found")
