import re
import requests
from flask import jsonify
import telegram


bot = telegram.Bot("1723313591:AAFEqRwLck1K_xN-lrrx8j5UhQdwPeeE4Ic")

def sample_responses(text,chat_id):
    i = 7

    text = text.split(" ")
    text = [re.sub('[^a-zA-Z0-9]+', '', _) for _ in text]

    capitalists = ['biden','obama','america','trump' ,'lincoln','canada']
    random_gifs = [
    'https://tenor.com/view/communiste-communist-hugs-heart-red-gif-14360509',
    'https://tenor.com/view/comunismo-comunista-rojo-marx-stalin-gif-11647520',
    'https://tenor.com/view/capigifs-gomez-castro-communism-gif-13106558',
    'https://tenor.com/view/simpsons-lenin-crush-capitalism-funny-gif-5488019',
    'https://tenor.com/view/heart-love-mustache-change-color-gif-17567673',
    'https://tenor.com/view/communism-communist-stalin-gif-5148588',
    'https://tenor.com/view/marx-marxism-communism-intesifies-funny-gif-16697750',
    'https://tenor.com/view/carlos-marx-marx-karl-marx-gif-11822631',
    'https://tenor.com/view/communism-communist-dance-gif-5148596',
    'https://tenor.com/view/cccp-flag-wave-star-logo-gif-16196191',
    'https://tenor.com/view/elmo-communism-gif-19427247',
    ]

    answer = ""

    if(text == "how to start a revolution?"):
        
        send_gif(chat_id,'https://tenor.com/view/dancing-dance-communism-communist-meme-gif-15834108')
    else:
        for txt in text:
            if(txt == "image"):
                break
            if(txt in capitalists):
                i = 0
                break
            if(txt == "me"):
                i = 1
                text = " ".join(text)
                answer = text.replace("me","Us*")
                break
            if(txt == "i"):
                i = 2
                break
            if(txt == "fact"):
                i = 3
                break

    
    switcher={
        0:'We do not talk about those Capitalist Shits here, comrade ',
        1: answer,
        2:'Comrade! there is no "I" in Communsm ',
        3:'',
        4:'Thursday',
        5:'Friday',
        6:'Saturday'
    }
    return switcher.get(i,"My Commie brain can't digest what you said comrade")


    
def send_image(chat_id):
    bot.send_photo(chat_id,photo=open('stalin.jpg','rb'))

def get_gif():
    random_gifs = [
    'https://tenor.com/view/communiste-communist-hugs-heart-red-gif-14360509',
    'https://tenor.com/view/comunismo-comunista-rojo-marx-stalin-gif-11647520',
    'https://tenor.com/view/capigifs-gomez-castro-communism-gif-13106558',
    'https://tenor.com/view/simpsons-lenin-crush-capitalism-funny-gif-5488019',
    'https://tenor.com/view/heart-love-mustache-change-color-gif-17567673',
    'https://tenor.com/view/communism-communist-stalin-gif-5148588',
    'https://tenor.com/view/marx-marxism-communism-intesifies-funny-gif-16697750',
    'https://tenor.com/view/carlos-marx-marx-karl-marx-gif-11822631',
    'https://tenor.com/view/communism-communist-dance-gif-5148596',
    'https://tenor.com/view/cccp-flag-wave-star-logo-gif-16196191',
    'https://tenor.com/view/elmo-communism-gif-19427247',
    ]


    
