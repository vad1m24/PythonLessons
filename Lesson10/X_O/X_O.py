import telebot
from telebot import types
import random

API_TOKEN='5956715136:AAE9mU75g0migoqyuOQCJnIXTaccXB2LXqE'
bot = telebot.TeleBot(API_TOKEN)

dot_empty = '_'
dot_human = '❌'
dot_ai = '⭕️'
current_player = None
field = [dot_empty, dot_empty, dot_empty, dot_empty, dot_empty, dot_empty, dot_empty, dot_empty, dot_empty]
continues_game = True
item = {}
keyboard = None
win_rows = None
win_colomns = None
win_diagonals = None

def print_board(message):
    global keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    for i in range(len(field)):
        item[i] = types.InlineKeyboardButton(field[i], callback_data=str(i))
    keyboard.row(item[0], item[1], item[2])
    keyboard.row(item[3], item[4], item[5])
    keyboard.row(item[6], item[7], item[8])
    bot.send_message(message.chat.id, 'Вот ваше поле', reply_markup=keyboard)

def check_win():
    global continues_game

    def check_rows():
        global continues_game
        global win_rows
        row_1 = field[0] == field[1] == field[2] != dot_empty
        row_2 = field[3] == field[4] == field[5] != dot_empty
        row_3 = field[6] == field[7] == field[8] != dot_empty

        if row_1 or row_2 or row_3:
            win_rows = True
            continues_game = False
        else:
            return None

    def check_columns():
        global continues_game
        global win_colomns
        column_1 = field[0] == field[3] == field[6] != dot_empty
        column_2 = field[1] == field[4] == field[7] != dot_empty
        column_3 = field[2] == field[5] == field[8] != dot_empty

        if column_1 or column_2 or column_3:
            win_colomns = True
            continues_game = False
        else:
            return None

    def check_diagonals():
        global continues_game
        global win_diagonals
        diagonal_1 = field[0] == field[4] == field[8] != dot_empty
        diagonal_2 = field[2] == field[4] == field[6] != dot_empty

        if diagonal_1 or diagonal_2:
            win_diagonals = True
            continues_game = False
        else:
            return None

    check_rows()
    check_columns()
    check_diagonals()
check_win()

@bot.message_handler(commands=['start'])
def welcome(message):
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item[0] = types.KeyboardButton("Сыграть в ❌ ⭕️")
    item[1] = types.KeyboardButton("Отказаться")
    buttons.add(item[0], item[1])
    if message.text == "/start":
        bot.send_message(message.chat.id, "Привет, {0.first_name}! Поиграем с тобой?)".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=buttons)

@bot.message_handler(content_types=['text'])
def mess(message):
    if message.text == "Сыграть в ❌ ⭕️":
        if continues_game is True:
            print_board(message)
    elif message.text == "Отказаться":
        bot.send_message(message.chat.id, "Ты заходи, если что...")
        bot.stop_polling()
    else:
        bot.send_message(message.chat.id, "Мая твая не панимать!")

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if (call.message):

        def ai_turn():
            play_move_ai = random.randrange(0, 8, 1)
            if field[play_move_ai] == dot_empty:
                field[play_move_ai] = dot_ai
                check_win()
                if win_rows or win_colomns or win_diagonals is True:
                    bot.send_message(call.message.chat.id, '⭕️победил!')
                    bot.stop_polling()
            else:
                ai_turn()
        ai_turn()

        def human_turn():
            for i in range(9):
                if call.data == str(i):
                    if (field[i] == dot_empty):
                        field[i] = dot_human
                    check_win()
                    if win_rows or win_colomns or win_diagonals is True:
                        bot.send_message(call.message.chat.id, '❌  победил!')
                        bot.stop_polling()

                item[i] = types.InlineKeyboardButton(field[i], callback_data=str(i))
        human_turn()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Крестики нолики", reply_markup=None)

        global keyboard
        keyboard.row(item[0], item[1], item[2])
        keyboard.row(item[3], item[4], item[5])
        keyboard.row(item[6], item[7], item[8])
        bot.send_message(call.message.chat.id, "Выбери клетку", reply_markup=keyboard)



bot.polling()