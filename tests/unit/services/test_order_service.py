from api.service.order import OrderService, UpdateOrDeletInInvalidStatusException
from api.models.order import Status

import pytest
from dataclasses import dataclass


@dataclass()
class OrderStub:
    status: str


class Model:
    def set_ret(self, ret):
        self.ret = ret

    def get(self, *args, **kwargs):
        return self.ret

class CashbackServiceMock:
    @staticmethod
    def get(*args, **kwargs):
        return {'body': {'credit': 1000}}


class TestOrderService:

    def test_create_new_order_should_create_approved_for_whitelisted_document(self, order_model):
        svc = OrderService(model=order_model, cashback_service=CashbackServiceMock)

        o = svc.create({'document': OrderService.WHITE_LIST[0], 'value': 1000.00})

        assert o['status'] == Status.APPROVED


    def test_edit_order_should_only_allow_for_validating_status(self):
        model = Model()
        obj = OrderStub(status=Status.APPROVED)

        model.set_ret(obj)

        svc = OrderService(model=model, cashback_service=CashbackServiceMock)

        with pytest.raises(UpdateOrDeletInInvalidStatusException):
            svc.update(id=1, values={}, document='')
