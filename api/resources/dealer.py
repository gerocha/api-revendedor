from api.resources.base import BaseResource
from api.service.dealer import DealerService
from api.resources.schemas import InsertDealerSchema

from flask import request, abort
from marshmallow import ValidationError

class DealerResource(BaseResource):
    def post(self):
        from api.app import db

        try:
            result = InsertDealerSchema().load(request.json or {})
            dealer = DealerService(db=db).create(dealer=result)
            return {'id': dealer.id}, 201
        except ValidationError as err:
            abort(400, err.messages)
