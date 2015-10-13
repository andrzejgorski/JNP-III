import unittest
from .views import my_view
from core import database as db

from pyramid import testing


class ViewTests(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['project'], 'navgar')

    def test_db_connection(self):
        connection = db.get_db_connection()
