import aiohttp
from aiohttp import web
import arrow
import json
import motor.motor_asyncio

mongo_url = 'mongodb://localhost:27017'
mongo_client = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
db = mongo_client['test_db']


async def handle_mongo_write(request):
    data = await request.post()
    print(data)
    mark = data.get('mark')
    info = data.get('info')
    res = await db.test_collection.update_one({'mark': mark}, {'$set': {'info': info}}, True)
    return web.json_response({'status': 'OK'})


async def handle_mongo_read(request):
    data = await request.post()
    mark = data.get('mark')
    doc = await db.test_collection.find_one({'mark': mark})
    print(doc)
    del doc['_id']
    return web.json_response(doc)


app = web.Application()
app.router.add_post('/mongo/write', handle_mongo_write)
app.router.add_post('/mongo/read', handle_mongo_read)
web.run_app(app, port=3001)
