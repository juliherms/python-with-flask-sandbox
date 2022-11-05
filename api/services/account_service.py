from api import db
from ..models import account_model

def list_accounts():
    accounts = account_model.Account.query.all()
    return accounts

def list_accounts_by_id(id):
    account = account_model.Account.query.filter_by(id=id).first()
    return account

#Salva uma conta no banco de dados
def save_account(account):
    account_bd = account_model.Account(name=account.name, resume=account.resume, amount=account.amount)
    db.session.add(account_bd)
    db.session.commit()
    return account_bd