import redis
from flask import Blueprint, current_app
from flask_jwt_extended import (
    JWTManager, 
    jwt_required, 
    create_access_token, 
    get_jwt_identity,
    get_jwt
)

bp = Blueprint('auth', __name__, url_prefix='/auth')

jwt = JWTManager()

jwt_redis_blocklist = redis.StrictRedis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True
)

@bp.route('/login')
def login():
    token = create_access_token(identity='yo')
    return {'token': token}

@bp.route('/logout')
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    access_expires = current_app.config['JWT_ACCESS_TOKEN_EXPIRES']
    jwt_redis_blocklist.set(jti, '', ex=access_expires)

    return {'msg': 'Access token revoked'}

# test purposes
@bp.route('/protected')
@jwt_required()
def protected():
    user = get_jwt_identity()
    return {'user': user}