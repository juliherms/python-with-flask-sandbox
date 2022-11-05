from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config') #configure params from database

db = SQLAlchemy(app)

m1 = Migrate(app, db) #Habilita o migrate de banco de dados

from .models import  account_model