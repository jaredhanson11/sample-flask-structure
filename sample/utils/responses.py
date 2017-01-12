def error(err_message, status_code=400):
    return {'error': err_message}, status_code, {'Content-Type': 'application/json'}
