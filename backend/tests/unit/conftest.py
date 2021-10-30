import os
import tempfile

import pytest

from flaskr import create_app
from flaskr.db import db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf-8')

@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///' + db_path,
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'SECRET_KEY': os.urandom(24),
        'JWT_SECRET_KEY': os.urandom(24)
    })

    with app.app_context():
        db.engine.execute(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)