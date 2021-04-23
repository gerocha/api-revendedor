from api.resources.base import BaseResource
from api.resources.schemas import LoginSchema

from flask_jwt_extended import create_access_token
from flask import request, abort
from marshmallow import ValidationError


class AuthResource(BaseResource):
    def post(self):
        from api.models.dealer import Dealer


        try:
            result = LoginSchema().load(request.json or {})
            dealer = Dealer.query.filter_by(email=result['email']).first()
            if not dealer.is_valid_credential(password=result["password"]):
                abort(400, 'Bad Credentials')
            if not dealer:
                abort(400, 'Bad Credentials')
            access_token = create_access_token(identity=dealer.document)

            return {'access_token': access_token}
        except ValidationError as err:
            abort(400, err.messages)
