from flask_restful import Resource, reqparse
from flask import jsonify

from api.posts import abort_if_post_not_found
from api.users import abort_if_user_not_found
from data import db_session
from data.likes import Like
from data.posts import Post
from data.users import User



class LikeResource(Resource):
    def __init__(self):
        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument('post_id', required=True)
        self.post_parser.add_argument('user_id', required=True)

        self.delete_parser = reqparse.RequestParser()
        self.delete_parser.add_argument('post_id', required=True)
        self.delete_parser.add_argument('user_id', required=True)

        self.get_parser = reqparse.RequestParser()
        self.get_parser.add_argument('post_id', required=True)
        self.get_parser.add_argument('user_id', required=True)

    def post(self):
        session = db_session.create_session()
        args = self.post_parser.parse_args()
        user_id = args['user_id']
        post_id = args['post_id']
        abort_if_user_not_found(user_id)
        abort_if_post_not_found(post_id)
        post = session.query(Post).get(post_id)
        like = Like()
        like.post_id = post_id
        like.user_id = user_id
        post.likes.append(like)
        session.commit()
        return jsonify({'message': 'OK'})

    def delete(self):
        session = db_session.create_session()
        args = self.post_parser.parse_args()
        user_id = args['user_id']
        post_id = args['post_id']
        abort_if_user_not_found(user_id)
        abort_if_post_not_found(post_id)
        post = session.query(Post).get(post_id)
        like = session.query(Like).filter(Like.post_id == post_id, Like.user_id == user_id).first()
        try:
            post.likes.remove(like)
            session.commit()
            return jsonify({'message': 'OK'})
        except ValueError: # лайков больше нет
            return jsonify({'message': 'NO LIKES'})

    def get(self):
        session = db_session.create_session()
        args = self.post_parser.parse_args()
        user_id = args['user_id']
        post_id = args['post_id']
        abort_if_user_not_found(user_id)
        abort_if_post_not_found(post_id)
        post = session.query(Post).get(post_id)
        like = session.query(Like).filter(Like.post_id == post_id, Like.user_id == user_id).first()
        return like in post.likes


