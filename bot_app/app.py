from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'Is it reacaahu ahsdiahsidha'


@app.route('/data')
def names():
    data = {
        "first_names": ["John", "Jacob", "Julie", "Jenny"]
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run()
