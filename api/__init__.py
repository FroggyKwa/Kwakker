from .users import UserResource, UsersListResource


def add_resources(api):
    api.add_resource(UserResource, '/api/v01/user/<username>')
    api.add_resource(UsersListResource, '/api/v01/users')
    return api

