from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

app = Flask(__name__)

#configure params from database
app.config.from_object('config')

db = SQLAlchemy(app)

#Habilita o migrate de banco de dados
m1 = Migrate(app, db)

#Habilita o marshmallow para validacao de dados
ma = Marshmallow(app)

from .models import  account_model