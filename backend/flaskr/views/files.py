from functools import wraps
from flask import Blueprint
from flask.globals import request
from flask_jwt_extended import jwt_required, get_current_user

from flaskr.db import db, user
from flaskr.db.file import File
from flaskr.errors import FileError

bp = Blueprint('files', __name__, url_prefix='/files')

def file_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        user = get_current_user()
        file_id = kwargs.get('file_id', 0)
        file = File.query.filter_by(id=file_id, user_id=user.id, deleted=False).first()

        if not file:
            raise FileError('Invalid id!')

        del kwargs['file_id']
        kwargs['file'] = file

        return func(*args, **kwargs)
    
    return decorator

@bp.route('/<int:file_id>', methods=['GET'])
@jwt_required()
@file_required
def download(file):
    return file.download()

@bp.route('/<int:file_id>', methods=['PATCH'])
@jwt_required()
@file_required
def update(file):
    new_name = request.form.get('name', '')

    file.update_name(new_name)
    file.is_valid()
    db.session.commit()

    return {'msg': 'ok'}

@bp.route('/<int:file_id>', methods=['DELETE'])
@jwt_required()
@file_required
def delete(file):
    file.delete()

    return {'msg': 'ok'}

@bp.route('/', methods=['POST'])
@jwt_required()
def upload():
    if 'file' not in request.files:
        raise FileError('No file sent!')

    file = File(
        file = request.files['file'],
        user_id = get_current_user().id
    )

    file.is_valid()
    file.save()

    return {'msg': 'ok'}