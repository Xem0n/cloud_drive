def error_handler(error):
    return {'error': error.description}, error.code