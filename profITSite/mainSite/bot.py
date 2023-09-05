import telebot

TOKEN = '6442093653:AAFTCnrGTLjmZIC8rPkGXCvR3UjaK4thQVc'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

def start_bot():
    bot.polling()