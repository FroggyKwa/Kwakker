import datetime
import sqlalchemy
from sqlalchemy.orm import relationship, backref
from sqlalchemy_serializer import SerializerMixin

from data.tags import Tags
from .db_session import SqlAlchemyBase


class Post(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'post'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    content = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    user = relationship('User', back_populates="posts")
    likes = relationship('Like', back_populates='post')
    tags = relationship('Tag', secondary='tags', lazy=True, backref=backref('posts', lazy=True))
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

