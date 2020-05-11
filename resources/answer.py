from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError

from models.answer import AnswerModel


class Answer(Resource):
    def get(self, a, b):
        answer = AnswerModel.find_by_bounds(float(a), float(b))
        if answer:
            return answer.json()
        return {'message': 'No such answer'}, 404

    def post(self, a, b, y, err):
        if AnswerModel.find_by_bounds(a, b) is not None:
            return {'message': 'Answer already exists'}, 400

        answer = AnswerModel(a, b, y, err)
        try:
            answer.persist()
        except SQLAlchemyError:
            return {'message': 'Error persisting answer'}, 500

        return answer.json(), 201


class AnswerList(Resource):
    def get(self):
        return {'answers': list(map(lambda answer: answer.json(), AnswerModel.get_all()))}
