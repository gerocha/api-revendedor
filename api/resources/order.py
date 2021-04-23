from api.resources.base import BaseResource, LoggedResource
from api.resources.schemas import InserOrderSchema
from api.service.order import OrderService, UpdateOrDeletInInvalidStatusException

from api.resources.schemas import UpdateOrderSchema, ListOrderSchema

from flask import request, abort
from flask_jwt_extended import get_jwt_identity
from marshmallow import ValidationError


class OrderResource(LoggedResource):
    def get(self):
        from api.models.order import Order
        document = get_jwt_identity()
        return ListOrderSchema().dump(OrderService(model=Order).get(document=document), many=True)

    def post(self):
        from api.models.order import Order
        try:
            order = InserOrderSchema().load(request.json or {})
            document = get_jwt_identity()
            order['document'] = document
            rt = OrderService(model=Order).create(order)
            return {'id': rt.id}, 201
        except ValidationError as err:
            abort(400, err.messages)

class OrderChangeResource(LoggedResource):
    def put(self, id):
        from api.models.order import Order

        new_values = UpdateOrderSchema().load(request.json or {})
        document = get_jwt_identity()

        try:
            rt = OrderService(model=Order).update(id=id, values=new_values, document=document)

            return rt, 200
        except UpdateOrDeletInInvalidStatusException:
            abort(400, 'Cant change order in current status')

    def delete(self, id):
        from api.models.order import Order

        try:
            document = get_jwt_identity()
            rt = OrderService(model=Order).delete(id=id, document=document)

            return rt, 200
        except UpdateOrDeletInInvalidStatusException:
            abort(400, 'Cant change order in current status')
