import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'posts'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    tags = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    likes = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    content = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    author = sqlalchemy.Column(sqlalchemy.ForeignKey('users.id'))
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

