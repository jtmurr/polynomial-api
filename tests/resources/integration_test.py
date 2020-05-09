import unittest
from unittest.mock import patch

from models.integration import IntegrationModelV1, IntegrationModelV2
from resources.integration import IntegrationV1, IntegrationV2

v1 = IntegrationV1()
v2 = IntegrationV2()


class IntegrateTest(unittest.TestCase):
    @patch.object(IntegrationModelV1, 'json')
    def test_get_v1(self, mock_json):
        v1.get(0, 1)

        self.assertTrue(mock_json.called)

    @patch.object(IntegrationModelV2, 'json')
    def test_get_v2(self, mock_json):
        v2.get(0, 1)

        self.assertTrue(mock_json.called)
