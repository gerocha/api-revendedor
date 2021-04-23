from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

class BaseResource(Resource):
    pass


class LoggedResource(BaseResource):
    decorators = [jwt_required()]
