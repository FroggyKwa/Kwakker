from flask_restful import Resource, reqparse
from flask import jsonify
from data import db_session
from data.users import *


class UserResource(Resource):
    def __init__(self):
        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument('username', required=True)
        self.post_parser.add_argument('name', required=True)
        self.post_parser.add_argument('surname', default='')
        self.post_parser.add_argument('age')
        self.post_parser.add_argument('email')
        self.post_parser.add_argument('password', required=True)

        self.delete_parser = reqparse.RequestParser()
        self.delete_parser.add_argument('user_id', required=True)

        self.get_parser = reqparse.RequestParser()
        self.get_parser.add_argument('user_id', required=True)

    def post(self):
        session = db_session.create_session()
        args = self.post_parser.parse_args()
        user = User()
        user.email = args['email']
        user.surname = args['surname']
        user.username = args['username']
        user.name = args['name']
        user.age = args['age']
        user.set_password(args['password'])
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})

    def delete(self):
        user_id = self.delete_parser.parse_args()['user_id']
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})

    def get(self):
        username = self.get_parser.parse_args()['username']
        session = db_session.create_session()
        user = session.query(User).filter(User.username == username).first()
        try:
            return jsonify(user.to_dict(only=('id', 'username', 'name', 'surname', 'created_at')))
        except Exception as e:
            return jsonify({'error': 404})  # user not found


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(only=('id', 'username', 'name', 'surname')) for item in users]})


def abort_if_user_not_found(user_id):
    from data.db_session import create_session
    session = create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")
    session.close()
