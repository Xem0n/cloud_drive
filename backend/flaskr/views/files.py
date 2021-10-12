from functools import wraps
from flask import Blueprint
from flask.globals import current_app, request
from flask.helpers import send_from_directory
from flask_jwt_extended import jwt_required, get_current_user
from flaskr.db import user
from flaskr.db.file import File

bp = Blueprint('files', __name__, url_prefix='/files')

def file_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        user = get_current_user()
        file_id = kwargs.get('file_id', 0)
        file = File.query.filter_by(id=file_id, user_id=user.id).first()

        if not file:
            return {'error': 'Invalid id!'}, 406

        del kwargs['file_id']
        kwargs['file'] = file

        return func(*args, **kwargs)
    
    return decorator

@bp.route('/<int:file_id>', methods=['GET'])
@jwt_required()
@file_required
def download(file):
    return send_from_directory(
        '../' + current_app.config['UPLOAD_FOLDER'],
        file.get_filename(),
        as_attachment=True,
        attachment_filename=file.name
    )

@bp.route('/', methods=['POST'])
@jwt_required()
def upload():
    if 'file' not in request.files:
        return {'error': 'No file sent!'}, 406

    file = File(
        file = request.files['file'],
        user_id = get_current_user().id
    )

    try:
        file.is_valid()
    except Exception as e:
        return {'error': str(e)}, 406
    else:
        file.save()

        return {'msg': 'ok'}