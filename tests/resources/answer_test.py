from unittest.mock import patch

from sqlalchemy.exc import SQLAlchemyError

from models.answer import AnswerModel
from resources.answer import AnswerList, Answer
from tests.base_test_for_db import BaseDatabaseTest


class AnswerTest(BaseDatabaseTest):
    def test_get_when_answer_exists(self):
        with self.app_context():
            AnswerModel(1, 2, 3, 4).persist()
            answer = Answer()
            expected = {'bounds': {'lower': 1.0, 'upper': 2.0}, 'result': {'err': 4.0, 'y': 3.0}}

            actual = answer.get(1, 2)

            self.assertEqual(actual, expected, 'Wrong results.')

    def test_get_when_lower_bound_exists(self):
        with self.app_context():
            AnswerModel(1, 2, 3, 4).persist()
            answer = Answer()
            expected = ({'message': 'No such answer'}, 404)

            actual = answer.get(1, 3)

            self.assertEqual(actual, expected, 'Wrong results.')

    def test_get_when_upper_bound_exists(self):
        with self.app_context():
            AnswerModel(1, 2, 3, 4).persist()
            answer = Answer()
            expected = ({'message': 'No such answer'}, 404)

            actual = answer.get(3, 2)

            self.assertEqual(actual, expected, 'Wrong results.')

    def test_get_when_answer_not_exists(self):
        with self.app_context():
            answer = Answer()
            expected = ({'message': 'No such answer'}, 404)

            actual = answer.get(1, 2)

            self.assertEqual(actual, expected, 'Wrong results.')

    def test_post_when_answer_exists(self):
        with self.app_context():
            AnswerModel(1, 2, 3, 4).persist()
            answer = Answer()
            expected = ({'message': 'Answer already exists'}, 400)

            actual = answer.post(1, 2, 3, 4)

            self.assertEqual(actual, expected, 'Wrong results.')

    def test_post_when_answer_not_exists(self):
        with self.app_context():
            answer = Answer()
            expected = ({'bounds': {'lower': 1.0, 'upper': 2.0}, 'result': {'err': 4.0, 'y': 3.0}}, 201)

            actual = answer.post(1, 2, 3, 4)

            self.assertEqual(actual, expected, 'Wrong results.')

    @patch.object(AnswerModel, 'persist')
    def test_post_when_exception_raised(self, mock_persist):
        mock_persist.side_effect = SQLAlchemyError()
        with self.app_context():
            answer = Answer()
            expected = ({'message': 'Error persisting answer'}, 500)

            actual = answer.post(1, 2, 3, 4)

            self.assertEqual(actual, expected, 'Wrong results.')


class AnswerListTest(BaseDatabaseTest):
    def test_get(self):
        with self.app_context():
            AnswerModel(1, 2, 3, 4).persist()
            AnswerModel(5, 6, 7, 8).persist()
            answer_list = AnswerList()
            expected = {
                'answers': [
                    {
                        'bounds': {
                            'lower': 1.0,
                            'upper': 2.0
                        },
                        'result': {
                            'err': 4.0,
                            'y': 3.0
                        }
                    },
                    {
                        'bounds': {
                            'lower': 5.0,
                            'upper': 6.0
                        },
                        'result': {
                            'err': 8.0,
                            'y': 7.0
                        }
                    }
                ]
            }

            actual = answer_list.get()

            self.assertEqual(actual, expected, 'Wrong results.')
