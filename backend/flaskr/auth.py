from flask import Blueprint, current_app
from flask.globals import request
from flask_jwt_extended import (
    JWTManager, 
    jwt_required, 
    create_access_token, 
    get_jwt_identity,
    get_jwt
)
from flask_bcrypt import Bcrypt
from .db import db
from .db.user import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

jwt = JWTManager()
bcrypt = Bcrypt()

token_blacklist = set()

@jwt.token_in_blocklist_loader
def check_if_token_blacklisted(header, payload):
    jti = payload['jti']

    return jti in token_blacklist

@bp.route('/register', methods=['POST'])
def register():
    name = request.form.get('name', '')
    password = request.form.get('password', '')

    new_user = User(name=name, password=password)

    try:
        new_user.is_valid()
    except Exception as e:
        return {'error': str(e)}, 406
    else:
        new_user.encrypt(bcrypt)

        db.session.add(new_user)
        db.session.commit()

        return {'msg': 'Ok'}, 200

@bp.route('/login')
def login():
    token = create_access_token(identity='yo')
    return {'token': token}

def authenticate(name, password):
    pass

@bp.route('/logout')
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    token_blacklist.add(jti)

    return {'msg': 'Access token revoked'}

# test purposes
@bp.route('/protected')
@jwt_required()
def protected():
    user = get_jwt_identity()
    return {'user': user}