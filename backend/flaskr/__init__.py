import os
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    load_config(app, test_config)
    ensure_instance_folder(app)
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

def register_blueprints(app):
    from . import auth
    app.register_blueprint(auth.bp)