from .users import UserResource, UsersListResource
from .posts import PostResource, PostListResource


def add_resources(api):
    api.add_resource(UserResource, '/api/v01/user')
    api.add_resource(UsersListResource, '/api/v01/users')
    api.add_resource(PostResource, '/api/v01/post')
    api.add_resource(PostListResource, '/api/v01/posts')
    return api
