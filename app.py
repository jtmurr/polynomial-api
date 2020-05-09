from flask import Flask
from flask_restful import Api

from resources.integration import IntegrationV1, IntegrationV2

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
api_v1 = Api(app, prefix='/api/polynomial')

api_v1.add_resource(IntegrationV1, '/v1/integrate/<a>/<b>')
api_v1.add_resource(IntegrationV2, '/v2/integrate/<a>/<b>')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
