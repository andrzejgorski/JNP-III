import unittest
from navgar_app.views import (
    my_view,
    get_posts,
)
from navgar_core import database as db

from pyramid import testing


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


class ViewTests(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['project'], 'navgar')

    def test_get_posts(self):
        request = testing.DummyRequest()
        request.params['posts_limit'] = 12
        response = get_posts(request)
        self.assertEqual(response, example_posts)

    def test_db_connection(self):
        session = db.get_db_session()
