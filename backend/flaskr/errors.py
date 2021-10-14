from werkzeug.exceptions import HTTPException

class FileError(HTTPException):
    code = 406

class InvalidCredentialsError(HTTPException):
    code = 406

class UserError(HTTPException):
    code = 403