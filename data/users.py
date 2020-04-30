import datetime

from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
import sqlalchemy
from flask_restful import abort
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin
from .db_session import SqlAlchemyBase, create_session


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    username = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
    status = sqlalchemy.Column(sqlalchemy.Text, default='')
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime,
                                   default=datetime.datetime.now)
    likes = relationship('Like', back_populates="user")
    posts = relationship('Post', back_populates="user")

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)


def get_user_by_username(username) -> User:
    session = create_session()
    user = session.query(User).filter(User.username == username).first()
    return user
