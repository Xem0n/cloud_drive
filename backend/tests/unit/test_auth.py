from flaskr import auth
import pytest

from flaskr.auth import authenticate
from flaskr.errors import InvalidCredentialsError

USERNAME = 'username'
PASSWORD = 'password1!23'

def test_auth(app):
    with app.app_context():
        assert authenticate(USERNAME, PASSWORD)

        with pytest.raises(InvalidCredentialsError):
            assert authenticate('invalid username', 'password1!23')
            assert authenticate('username', 'invalid password')
            assert authenticate('invalid username', 'invalid password')