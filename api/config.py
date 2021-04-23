import os


DEFAULT_CASHBACK_API_URL = 'https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback?cpf='
CASHBACK_API_URL = os.environ.get('CASHBACK_API_URL', DEFAULT_CASHBACK_API_URL)
CASHBACK_API_URL_TOKEN = 'ZXPURQOARHiMc6Y0flhRC1LVlZQVFRnm'
DATABASE_STRING = os.environ.get('DATABASE_STRING', 'sqlite://')
