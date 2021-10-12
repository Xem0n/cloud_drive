import os
from datetime import datetime
from flask import current_app
from . import db

class File(db.Model):
    # id serves as a path too to avoid injecting files with invalid names 
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, file, **kwargs):
        self.file = file
        kwargs['name'] = file.filename

        super().__init__(**kwargs)

    def is_valid(self):
        if self.name.strip() == '':
            raise InvalidFilenameError('Invalid filename!')

        return True

    def save(self):
        db.session.add(self)
        db.session.commit()

        self.save_file()
    
    def save_file(self):
        upload_folder = current_app.config['UPLOAD_FOLDER']
        filename = self.get_filename()
        path = os.path.join(upload_folder, filename)

        try:
            os.mkdir(upload_folder)
        except:
            pass

        self.file.save(path)

    def get_filename(self):
        _, extension = os.path.splitext(self.name)
        filename = str(self.id).strip() + extension

        return filename.strip()

    def update_name(self, name):
        name = name.strip()
        _, extension = os.path.splitext(self.name)
        extension = extension.strip()

        if extension == '':
            extension = self.name

        self.name = name + extension

        self.is_valid()
        db.session.commit()

    def __repr__(self):
        return '<File - %s>' % self.name

class InvalidFilenameError(Exception):
    pass