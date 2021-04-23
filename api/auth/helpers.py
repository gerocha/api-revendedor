def authenticate(username, password):
    from api.models.dealer import Dealer
    print(username)

    return Dealer.query.filter_by(email=username).first()

def identity(payload):
    from api.models.dealer import Dealer

    return Dealer.query.get(payload['identity'])
