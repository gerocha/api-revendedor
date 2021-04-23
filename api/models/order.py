from api.app import db
from api.resources.enums import Status

from sqlalchemy import Column, Integer, String, Enum, Numeric, SmallInteger
import re


class Order(db.Model):
    id = Column(Integer, primary_key=True)
    code = Column(String(120), unique=True, nullable=False)
    document = Column(String(120), nullable=False)
    value = Column(Numeric(63), nullable=False)
    cashback = Column(Numeric(63))
    status = Column('status', Enum(Status), nullable=False, default=Status.VALIDATING)
    date = Column(String(120), nullable=False)
    active = Column(SmallInteger, nullable=False, default=1)

    @classmethod
    def create(cls, order):
        obj = cls(**order)
        db.session.add(obj)
        db.session.commit()

        return obj

    def edit(self, id: int, values: dict):
        for key, value in values.items():
            setattr(self, key, value)
        db.session.commit()
        db.session.flush()
        return {'id': self.id,
                'code': self.code,
                'document': self.document,
                'status': str(self.status),
                'date': self.date }

    def delete(self):
        self.active = 0
        db.session.commit()
        db.session.flush()

    @classmethod
    def get_by_document(cls, document: str):
        return cls.query.filter_by(document=document, active=1).all()

    @classmethod
    def get(cls, id, document):
        return Order.query.filter_by(id=id, active=1, document=document).first()
