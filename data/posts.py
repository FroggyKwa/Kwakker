import datetime
import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Post(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'post'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    tags = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    likes = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    content = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    author = sqlalchemy.Column(sqlalchemy.ForeignKey('users.id'))
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

