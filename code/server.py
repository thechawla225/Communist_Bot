from bot import Communist_bot
from telegram.ext import *
import responses as R
import telegram

print("the revolution has began")


bot = telegram.Bot("1723313591:AAFEqRwLck1K_xN-lrrx8j5UhQdwPeeE4Ic")

def start(update,context):
    update.message.reply_text('The Revolution has began comrade')

def help_command(update,context):
    update.message.reply_text('I serve the soviet union, what do u want?')

def handle_message(update,content):
    text = str(update.message.text).lower()
    chatid = update.message.chat_id
    
    response = R.sample_responses(text,chatid)

    update.message.reply_text(response)

def send_gif(chat_id,document = 'https://tenor.com/view/marx-marxism-communism-intesifies-funny-gif-16697750'):
    bot.sendDocument(chat_id, document)

def error(update,context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater("1723313591:AAFEqRwLck1K_xN-lrrx8j5UhQdwPeeE4Ic",use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_handler(MessageHandler(Filters.text,handle_message))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

main()











'''
def make_reply(message):
    reply = "Hello Darling"
    return reply

p = Communist_bot()
print(".....")
updates = p.get_updates()
print(updates)
updates = updates['result']
prev = len(updates)

while True:

    p = Communist_bot()
    print(".....")
    updates = p.get_updates()
    print(updates)
    updates = updates['result']
    if(len(updates)>prev):
        prev = len(updates)
        if updates:
            for item in updates:
                update_id = item["update_id"]
                try:
                    message = item["update_id"]
                except:
                    message = None
                print("Sending Response")
                sender = item["message"]["from"]["id"]
                reply = make_reply(message)
                p.send_message(reply,sender)
'''