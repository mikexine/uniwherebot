# -*- coding: utf-8 -*-
import string
import pickledb

# keywords
MensaKeywords = ['mensa', 'mense', 'pranzo', 'fame']
AulaStudioKeywords = ['aula', 'aulastudio', 'aula studio',
                      'studio', 'esami', 'studiare', 'esame']
MensaList = ['piovego', 'forcellini', 'murialdo', 'belzoni',
             'acli', 'agripolis', 'francesco', 'sanfrancesco']
AulaStudioList = ['galilei', 'jappelli', 'marsala', 'pollaio',
                  'venezia', 'viavenezia', 'branca',
                  'tito', 'livio', 'titolivio']


class BotReply:

    def __init__(self):
        pass

    @classmethod
    def GetKeyword(self, Text):
        TextSplit = (Text.lower()).split()
        for x in range(len(MensaList)):
            if MensaList[x] in TextSplit:
                Keyword = MensaList[x]
                if Keyword == 'francesco' or Keyword == 'sanfrancesco':
                    Keyword = 'sanfrancesco'
                return Keyword
        for x in range(len(AulaStudioList)):
            if AulaStudioList[x] in TextSplit:
                Keyword = AulaStudioList[x]
                if Keyword == 'venezia' or Keyword == 'viavenezia':
                    Keyword = 'viavenezia'
                elif Keyword == 'tito' or Keyword == 'livio' \
                                or Keyword == 'titolivio':
                    Keyword = 'titolivio'
                elif Keyword == 'branca':
                    Keyword = 'vbranca'
                return Keyword
        for x in range(len(MensaKeywords)):
            if MensaKeywords[x] in TextSplit:
                return 'mensa'
        for x in range(len(AulaStudioKeywords)):
            if AulaStudioKeywords[x] in TextSplit:
                return 'aulastudio'

    @classmethod
    def CreateReply(self, Keyword):
        if Keyword is None:
            return 'Spiegati meglio!'
        else:
            mydb = pickledb.load('LocalData.db', False)
            return mydb.get(Keyword)['text']

    def Reply(self, Message):
        # prepare the reply
        User = Message['from']
        RawText = (Message['text'])
        Text = RawText.encode('utf-8').translate(None, string.punctuation)
        Keyword = BotReply.GetKeyword(Text)
        ReplyText = BotReply.CreateReply(Keyword)
        ReplyMessage = {
                        'to': User,
                        'text': ReplyText
                    }
        return ReplyMessage
