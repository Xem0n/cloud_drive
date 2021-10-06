from flask import Blueprint, request
from flask_jwt_extended import (
    jwt_required, 
    get_jwt, 
    get_current_user,
    create_access_token
)

from flaskr.auth import authenticate, token_blacklist
from flaskr.db.user import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    name = request.form.get('name', '').strip()
    password = request.form.get('password', '').strip()

    new_user = User(name=name, password=password)

    try:
        new_user.is_valid()
    except Exception as e:
        return {'error': str(e)}, 406
    else:
        new_user.encrypt()
        new_user.save()

        return {'msg': 'Ok'}, 200

@bp.route('/login', methods=['POST'])
@jwt_required(optional=True)
def login():
    user = get_current_user()

    if user:
        return {'error': 'Already logged in!'}, 403
    else:
        name = request.form.get('name', '')
        password = request.form.get('password', '')
        user = authenticate(name, password)

        if user:
            token = create_access_token(identity=user.id)

            return {'token': token}
        else:
            return {'error': 'Wrong credentials!'}, 406

@bp.route('/logout', methods=['DELETE'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    token_blacklist.add(jti)

    return {'msg': 'Access token revoked'}