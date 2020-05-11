from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError

from models.answer import AnswerModel
from models.integration import IntegrationModelV1, IntegrationModelV2
from polymath import Polymath


class Integration(Resource):
    @staticmethod
    def integrate(a, b):
        return Polymath.integrate(float(a), float(b))

    @staticmethod
    def persist(a, b, y, err):
        if AnswerModel.find_by_bounds(a, b) is None:
            answer = AnswerModel(a, b, y, err)
            try:
                answer.persist()
                return 1
            except SQLAlchemyError:
                return 2
        return 3


class IntegrationV1(Integration):
    def get(self, a, b):
        y, err = Integration.integrate(a, b)
        Integration.persist(a, b, y, err)
        return IntegrationModelV1(y, err).json()


class IntegrationV2(Integration):
    def get(self, a, b):
        y, err = Integration.integrate(a, b)
        Integration.persist(a, b, y, err)
        return IntegrationModelV2(y, err).json()
