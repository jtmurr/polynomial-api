import unittest

from models.integration import IntegrationModelV1, IntegrationModelV2
from resources.integration import IntegrationV1, IntegrationV2

v1 = IntegrationV1()
v2 = IntegrationV2()


class IntegrateTest(unittest.TestCase):
    def test_get_v1(self):
        actual = v1.get(0, 1)

        self.assertIs(type(actual), IntegrationModelV1)

    def test_get_v2(self):
        actual = v2.get(0, 1)

        self.assertIs(type(actual), IntegrationModelV2)
