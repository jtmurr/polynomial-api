import unittest

from resources.integration import IntegrationV1, IntegrationV2

v1 = IntegrationV1()
v2 = IntegrationV2()


class IntegrateTest(unittest.TestCase):
    def test_get_v1(self):
        actual = v1.get(0, 1)

        self.assertIsNotNone(actual['ans'])
        self.assertIsNotNone(actual['ans']['y'])
        self.assertIsNotNone(actual['ans']['err'])

    def test_get_v2(self):
        actual = v2.get(0, 1)

        self.assertIsNotNone(actual['y'])
        self.assertIsNotNone(actual['err'])
