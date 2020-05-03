import datetime
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Tag(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'tags'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    tag = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    post_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('post.id'))
    post = relationship('Post', back_populates='tags')
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)


def extract_hash_tags(s):
    return set(part[1:] for part in s.split() if part.startswith('#'))
