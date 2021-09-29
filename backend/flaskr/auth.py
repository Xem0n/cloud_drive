from flask.globals import request
from flask_jwt_extended import JWTManager, get_jwt_identity

from .bcrypt import bcrypt
from .db.user import User

jwt = JWTManager()

token_blacklist = set()

@jwt.token_in_blocklist_loader
def check_if_token_blacklisted(header, payload):
    jti = payload['jti']

    return jti in token_blacklist

@jwt.user_lookup_loader
def get_user_from_token(header, payload):
    id = payload['sub']
    current_user = User.query.filter_by(id=id).first()

    return current_user

def authenticate(name, password):
    user = User.query.filter_by(name=name).first()

    if user and bcrypt.check_password_hash(user.password, password):
        return user
    else:
        return None