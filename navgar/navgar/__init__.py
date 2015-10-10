from pyramid.config import Configurator
from sqlalchemy import create_engine


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    engine = create_engine('sqlite:///:memory:', echo=True)

    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('posts/first', '/posts/first')
    config.add_route('test', '/test')
    config.scan()
    return config.make_wsgi_app()
