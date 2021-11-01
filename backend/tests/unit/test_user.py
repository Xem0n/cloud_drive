import pytest

from flaskr.bcrypt import bcrypt
from flaskr.db.user import User
from flaskr.errors import InvalidCredentialsError

def test_validation(app):
    with app.app_context():
        valid_user = User(name='name', password='password')

        invalid_login = User(name='inv', password='password')
        invalid_password = User(name='user', password='yo')
        already_exists = User(name='username', password='password')

        assert valid_user.is_valid()

        with pytest.raises(InvalidCredentialsError):
            assert invalid_login.is_valid() is InvalidCredentialsError
            assert invalid_password.is_valid() is InvalidCredentialsError
            assert already_exists.is_valid() is InvalidCredentialsError

def test_encryption():
    user = User(name='user', password='password')
    user.encrypt()

    assert bcrypt.check_password_hash(user.password, 'password')
    assert not bcrypt.check_password_hash(user.password, 'invalid password')