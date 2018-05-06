import aiohttp
from aiohttp import web
import arrow
import json
import motor.motor_asyncio
import hashlib, hmac
import arrow
import time


mongo_url = 'mongodb://localhost:27017'
mongo_client = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
db = mongo_client['test_db']

session = aiohttp.ClientSession()


class STATUS:
    FAIL = 'FAIL'
    SUCCESS = 'SUCCESS'


async def handle_mongo_write(request):
    data = await request.post()
    print(data)
    mark = data.get('mark')
    info = data.get('info')
    res = await db.info_repo.update_one({'mark': mark}, {'$set': {'info': info}}, True)
    if res.acknowledged is True:
        return web.json_response({'status': STATUS.SUCCESS})
    else:
        return web.json_response(({'status': STATUS.FAIL}))


async def handle_mongo_read(request):
    data = await request.post()
    print(data)
    mark = data.get('mark')
    doc = await db.info_repo.find_one({'mark': mark})
    if doc is None:
        return web.json_response({})
    print(doc)
    del doc['_id']
    return web.json_response(doc)


async def handle_mongo_login(request):
    data = await request.post()
    print(data)
    account = data.get('account')
    doc = await db.users.find_one({'account': account})
    if doc is None:
        return web.json_response({})
    print(doc)
    del doc['_id']
    return web.json_response(doc)


async def handle_mongo_signup(request):
    data = await request.post()
    print(data)
    account = data.get('account')
    doc = await db.users.find_one({'account': account})
    if doc is not None:
        return web.json_response({'status': STATUS.FAIL, 'detail': 'Account name used!'})
    else:
        password = data.get('password')
        res = await db.users.insert_one({'account': account, 'password': password})
        if res.acknowledged is True:
            return web.json_response({'status': STATUS.SUCCESS})

        return web.json_response({'status': STATUS.FAIL, 'detail': 'insert db error'})


async def handle_mongo_new_key(request):
    body = await request.post()
    print(body)
    mark = body.get('mark')
    async with session.get(
            'https://www.random.org/integers/?num=32&min=0&max=15&col=32&base=2&format=plain&rnd=new') as resp:
        text = await resp.text()
        key = hex(int(text.replace('\t', '').replace('\n', ''), 2))[2:].upper()
        res = await db.key_repo.update_one({'mark': mark}, {'$set': {'key': key}}, True)
        if res.acknowledged is True:
            return web.json_response({'status': STATUS.SUCCESS, 'key': key})
        else:
            return web.json_response({'status': STATUS.FAIL, 'detail': 'db error'})


async def handle_mongo_check(request):
    body = await request.post()
    mark = body.get('mark')
    code = body.get('code')
    res = await db.key_repo.find_one({'mark': mark})
    key = res['key']
    how_far = 5
    code_list = await get_code_list(key, arrow.now().timestamp, how_far=how_far)
    if code in code_list:
        return web.json_response({'status': STATUS.SUCCESS})
    return web.json_response({'status': STATUS.FAIL, 'detail': f'No match code in closest {how_far} interval'})


async def get_code_list(key, timestamp, how_far: int):
    nonce = timestamp // 30
    res = []
    for i in range(how_far):
        res.append(f'{genCode(key,nonce+i):06d}')
        res.append(f'{genCode(key,nonce-i):06d}')
    print(res)
    return res


def genCode(password, nonce):
    # print(password,nonce)
    raw = str(nonce)
    hex = hmac.new(password.encode(), raw.encode(), hashlib.sha1).hexdigest()
    start = int(hex[-1], 16)
    big_int = int(hex[start:start + 8], 16)
    code = big_int % 1000000
    return code


app = web.Application()
app.router.add_post('/mongo/write', handle_mongo_write)
app.router.add_post('/mongo/read', handle_mongo_read)
app.router.add_post('/mongo/login', handle_mongo_login)
app.router.add_post('/mongo/signup', handle_mongo_signup)
app.router.add_post('/mongo/key', handle_mongo_new_key)
app.router.add_post('/mongo/check', handle_mongo_check)
web.run_app(app, port=3001)
