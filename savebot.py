import telebot
import constants
from telebot import types

API_TOKEN = '2073493631:AAGMTA4EdsHWFzuM3Dh8tkliNU7OCOjIEmo'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
  sent = bot.send_message(message.chat.id, 'Please describe your problem.')
  bot.register_next_step_handler(sent, hello)

def hello(message):
    my_file = open('lohpidr.txt', 'w').write('pidaras', 'w')
    text_for_file = 'Some text here...'
    my_file.write(text_for_file)
    bot.send_message(message.chat.id, 'Thank you!')
bot.polling() 