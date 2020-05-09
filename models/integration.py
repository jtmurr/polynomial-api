class IntegrationModel():
    def __init__(self, y, err):
        self.y = y
        self.err = err


class IntegrationModelV1(IntegrationModel):
    def json(self):
        return {
            'ans': {
                'y': self.y,
                'err': self.err
            }
        }


class IntegrationModelV2(IntegrationModel):
    def json(self):
        return {
            'y': self.y,
            'err': self.err
        }
