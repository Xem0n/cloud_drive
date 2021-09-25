from db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(60), unique=False, nullable=False)