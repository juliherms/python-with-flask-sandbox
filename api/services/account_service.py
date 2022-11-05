from api import db
from ..models import account_model

#Salva uma conta no banco de dados
def save_account(account):
    account_bd = account_model.Account(name=account.name, resume=account.resume, amount=account.amount)
    db.session.add(account_bd)
    db.session.commit()
    return account_bd