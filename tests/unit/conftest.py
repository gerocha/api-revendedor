import pytest


@pytest.fixture()
def order_model():
    class DummyObj:
        def __init__(self, id, status, code, value):
            self.id = id
            self.code = code
            self.value = value
            self.status = status

    class DummyModel:
        def create(self, order):
            return order
    return DummyModel()
