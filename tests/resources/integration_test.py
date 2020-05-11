import unittest
from unittest.mock import patch

from sqlalchemy.exc import SQLAlchemyError

from models.answer import AnswerModel
from models.integration import IntegrationModelV1, IntegrationModelV2
from polymath import Polymath
from resources.integration import IntegrationV1, IntegrationV2, Integration
from tests.base_test_for_db import BaseDatabaseTest

v1 = IntegrationV1()
v2 = IntegrationV2()


class IntegrationTest(BaseDatabaseTest):
    @patch.object(Polymath, 'integrate')
    def test_integrate(self, integrate_mock):
        Integration.integrate(1, 2)

        self.assertTrue(integrate_mock.called_with(1, 2))

    def test_persist_success(self):
        with self.app_context():
            actual_first = Integration.persist(1, 2, 3, 4)
            actual_second = Integration.persist(1, 2, 3, 4)

            self.assertEqual(actual_first, 1, 'Wrong first return value.')
            self.assertEqual(actual_second, 3, 'Wrong second return value.')

    @patch.object(AnswerModel, 'persist')
    def test_persist_fail(self, mock_persist):
        mock_persist.side_effect = SQLAlchemyError()
        with self.app_context():
            expected = 2

            actual = Integration.persist(1, 2, 3, 4)

            self.assertEqual(actual, expected, 'Wrong results.')


class IntegrationV1Test(unittest.TestCase):
    @patch.object(IntegrationModelV1, 'json')
    @patch.object(Integration, 'persist')
    def test_get_v1(self, mock_json, mock_persist):
        v1.get(0, 1)

        self.assertTrue(mock_json.called)
        self.assertTrue(mock_persist.called)


class IntegrationV2Test(unittest.TestCase):
    @patch.object(IntegrationModelV2, 'json')
    @patch.object(Integration, 'persist')
    def test_get_v2(self, mock_json, mock_persist):
        v2.get(0, 1)

        self.assertTrue(mock_json.called)
        self.assertTrue(mock_persist.called)
