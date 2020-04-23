from flask import Flask, jsonify
from polymath import Polymath

app = Flask(__name__)
app.config['TESTING'] = True

@app.route('/integrate/<a>/<b>/', methods=['GET'])
def get_integral(a, b):
    pm = Polymath()
    y, err = pm.integrate(float(a), float(b))
    return jsonify({
        'y': y,
        'err': err
    })


app.run(port=3000)
