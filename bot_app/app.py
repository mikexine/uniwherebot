# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, render_template
import ConfigParser
from BotReply import BotReply

# initialize BotReply get configs from settings.ini
br = BotReply()
config = ConfigParser.ConfigParser()
config.read('./settings.ini')
Environment = config.get('main', 'environment')
Auth = str(config.get('main', 'auth_token'))
if Environment == 'debug':
    IsDebug = True
else:
    IsDebug = False

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/call_receive')
def receive():
    return render_template('receive.html')


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
