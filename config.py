DEBUG=True

USERNAME='api-accounts'
PASSWORD='accounts'
SERVER='localhost'
DB='account-management'

SQLALCHEMY_DATABASE_URI=f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS=True

SECRET_KEY='chave_secreta1'