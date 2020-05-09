from flask_restful import Resource

from models.integration import IntegrationModelV1, IntegrationModelV2
from polymath import Polymath


def integrate(a, b):
    return Polymath.integrate(float(a), float(b))


class IntegrationV1(Resource):
    def get(self, a, b):
        y, err = integrate(a, b)
        return IntegrationModelV1(y, err).json()


class IntegrationV2(Resource):
    def get(self, a, b):
        y, err = integrate(a, b)
        return IntegrationModelV2(y, err).json()
