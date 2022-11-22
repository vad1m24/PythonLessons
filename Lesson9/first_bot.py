import telebot
import json


API_TOKEN='5956715136:AAE9mU75g0migoqyuOQCJnIXTaccXB2LXqE'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Готов к работе!")

films=['Мортал комбат', "Матрица"]
@bot.message_handler(commands=['show'])
def show_message(message):
    bot.send_message(message.chat.id,' '.join(films))

calc = False
@bot.message_handler(commands=['calc'])
def calc_message(message):
    global calc
    #eq = message.text.split()[1:]
    #print(eq[0])
    #print(eval(eq[0]))
    calc=True
    bot.send_message(message.chat.id,'А теперь введите выражение для расчета')

@bot.message_handler(content_types='text')
def check_message(message):
    global calc
    if 'привет' in message.text:
        bot.send_message(message.chat.id,'И тебе привет коли не шутишь!')
    if calc:
        calc=False
        bot.send_message(message.chat.id,'результат равен '+str(eval(message.text)))





bot.polling()
