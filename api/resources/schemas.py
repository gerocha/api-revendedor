from marshmallow import Schema, fields, ValidationError, validate, pre_load
from api.resources.enums import Status


class BaseDocument(Schema):
    document = fields.Str(required=True)

    @pre_load
    def clear_document(self, in_data, **kwargs):
        if in_data.get('document', None):
            in_data['document'] = in_data['document'].replace('.', '').replace('-', '')
        return in_data


class InsertDealerSchema(BaseDocument):
    full_name = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)


class LoginSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)

class InserOrderSchema(Schema):
    code = fields.Str(required=True)
    date = fields.Str(required=True)
    value = fields.Decimal(required=True)


class UpdateOrderSchema(Schema):
    code = fields.Str()
    document = fields.Str()
    date = fields.Str()
    value = fields.Decimal()
    status = fields.Str(validate=validate.OneOf([status.name for status in Status]))


class ListOrderSchema(Schema):
    code = fields.Str()
    document = fields.Str()
    date = fields.Str()
    value = fields.Number()
    cashback = fields.Number()
    status = fields.Str()
