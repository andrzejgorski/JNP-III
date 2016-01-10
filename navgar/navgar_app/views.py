from pyramid.view import view_config
from navgar_core import database as db
import redis


session = db.create_db_session()


@view_config(route_name='home', renderer='templates/home.pt')
def main_page(request):
    return {}


@view_config(route_name='posts/most_popular', renderer='json')
def get_most_popular_posts(request):
    most_popular_posts = [
        {
            'author': 'Adam',
            'content': 'Lorem Ipsum'
        },
        {
            'author': 'Marcin',
            'content': 'Pecunia non olet'
        }
    ]
    # Andrzej FIXME: I can't be hardcoded :)
    return most_popular_posts

@view_config(route_name='users/most_popular', renderer='json')
def get_most_popular_users(request):
    most_popular_users = [
        {
            'id' : 1,
            'user': 'Jan Kowalski',
            'followers': 100
        },
        {
            'id' : 2,
            'user': 'Michał Adamczyk',
            'followers': 90
        },
        {
            'id' : 3,
            'user': 'Adam Konserwa',
            'followers': 60
        },
    ]
    # Andrzej FIXME: I can't be hardcoded :)
    return most_popular_users


# @view_config(route_name='test', renderer='json')
# def test_view(request):
#     redis_server = redis.Redis("localhost")
#     redis_server.set("name", "Andrzej")
#     value = redis_server.get("name")
#     return { 'value': str(value) }
