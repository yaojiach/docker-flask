from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
jwt = JWTManager(app)
api = Api(app)

from models import RevokedToken

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return RevokedToken.is_jti_blacklisted(jti)

from resources import (
    UserRegistration,
    UserLogin,
    UserLogoutAccess,
    UserLogoutRefresh,
    TokenRefresh,
    ProtectedResource,
    OpenResource
)

api.add_resource(UserRegistration, '/api/registration')
api.add_resource(UserLogin, '/api/login')
api.add_resource(UserLogoutAccess, '/api/logout/access')
api.add_resource(UserLogoutRefresh, '/api/logout/refresh')
api.add_resource(TokenRefresh, '/api/token/refresh')
api.add_resource(ProtectedResource, '/api/protected')
api.add_resource(OpenResource, '/api/open')
