import requests
import json

# Target Url and auth token, comment to swith between local and production
# Url = 'http://localhost:5000/receive'
# AuthToken = 'mydebugtoken'

Url = 'http://46.101.123.6/receive'
AuthToken = 'difficult'

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
