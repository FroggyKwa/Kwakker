from .users import UserResource, UsersListResource
from .posts import PostResource, PostListResource
from .likes import LikeResource


def add_resources(api):
    api.add_resource(UserResource, '/api/v01/user')
    api.add_resource(UsersListResource, '/api/v01/users')
    api.add_resource(PostResource, '/api/v01/post')
    api.add_resource(PostListResource, '/api/v01/posts')
    api.add_resource(LikeResource, '/api/v01/like')
    return api
