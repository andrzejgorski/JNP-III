import unittest
from navgar_app.views import my_view
from navgar_core import database as db

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
        session = db.get_db_session()
