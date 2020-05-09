from flask_restful import Resource

from polymath import Polymath


def integrate(a, b):
    return Polymath.integrate(float(a), float(b))


class IntegrationV1(Resource):
    def get(self, a, b):
        y, err = integrate(a, b)
        return {
            'ans': {
                'y': y,
                'err': err
            }
        }


class IntegrationV2(Resource):
    def get(self, a, b):
        y, err = integrate(a, b)
        return {
            'y': y,
            'err': err
        }
