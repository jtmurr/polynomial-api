from db import db


class AnswerModel(db.Model):
    __tablename__ = 'answer'

    id = db.Column(db.Integer, primary_key=True)
    lower = db.Column(db.Float)
    upper = db.Column(db.Float)
    y = db.Column(db.Float)
    err = db.Column(db.Float)

    def __init__(self, lower, upper, y, err):
        self.lower = lower
        self.upper = upper
        self.y = y
        self.err = err

    def json(self):
        return {
            'bounds': {
                'lower': self.lower,
                'upper': self.upper
            },
            'result': {
                'y': self.y,
                'err': self.err
            }
        }

    @classmethod
    def find_by_bounds(cls, a, b):
        return cls.query.filter_by(lower=a, upper=b).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    def persist(self):
        db.session.add(self)
        db.session.commit()
