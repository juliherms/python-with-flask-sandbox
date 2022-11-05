from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_restful import Api
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

#configure params from database
app.config.from_object('config')

#habilita as metricas do prometheus
metrics = PrometheusMetrics(app)
metrics.info('api_info', 'API info', version='0.1-alpha')

db = SQLAlchemy(app)

#Habilita o migrate de banco de dados
m1 = Migrate(app, db)

#Habilita o marshmallow para validacao de dados
ma = Marshmallow(app)

#Habilita o flask restful
api = Api(app)

from .models import account_model
from .controllers import account_controller