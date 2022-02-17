import random

Hello = ('hello','hey','hii','hi')

reply_Hello = ('hello sir , i am jerry...',
                'hey.whats Up',
                 'hey how are you?')

Bye = ('bye','exit','sleep')

reply_bye  = ("bye sir",
"thanks for using me sir, have a good day",
"good bye sir")
how_are_you = ("how are you")

reply_how = ("i am fine sir, what about a you")

nice = ('nice','good','well')

reply_nice = ("thanks sir")

functions = ['functions','abilities','what can you do']

reply_functions = ('i can perform may tasks, how can i help you?',
'i can call to your G.F',
'i can message your mom that you are not studying',
'i can tell your class teacher that you had attended all the online classes on insta, facebook etc',
'if you want me to tell my features , call : print features')

sorry_reply = ("Sorry")

def Chatterbot(text):
    text = str(text)

    for word in text.split():
        if word in Hello:
            reply = random.choice(reply_Hello)

            return reply

        elif word in Bye:

            reply = random.choice(reply_bye)

            return reply

        elif word in how_are_you:

            reply = random.choice(reply_how)

            return reply

        else:

            return random.choice(sorry_reply)

