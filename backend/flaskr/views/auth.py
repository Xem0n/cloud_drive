from flask import Blueprint, request
from flask_jwt_extended import (
    jwt_required, 
    get_jwt, 
    get_current_user,
    create_access_token
)

from flaskr.auth import authenticate, token_blacklist
from flaskr.db.user import User
from flaskr.errors import UserError

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    name = request.form.get('name', '').strip()
    password = request.form.get('password', '').strip()

    new_user = User(name=name, password=password)
    new_user.is_valid()
    new_user.encrypt()
    new_user.save()

    return {'msg': 'ok'}

@bp.route('/login', methods=['POST'])
@jwt_required(optional=True)
def login():
    user = get_current_user()

    if user:
        raise UserError('Already logged in')

    name = request.form.get('name', '')
    password = request.form.get('password', '')

    user = authenticate(name, password)
    token = create_access_token(identity=user.id)

    return {'token': token}

@bp.route('/logout', methods=['DELETE'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    token_blacklist.add(jti)

    return {'msg': 'Access token revoked'}