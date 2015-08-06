import orm,asyncio
from models import User, Blog, Comment

def test(loop):
    yield from orm.create_pool(user='root', password='password', db='db_python',loop=loop)
    u = User(name='Test', email='test@example.com', passwd='88888888', image='about:blank')
    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()