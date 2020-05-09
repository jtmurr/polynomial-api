import unittest

from app import app


class BaseUT(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context