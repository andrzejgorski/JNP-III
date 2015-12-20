from pyramid.config import Configurator
from sqlalchemy import create_engine
from navgar_core import database as db
import yaml



def load_config(config):
    file_name = config.get('config_file', None)
    if file_name is not None:
        with open(file_name, 'r') as stream:
            config.update(yaml.load(stream))
    return config


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    global_config = load_config(global_config)
    db.configure_engine(global_config)

    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('posts/first', '/posts/first')
    config.add_route('test', '/test')
    config.scan()
    return config.make_wsgi_app()
