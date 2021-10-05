from flask import Blueprint
from flask_jwt_extended import jwt_required

bp = Blueprint('files', __name__, url_prefix='/files')

@bp.route('/<int:file_id>', methods=['GET'])
@jwt_required()
def download(file_id):
    return {'msg': 'ok', 'file': file_id}