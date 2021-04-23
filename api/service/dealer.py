
class DealerService:
    def __init__(self, db):
        self.db = db

    def create(self, dealer: dict):
        from api.models.dealer import Dealer

        obj = Dealer(**dealer)
        self.db.session.add(obj)
        self.db.session.commit()

        return obj
