from api import ma
from ..models import account_model
from marshmallow import fields

#classe responsavel por validar os atributos da conta
class AccountSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = account_model.Account
        load_instance = True

        name = fields.String(required=True)
        resume = fields.String(required=True)
        amount = fields.Float(required=True)