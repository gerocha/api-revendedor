from api.app import db

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash, check_password_hash


class Dealer(db.Model):
    id = Column(Integer, primary_key=True)
    full_name = Column(String(200), nullable=False)
    _password = Column('password', String(200), nullable=False)
    document = Column(String(14), nullable=False)
    email = Column(String(120), unique=True, nullable=False)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value: str):
        self._password = generate_password_hash(value)

    def is_valid_credential(self, password: str) -> bool:
        return check_password_hash(self.password, password)
