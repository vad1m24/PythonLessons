import telebot
from input import *
from out import *
from out import result_output
from rational_calc import *


API_TOKEN='5956715136:AAE9mU75g0migoqyuOQCJnIXTaccXB2LXqE'
bot = telebot.TeleBot(API_TOKEN)

var1 = ''

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Готов к работе!\nВведите переменные через пробел.")

@bot.message_handler(content_types=['text'])
def reading_message(message):
    global var1
    var1 = message.text
    input_numbers(message.text)
    bot.send_message(message.chat.id,'Решение: ' + message.text + ' = ' + str(result_output(ration_nums, el_1, el_3, el_4)))

bot.polling()