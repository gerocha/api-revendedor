from api.service.cashback import CashbackService


class UpdateOrDeletInInvalidStatusException(Exception):
    msg = 'Cant change order in current status'


def can_change(function):
    def wrapper(self, **kwargs):
        from api.resources.enums import Status

        obj = self.model.get(id=kwargs['id'], document=kwargs['document'])

        if obj.status != Status.VALIDATING:
            raise UpdateOrDeletInInvalidStatusException
        return function(self=self, obj=obj, **kwargs)
    return wrapper


class OrderService:
    WHITE_LIST = ['15350946056']

    def __init__(self, model, cashback_service = CashbackService):
        self.model = model
        self.cashback_service = cashback_service

    def get(self, document: str):
        return self.model.get_by_document(document=document)


    def create(self, order):
        from api.models.order import Status

        response = self.cashback_service.get(order['document'])
        credit = response['body']['credit']
        credit_percentual = 0.2

        if order["document"] in self.WHITE_LIST:
            order["status"] = Status.APPROVED

        if order['value'] <= 1000:
            credit_percentual = 0.1

        if order['value'] > 1000 and order['value'] <= 1500:
            credit_percentual = 0.15

        order['cashback'] = credit * credit_percentual

        return self.model.create(order)


    @can_change
    def update(self, id: int, values: dict, document: str, obj):
        return obj.edit(id, values)

    @can_change
    def delete(self, id: int, document: str, obj):
        return obj.delete()
