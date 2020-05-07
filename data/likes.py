import datetime
import sqlalchemy
from sqlalchemy.orm import relationship, create_session
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase


class Like(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'likes'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    post_id = sqlalchemy.Column(sqlalchemy.ForeignKey('post.id'))
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    post = relationship('Post', back_populates='likes')
    user = relationship('User', back_populates='likes')

