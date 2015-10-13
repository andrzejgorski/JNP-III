import unittest
from navgar_app.views import (
    main_page,
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

    def test_main_page(self):
        request = testing.DummyRequest()
        info = main_page(request)

    def test_get_posts(self):
        limit = 2

        request = testing.DummyRequest()
        request.params['posts_limit'] = limit

        response = get_posts(request)
        # TODO get response from appi
        response_data = response  # in future response.json()

        self.assertEqual(response_data, example_posts)
        self.assertEqual(len(response_data), limit)

    def test_db_connection(self):
        session = db.get_db_session()
