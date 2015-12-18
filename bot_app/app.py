from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/')
def index():
    return 'chissasd....'


@app.route('/receive', methods=['POST'])
def foo():
    data = json.loads(request.data)
    return str(data)


@app.route('/data')
def names():
    data = {
        "first_names": ["John", "Jacob", "Julie", "Jenny"]
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run()
