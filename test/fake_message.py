# -*- coding: utf-8 -*-

import requests
import json
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('./test_settings.ini')
Ask = raw_input('Test in debug or production? Insert D or P: ')
EnvSet = False

while EnvSet is not True:
    if Ask == 'D':
        Url = config.get('debug', 'url')
        AuthToken = config.get('debug', 'auth_token')
        EnvSet = True
    elif Ask == 'P':
        Url = config.get('production', 'url')
        AuthToken = config.get('production', 'auth_token')
        EnvSet = True
    else:
        Ask = raw_input('Test in debug or production? Insert D or P: ')

print Url

# Faking messages
try:
    while True:
        # Sender = raw_input('Send a message from: ')
        Sender = 'mikexine'
        Text = raw_input('Text in the message: ')
        Headers = {
            'content-type': 'application/json',
            'auth-token': AuthToken
        }
        Data = {
            'from': Sender,
            'text': Text
        }
        Msg = requests.post(Url, headers=Headers, data=json.dumps(Data))
        print Msg
        print Msg.json()
except KeyboardInterrupt:
    print 'interrupted!'
