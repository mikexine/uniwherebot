import requests
import json
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('test_settings.ini')
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
