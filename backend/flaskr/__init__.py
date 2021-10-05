import os
from flask import Flask

from .db import db
from .auth import jwt
from .bcrypt import bcrypt

from .views.auth import bp as auth_blueprint
from .views.files import bp as files_blueprint

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    load_config(app, test_config)
    ensure_instance_folder(app)
    init_extensions(app)
    register_blueprints(app)

    return app

def load_config(app, test_config):
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

def ensure_instance_folder(app):
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

def init_extensions(app):
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    with app.app_context():
        db.create_all()

def register_blueprints(app):
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(files_blueprint)