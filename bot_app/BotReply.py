# -*- coding: utf-8 -*-
import string
import pickledb
import random


# connect to DB and to "boh" choice
db = pickledb.load('uniwhereDB.db', False)
boh = ['Spiegati meglio!',
       'Mi dispiace ma non ho capito...',
       'Prova a scrivere altro, se ti va ;)']


class BotReply:

    def __init__(self):
        pass

    @classmethod
    def GetKeyword(self, Text):
        TextSplitRaw = (Text.lower()).split()
        TextSplit = [s for s in TextSplitRaw if len(s) >= 4]
        for key in range(len(db.getall())):
            Keyword = db.getall()[key]
            wordList = db.get(Keyword)['words']
            if any(x in wordList for x in TextSplit):
                return Keyword

    @classmethod
    def CreateReply(self, Keyword):
        if Keyword is None:
            return random.choice(boh)
        else:
            return db.get(Keyword)['text']

    def Reply(self, Message):
        # prepare the reply
        User = Message['from']
        RawText = Message['text']
        Text = RawText.encode('utf-8').translate(None, string.punctuation)
        Keyword = BotReply.GetKeyword(Text)
        ReplyText = BotReply.CreateReply(Keyword)
        ReplyMessage = {
                        'to': User,
                        'text': ReplyText
                    }
        return ReplyMessage
