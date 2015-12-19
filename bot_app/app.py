# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
import arrow
import ConfigParser
from BotReply import BotReply

# get configs from settings.ini
config = ConfigParser.ConfigParser()
config.read('./settings.ini')
Environment = config.get('main', 'environment')
Auth = str(config.get('main', 'auth_token'))
if Environment == 'debug':
    IsDebug = True
else:
    IsDebug = False

# initialize BotReply
br = BotReply()

app = Flask(__name__)


@app.route('/')
def index():
    MyTime = arrow.utcnow().format('YYYY-MM-DD HH:mm:ss ZZ')
    return 'Hello Uniwhere! UtcNow: ' + str(MyTime) + ' ' + Environment


@app.route('/receive', methods=['POST'])
def reply():
    # get the message
    Message = request.get_json(silent=True)
    AuthHeader = request.headers.get('auth-token')
    if AuthHeader == Auth:
        ReplyMessage = br.Reply(Message)
    else:
        ReplyMessage = {
            'error': 'Unauthorized',
            'your token': AuthHeader
        }
        # return the reply
    return jsonify(ReplyMessage)


if __name__ == '__main__':
    app.run(debug=IsDebug)
