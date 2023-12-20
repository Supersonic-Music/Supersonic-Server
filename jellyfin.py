from werkzeug.security import check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

# This is just a mock user for the sake of example
users = {
    "pilot": {
        "password": "rubrub123",  # replace with actual hashed password
        "name": "pilot"
    }
}

def generate_token(secret_key, user):
    s = Serializer(secret_key, expires_in=3600)
    return s.dumps({'user': user}).decode('utf-8')

def authenticate(secret_key, username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return generate_token(secret_key, user['name'])
    else:
        return None