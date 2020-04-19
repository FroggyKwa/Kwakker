from flask_restful import Resource
from flask import jsonify

from data import db_session
from data.users import *


class UserResource(Resource):
    def add(self, nickname, name, surname, age, email, hashed_password):
        session = db_session.create_session()
        user = User()
        user.email = email
        user.surname = surname
        user.username = nickname
        user.name = name
        user.age = age
        user.hashed_password = hashed_password
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})

    def get(self, username):
        session = db_session.create_session()
        try:
            user = session.query(User).filter(User.username == username)
            return jsonify(user.to_dict)
        except Exception as e:
            print('User not found')
            print(e.__class__.__name__)
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