from pyramid.view import view_config
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
def my_view(request):
    return {}


@view_config(route_name='posts/first', renderer='json')
def example_post(request):
    return example_posts


@view_config(route_name='test', renderer='json')
def test_view(request):
    redis_server = redis.Redis("localhost")
    redis_server.set("name", "Andrzej")
    value = redis_server.get("name")
    return { 'value': str(value) }
