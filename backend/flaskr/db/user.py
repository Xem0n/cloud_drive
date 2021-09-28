from . import db

class InvalidNameError(Exception):
    pass

class InvalidPasswordError(Exception):
    pass

class AlreadyExistsError(Exception):
    pass

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(60), unique=False, nullable=False)

    def is_valid(self):
        if len(self.name) < 3:
            raise InvalidNameError('Invalid username!')

        if len(self.password) < 8 or len(self.password) > 16:
            raise InvalidPasswordError('Invalid password!')

        if User.query.filter_by(name=self.name).first() is not None:
            raise AlreadyExistsError('User with given name already exists!')

        return True

    def encrypt(self, bcrypt):
        self.password = bcrypt.generate_password_hash(self.password).decode('utf-8')

    def __repr__(self):
        return '<User %s - %s>' % (self.name, self.password)