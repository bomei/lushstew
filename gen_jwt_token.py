import jwt

payload = {
    'iss': 'bo-key',
    'path': ['bee', 'yes', 'example.co'],
}

token = jwt.encode(payload, 'bo-secret', algorithm='HS256')

print(token.decode())
