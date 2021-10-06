from sqlalchemy.orm import backref
from . import db
from flaskr.bcrypt import bcrypt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(60), unique=False, nullable=False)
    files = db.relationship('File', backref='user', lazy=True)

    def is_valid(self):
        if not 3 < len(self.name) < 80:
            raise InvalidNameError('Invalid username!')

        if len(self.password) < 8 or len(self.password) > 16:
            raise InvalidPasswordError('Invalid password!')

        if User.query.filter_by(name=self.name).first():
            raise AlreadyExistsError('User with given name already exists!')

        return True

    def encrypt(self):
        self.password = bcrypt.generate_password_hash(self.password).decode('utf-8')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<User %s - %s>' % (self.name, self.password)

class InvalidNameError(Exception):
    pass

class InvalidPasswordError(Exception):
    pass

class AlreadyExistsError(Exception):
    pass