from aiohttp import web
import json
import arrow
import jwt
import aiohttp

session = aiohttp.ClientSession()
kong_listen = 'http://alihz-debug.qbtrade.org:28000'
kong_admin = 'http://alihz-debug.qbtrade.org:28001'


class User:
    def __init__(self, username, pwd, key=None, secret=None):
        self.username = username,
        self.pwd = pwd
        if key is None:
            self.key = self.username
        if secret is None:
            self.secret = self.username + self.pwd


user_set = dict()


async def handle(request):
    print('/')
    return web.Response(text='Hello, van')


async def create_kong_user(username):
    body = {'username': username, 'custom_id': username}
    async with session.post(f'{kong_admin}/consumers', data=body) as resp:
        return resp


async def create_user_jwt(user: User):
    body = {'secret': user.secret, 'key': user.key}
    async with session.post(f'{kong_admin}/consumers/{user.username}/jwt', data=body) as resp:
        print(1)


async def handle_new_user(request):
    params = request.query
    username = params.get('name', 'Anonymous')
    pwd = params.get('pwd', '')
    key = params.get('key', None)
    secret = params.get('secret', None)
    resp = await create_kong_user(username)  # type: aiohttp.ClientResponse
    if resp.status != 201:
        return web.Response(status=resp.status, reason=resp.reason,
                            text=json.dumps({'status': resp.status, 'reason': resp.reason, 'username': username}))

    user = User(username, pwd, key, secret)
    user_set[username] = user

    sta, resp = await create_user_jwt(user)


async def handle_gentoken(request):
    name = request.query.get('name', 'Anonymous')
    pwd = request.query.get('pwd', None)
    iat = arrow.now()
    exp = iat.replace(seconds=120)
    payload = {
        'username': name,
        'exp': exp.timestamp,
        'iat': iat.timestamp,
        'iss': name
    }
    secret = 'bo-secret'
    token = jwt.encode(payload, secret, algorithm='HS256')
    print(name)
    print(token)
    return web.Response(text=token.decode())


async def handle_userinfo(request):
    token = request.query.get('jwt', '')
    if token == '':
        token = request.query.get('x-access-token', '')
    print(f'token: {token}')
    if token != '':
        payload = jwt.decode(token, 'bobo-secret', algorithms='HS256')
        if payload:
            print(payload)
            return web.Response(text=json.dumps({'Status': 'True', 'Token': token, 'payload': payload}))
    return web.Response(text='token is blank')

async def handle_tolog(request):
    data = await request.post()
    print(arrow.now())
    msg = ''
    for k, v in data.items():
        if len(v) > 0:
            msg = data
            break
        try:
            msg = json.loads(k)

        except:
            msg = k
    print(msg)
    resp = {
        'name': 'hello',
        'action': 'welcome'
    }
    return web.json_response(resp)


async def handle_index(request):
    method = request.method
    url = str(request.url)
    headers = dict(request.headers)
    data = await request.read()
    data = data.decode()
    params = dict(request.query)
    print([method, url, headers, data, params], sep='\n')
    return web.Response(
        text=json.dumps({'method': method, 'url': url, 'headers': headers, 'data': data, 'params': params}), status=200)


app = web.Application()
app.router.add_route('POST', '/tolog', handle_tolog)
app.router.add_get('/jwtex', handle)
app.router.add_get('/jwtex/userinfo', handle_userinfo)
app.router.add_get('/jwtex/gentoken', handle_gentoken)
app.router.add_get('/jwtex/adduser', handle_new_user)
app.router.add_route('*', '/', handle_index)
web.run_app(app, port=44444)
