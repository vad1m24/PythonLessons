import telebot
from telebot import types
import json
from searching_json import *
from building_json import *
from reading_json import *
import del_json


API_TOKEN='5956715136:AAE9mU75g0migoqyuOQCJnIXTaccXB2LXqE'
bot = telebot.TeleBot(API_TOKEN)

new_empl_info = {}
keys = []
phones = []

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Готов к работе!")

@bot.message_handler(commands=['build'])
def build_message(message):
    try:
        building_first_json()
        bot.send_message(message.chat.id,"ваш json-файл написан")
        bot.send_message(message.chat.id, json.dumps(data, indent=4, sort_keys=True))
    except:
        bot.send_message(message.chat.id, "Что-то пошло не так, попробуй еще раз")

@bot.message_handler(commands=['add'])
def adding_message(message):
    bot.send_message(message.chat.id, "Давайте заполним данные нового сотрудника для удобного поиска в базе данных.")
    adding_empl(message)

def adding_empl(message):
    msg = bot.send_message(message.chat.id, 'Введите ФИО нового работника')
    bot.register_next_step_handler(msg, fio_empl)

def fio_empl(message):
    global new_empl_info
    new_empl_info['Full name'] = message.text
    msg = bot.send_message(message.chat.id, 'Введите пол (F / M) нового работника')
    bot.register_next_step_handler(msg, sex_empl)

def sex_empl(message):
    new_empl_info['Sex'] = message.text
    msg = bot.send_message(message.chat.id, 'Введите дату рождения нового работника (dd.mm.year)')
    bot.register_next_step_handler(msg, age_empl)

def age_empl(message):
    new_empl_info['Birth date'] = message.text
    msg = bot.send_message(message.chat.id, 'Введите семейное положение нового работника')
    bot.register_next_step_handler(msg, marital_status_empl)

def marital_status_empl(message):
    new_empl_info['Marital status'] = message.text
    msg = bot.send_message(message.chat.id, 'Введите должность нового работника')
    bot.register_next_step_handler(msg, job_title_empl)

def job_title_empl(message):
    new_empl_info['Job title'] = message.text
    msg = bot.send_message(message.chat.id, 'Введите заработную плату нового работника')
    bot.register_next_step_handler(msg, salary_empl)

def salary_empl(message):
    new_empl_info['salary'] = int(message.text)
    msg = bot.send_message(message.chat.id, 'Введите первый телефонный номер нового работника')
    bot.register_next_step_handler(msg, phone_1)

def phone_1(message):
    global phones
    ph_1 = message.text
    phones.append(int(ph_1))
    msg = bot.send_message(message.chat.id, 'Введите второй телефонный номер нового работника')
    bot.register_next_step_handler(msg, phone_2)

def phone_2(message):
    global phones
    ph_2 = message.text
    phones.append(int(ph_2))
    ending_dict(message)

def ending_dict(message):
    new_empl_info['Phone numbers'] = phones
    adding_id(message)

def adding_id(message):
    with open('employees.json', 'r') as file:
        data = json.load(file)
        for k, v in data.items():
            keys.append(k)
    new_empl_key = int(keys[-1]) + 1
    data[new_empl_key] = new_empl_info
    with open('employees.json', 'w')as file:
        json.dump(data, file, indent=4)
    bot.send_message(message.chat.id, "Новый сотрудник добавлен.")
    bot.send_message(message.chat.id, json.dumps(data, indent=4))

@bot.message_handler(commands=['search'])
def search_empl(message):
    msg = bot.send_message(message.chat.id, "Введите данные сотрудника.")
    bot.register_next_step_handler(msg, search_empl_json)

def search_empl_json(message):
    msg = message.text
    searching_el(msg)
    bot.send_message(message.chat.id, json.dumps(results, indent=4))

@bot.message_handler(commands=['delete'])
def delete_empl(message):
    msg = bot.send_message(message.chat.id, "Введите ФИО сотрудника которого хотите удалить.")
    bot.register_next_step_handler(msg, delete_empl_json)

def delete_empl_json(message):
    msg = message.text
    del_json.del_el(msg)
    bot.send_message(message.chat.id, "Сотрудник удален.")
    bot.send_message(message.chat.id, del_json.json.dumps(employees, indent=4))


bot.polling()