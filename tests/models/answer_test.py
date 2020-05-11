from models.answer import AnswerModel
from tests.base_test_for_db import BaseDatabaseTest


class AnswerModelTest(BaseDatabaseTest):
    def test_json(self):
        with self.app_context():
            actual = AnswerModel(1, 2, 3, 4).json()

            self.assertIsNotNone(actual['bounds'])
            self.assertIsNotNone(actual['bounds']['lower'])
            self.assertIsNotNone(actual['bounds']['upper'])
            self.assertIsNotNone(actual['result'])
            self.assertIsNotNone(actual['result']['y'])
            self.assertIsNotNone(actual['result']['err'])

    def test_persist(self):
        with self.app_context():
            AnswerModel(1, 2, 3, 4).persist()

            self.assertIsNotNone(AnswerModel.find_by_bounds(1, 2))
