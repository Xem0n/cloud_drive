import warnings

from flaskr import create_app

def test_config():
    warnings.filterwarnings('ignore', category=UserWarning)
    warnings.filterwarnings('ignore', category=DeprecationWarning)

    assert not create_app().testing
    assert create_app({'TESTING': True}).testing