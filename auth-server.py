import aiohttp
from aiohttp import web
import arrow
import json
import motor.motor_asyncio

mongo_url = 'mongodb://localhost:27017'
mongo_client = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
db = mongo_client['test_db']


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
        else:
            return web.json_response({'status': STATUS.FAIL, 'detail': 'insert db error'})


app = web.Application()
app.router.add_post('/mongo/write', handle_mongo_write)
app.router.add_post('/mongo/read', handle_mongo_read)
app.router.add_post('/mongo/login', handle_mongo_login)
app.router.add_post('/mongo/signup', handle_mongo_signup)
web.run_app(app, port=3001)
