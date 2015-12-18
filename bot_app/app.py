from flask import Flask, jsonify, request
import arrow

app = Flask(__name__)


@app.route('/')
def index():
    return 'chissasd....'


@app.route('/receive', methods=['POST'])
def reply():
    # get the message
    Message = request.get_json(silent=True)
    print Message
    # prepare the reply
    User = Message['from']
    Text = Message['text']
    MyTime = arrow.utcnow().format('YYYY-MM-DD HH:mm:ss ZZ')
    ReplyText = 'Prova: ' + str(Text) + ' ' + str(MyTime)
    ReplyMessage = {
                    'to': str(User),
                    'text': str(ReplyText)
                    }
    # return the reply
    return jsonify(ReplyMessage)


if __name__ == '__main__':
    app.run()
