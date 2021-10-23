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
        'SECRET_KEY': b'\xe5\x03%\xf5\x99\xb8N\xc7\x1b2h\xdc-;T\xb5\x8b\x86\xde\xf6\xb4\x7f\x9aO',
        'JWT_SECRET_KEY': b'\x02C\xfc\x00\xb9\xb0\xcf\xda\xd6bi\x027\xec\xc7\xba\x9d\xab\xfb\x16\x89\xe4m5'
    })

    with app.app_context():
        db.engine.execute(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)