from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_access_token, 
    create_refresh_token, 
    jwt_required, 
    jwt_refresh_token_required, 
    get_jwt_identity, 
    get_raw_jwt,
    get_jti
)
from run import db
from models import User, RevokedToken


parser_user_access = reqparse.RequestParser()
parser_user_access.add_argument('email', required=True)
parser_user_access.add_argument('password', required=True)

parser_revoke = reqparse.RequestParser()
parser_revoke.add_argument('refresh_token', required=True)

parser_refresh = reqparse.RequestParser()
parser_refresh.add_argument('access_token', required=True)

class UserRegistration(Resource):
    def post(self):
        data = parser_user_access.parse_args()
        email = data.get('email')
        password = data.get('password')
        if User.find_by_email(email):
            return {'message': f'Email {email} already exists'}
        user = User(
            email=email,
            password_hash=User.generate_hash(password)
        )
        try:
            db.session.add(user)
            db.session.commit()
            access_token = create_access_token(identity=email)
            refresh_token = create_refresh_token(identity=email)
            return (
                {
                    'message': f'User {email} was created',
                    'access_token': access_token,
                    'refresh_token': refresh_token
                },
                200
            )
        except:
            return ({'message': 'Something went wrong'}, 500)


class UserLogin(Resource):
    def post(self):
        data = parser_user_access.parse_args()
        email = data.get('email')
        password = data.get('password')
        current_user = User.find_by_email(email)
        if not current_user:
            return {'message': f"Email {email} doesn't exist"}
        if User.verify_hash(password, current_user.password_hash):
            access_token = create_access_token(identity=email)
            refresh_token = create_refresh_token(identity=email)
            return {
                'message': f'Logged in as {current_user.email}',
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        else:
            return {'message': 'Invalid credentials'}
      
      
class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        data = parser_revoke.parse_args()
        refresh_token = data.get('refresh_token')
        jti = get_raw_jwt()['jti']
        refresh_jti = get_jti(refresh_token)
        try:
            revoked_token = RevokedToken(jti=jti)
            revoked_token.revoke()
            revoked_token = RevokedToken(jti=refresh_jti)
            revoked_token.revoke()
            return {'message': 'Access and refresh token has been revoked'}
        except:
            return ({'message': 'Something went wrong'}, 500)
      
      
class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedToken(jti=jti)
            revoked_token.revoke()
            return {'message': 'Refresh token has been revoked'}
        except:
            return ({'message': 'Something went wrong'}, 500)
      
      
class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        data = parser_refresh.parse_args()
        old_access_token = data.get('access_token')
        jti = get_raw_jwt()['jti']
        refresh_jti = get_jti(refresh_token)
        current_user = get_jwt_identity()
        # Refresh new access token
        access_token = create_access_token(identity=current_user)
        # Revoke old access token
        revoked_token = RevokedToken(jti=old_access_token)
        revoked_token.revoke()
        return {'access_token': access_token}


class OpenResource(Resource):
    def get(self):
        return {
            'message': 'This is a message'
        }

class ProtectedResource(Resource):
    @jwt_required
    def get(self):
        return {
            'message': 'This is a secret'
        }
