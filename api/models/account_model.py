from api import db

#Tabela responsavel por representar uma conta
class Account(db.Model):
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    resume = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)