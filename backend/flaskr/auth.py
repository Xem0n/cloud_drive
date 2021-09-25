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

bp = Blueprint('auth', __name__, url_prefix='/auth')

jwt = JWTManager()
bcrypt = Bcrypt()

blacklist = set()

@jwt.token_in_blocklist_loader
def check_if_token_blacklisted(header, payload):
    jti = payload['jti']

    return jti in blacklist

@bp.route('/register', methods=['POST'])
def register():
    name = request.form.get('name', '')
    password = request.form.get('password', '')
    password = bcrypt.generate_password_hash(password).decode('utf-8')

    return {'msg': 'Ok'}, 200

@bp.route('/login')
def login():
    token = create_access_token(identity='yo')
    return {'token': token}

@bp.route('/logout')
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    blacklist.add(jti)

    return {'msg': 'Access token revoked'}

# test purposes
@bp.route('/protected')
@jwt_required()
def protected():
    user = get_jwt_identity()
    return {'user': user}