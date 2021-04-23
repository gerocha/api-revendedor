from api.config import CASHBACK_API_URL

import requests

class CashbackService:
    @staticmethod
    def get(document: str):
        response = requests.get(CASHBACK_API_URL + document)
        return response.json()
