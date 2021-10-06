from flask import Blueprint
from flask.globals import request
from flask_jwt_extended import jwt_required, get_current_user
from flaskr.db.file import File

bp = Blueprint('files', __name__, url_prefix='/files')

@bp.route('/<int:file_id>', methods=['GET'])
@jwt_required()
def download(file_id):
    return {'msg': 'ok'}

@bp.route('/', methods=['POST'])
@jwt_required()
def upload():
    if 'file' not in request.files:
        return {'error': 'No file sent!'}

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