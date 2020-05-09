from models.integration import IntegrationModelV1, IntegrationModelV2
from tests.base_ut import BaseUT


class IntegrateTest(BaseUT):
    def test_json_v1(self):
        with self.app_context():
            v1 = IntegrationModelV1(1, 2)

            actual = v1.json()

            self.assertIsNotNone(actual['ans'])
            self.assertIsNotNone(actual['ans']['y'])
            self.assertIsNotNone(actual['ans']['err'])

    def test_json_v2(self):
        with self.app_context():
            v2 = IntegrationModelV2(3, 4)

            actual = v2.json()

            self.assertIsNotNone(actual['y'])
            self.assertIsNotNone(actual['err'])
