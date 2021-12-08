import telebot
import constants
from telebot import types

API_TOKEN = '2073493631:AAGMTA4EdsHWFzuM3Dh8tkliNU7OCOjIEmo'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['ves'])
def handle_text (message):
    bot.send_message(message.chat.id, "сколько ты весишь? (в кило, блять)")
    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        txt = message.text
        my_file = open('lohpidr.txt', 'w')
        text_for_file = message.text
        my_file.write(text_for_file)
        bot.send_message(message.chat.id, 'жиробас. я тебя запомнил')
bot.polling() 
