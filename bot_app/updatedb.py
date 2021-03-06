#!/usr/bin/python
# -*- coding: utf-8 -*-

# still bad code, but it seems to work

import pickledb
import requests

url = "http://unidata.xyz/api/unipd/"

# getting keyboardcommands
db = pickledb.load('uniwhereDB.db', False)
r = requests.get(url + 'mensa', timeout=30)
data = r.json()
lastUpdate = str(data['last_update'])
data.pop('last_update', None)
mensaDict = data

for key in mensaDict:
    menuDict = {'primo': "", 'secondo': "", 'contorno': "", 'dessert': ""}
    orari = mensaDict[key]['orari']
    indirizzo = mensaDict[key]['indirizzo']
    if mensaDict[key]['calendario']['pranzo'] == 0:
        pr = "chiuso"
    else:
        pr = "aperto"

    if mensaDict[key]['calendario']['cena'] == 0:
        ce = "chiuso"
    else:
        ce = "aperto"

    calendario = 'Pranzo: ' + pr +\
        '\nCena: ' + ce
    telefono = mensaDict[key]['telefono']
    coord = mensaDict[key]['coord']
    for mkey in mensaDict[key]['menu']:
        for piatto in mensaDict[key]['menu'][mkey]:
            menuDict[mkey] += piatto + '\n'
    txtmenu = ' -- PRIMO --\n' + menuDict['primo'] +\
              ' -- SECONDO --\n' + menuDict['secondo'] + \
              ' -- CONTORNO --\n' + menuDict['contorno'] +\
              ' -- DESSERT --\n' + menuDict['dessert']
    reply = 'Orari: %s\nIndirizzo: %s\nTelefono: %s\n' \
            'Ultimo aggiornamento: %s\n\n%s\n\n%s' % \
            (orari, indirizzo, telefono, lastUpdate, calendario, txtmenu)

    cd = {
        'text': reply,
        'words': db.get(key)['words']
    }
    db.set(key, cd)
db.dump()


r = requests.get(url + 'aulastudio', timeout=30)
data = r.json()
asDict = data
for key in asDict:
    orari = asDict[key]['orario']
    indirizzo = asDict[key]['indirizzo']
    telefono = asDict[key]['tel']
    posti = asDict[key]['posti']
    coord = asDict[key]['coord']
    reply = 'Posti: %s\nIndirizzo: %s\nTelefono: %s\n -- Orari: -- \n%s\n' % \
        (posti, indirizzo, telefono, orari)
    cd = {
        'text': reply,
        'words': db.get(key)['words']
            }
    db.set(key, cd)
db.dump()
