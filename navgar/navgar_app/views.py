from pyramid.view import view_config

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
def example_post(request):
    return example_posts
