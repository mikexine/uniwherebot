import requests
import json

# Target Url and auth token, comment to swith between local and production
Url = 'http://localhost:5000/receive'
AuthToken = 'mydebugtoken'

# Url = 'http://46.101.123.6/receive'
# AuthToken = 'difficult'

# POST data
Data = {
    'from': 'Michele',
    'text': 'A sample text!'
}

# POST request without auth_token, result expected: error: unauthorized
Headers = {
    'content-type': 'application/json',
}
Msg = requests.post(Url, headers=Headers, data=json.dumps(Data))
print Msg.json()

# POST request with wrong auth_token, result expected: error: unauthorized
Headers = {
    'content-type': 'application/json',
    'auth-token': 'johnny'
}
Msg = requests.post(Url, headers=Headers, data=json.dumps(Data))
print Msg.json()

# authotized POST request, result expected: sample reply
Head = {
    'content-type': 'application/json',
    'auth-token': AuthToken
}
Msg = requests.post(Url, headers=Head, data=json.dumps(Data))
print Msg.json()

# stress test ??
# for x in range(10000):
#     Msg = requests.post(Url, headers=Headers, data=json.dumps(Data))
#     print Msg.json()
