from pyramid.view import view_config
from navgar_core import database as db
import redis


example_posts = [
    {
        'author': 'Adam',
        'content': 'Cześć wszystkim!'
    },
    {
        'author': 'Marcin',
        'content': 'Co tam?'
    }
]


@view_config(route_name='home', renderer='templates/home.pt')
def main_page(request):
    return {}


@view_config(route_name='posts/first', renderer='json')
def get_posts(request):
    posts_limit = request.params['posts_limit']
    # posts = (
    #     db.query(Posts)
    #     .order_by(Posts.date)
    #     .limit(posts_limit)
    #     .all()
    # )
    return example_posts


@view_config(route_name='test', renderer='json')
def test_view(request):
    redis_server = redis.Redis("localhost")
    redis_server.set("name", "Andrzej")
    value = redis_server.get("name")
    return { 'value': str(value) }
