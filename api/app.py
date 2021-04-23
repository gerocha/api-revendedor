from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from api.resources.dealer import DealerResource
from api.resources.cashback import CashbackResource
from api.resources.order import OrderResource, OrderChangeResource
from api.resources.auth import AuthResource
from api.config import DATABASE_STRING

from api.auth.helpers import authenticate, identity

db = SQLAlchemy()

def create_app() -> Flask:
    from api.models.dealer import Dealer
    from api.models.order import Order

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_STRING
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    api = Api(app)
    db.init_app(app)

    app.config["JWT_SECRET_KEY"] = "super-secret"
    jwt = JWTManager(app)

    api.add_resource(DealerResource, '/dealer')
    api.add_resource(OrderResource, '/order')
    api.add_resource(OrderChangeResource, '/order/<int:id>')
    api.add_resource(CashbackResource, '/cashback')
    api.add_resource(AuthResource, '/auth')

    return app

if __name__ == '__main__':
    create_app().run(host='0.0.0.0', debug=True)
