from flask import Flask
from flask_restful import Api

from resources.answer import AnswerList, Answer
from resources.integration import IntegrationV1, IntegrationV2

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///answers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app, prefix='/api/polynomial')

api.add_resource(IntegrationV1, '/v1/integrate/<a>/<b>')
api.add_resource(IntegrationV2, '/v2/integrate/<a>/<b>')

api.add_resource(AnswerList, '/v1/answers')
api.add_resource(Answer, '/v1/answer/<a>/<b>')

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(port=5000, debug=True)
