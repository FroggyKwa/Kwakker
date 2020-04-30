import datetime
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Post(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'post'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    tags = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    likes = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    content = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    user = relationship('User', back_populates="posts")
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

