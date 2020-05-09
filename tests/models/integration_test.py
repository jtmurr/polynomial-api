import unittest

from models.integration import IntegrationModelV1, IntegrationModelV2

v1 = IntegrationModelV1(1, 2)
v2 = IntegrationModelV2(3, 4)


class IntegrateTest(unittest.TestCase):
    def test_json_v1(self):
        actual = v1.json()

        self.assertIsNotNone(actual['ans'])
        self.assertIsNotNone(actual['ans']['y'])
        self.assertIsNotNone(actual['ans']['err'])

    def test_json_v2(self):
        actual = v2.json()

        self.assertIsNotNone(actual['y'])
        self.assertIsNotNone(actual['err'])
