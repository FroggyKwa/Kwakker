from .users import UserResource, UsersListResource
from .posts import PostResource, PostListResource


def add_resources(api):
    api.add_resource(UserResource, '/api/v01/user/<username>')
    api.add_resource(UsersListResource, '/api/v01/users')
    api.add_resource(PostResource, '/api/v01/post/<post_id>')
    api.add_resource(PostListResource, '/api/v01/posts/<post_id>')
    return api
