from flask_restful import Resource
from ..schemas import account_schema
from flask import request, make_response, jsonify
from ..entities import account
from ..services import account_service
from api import api

class AccountList(Resource):

    """Método responsável por salva uma conta no banco de dados."""
    def post(self):
        cs = account_schema.AccountSchema()
        validate = cs.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            resume = request.json["resume"]
            amount = request.json["amount"]

            new_account = account.Account(name,resume,amount)
            result = account_service.save_account(new_account)
            return make_response(cs.jsonify(result),201)

api.add_resource(AccountList, '/accounts')