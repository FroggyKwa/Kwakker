from flask_restful import Resource, abort
from flask import jsonify
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
            print(jsonify(post.to_dict()))
            return jsonify(post.to_dict())
        except AttributeError:
            return jsonify({'error': 404})  # post not found


class PostListResource(Resource):
    def get(self, post_id):
        post_id = int(post_id)
        session = db_session.create_session()
        posts = session.query(Post).filter(Post.id in range(post_id - 20 if post_id - 20 >= 0 else 0, post_id)).all()
        return jsonify({'post': [item.to_dict() for item in posts]})


def abort_if_post_not_found(post_id):
    from data.db_session import create_session
    session = create_session()
    user = session.query(Post).get(post_id)
    if not user:
        abort(404, message=f"Post {post_id} not found")
