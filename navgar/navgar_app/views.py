from pyramid.view import view_config
from navgar_core import database as db


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
    return {'project': 'navgar'}


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
