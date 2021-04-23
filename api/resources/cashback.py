from api.resources.base import BaseResource
from api.service.cashback import CashbackService


class CashbackResource(BaseResource):
    def get(self):
        return CashbackService.get('123123123123')
