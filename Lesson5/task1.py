# Создайте программу для игры с конфетами человек против бота.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
import random

start_candy = 2021
min_candy = 1
max_candy = 28

def game_lottery(c):
    candy = start_candy
    c = random.randint(1, 2)
    if c == 1:
        print('Твой ход, загребай!')
        while candy >= 0:
            hum_turn = int(input('Сколько конфет заберем?: '))
            if 1 <= hum_turn <= 28:
                print('Хорошо, такой ход возможен.')
            else:
                print('Мошенничество! Игра остановлена - ты проиграл!.')
                break
            candy = candy - hum_turn
            if candy == 0:
                print('Ты победил и забрал конфеты последним!')
                break
            elif candy < 0:
                print('Больше, чем есть не заберешь. Но ты победил и забрал остаток конфет последним!')
                break
            else:
                print('Хорошо, осталось ', candy, ' конфет')
            io_turn = random.randint(min_candy, max_candy)
            print('Компьютер заберет: ', io_turn, 'конфет')
            candy = candy - io_turn
            if candy == 0:
                print('Компьютер победил и забрал конфеты последним!')
                break
            elif candy < 0:
                print('Попытка зачтена. Компьютер победил и забрал конфеты последним!')
                break
            else:
                print('Осталось конфет: ', candy)
    else:
        print('Ход компа')
        while candy >= 0:
            io_turn = random.randint(min_candy, max_candy)
            print('Компьютер заберет: ', io_turn, 'конфет')
            candy = candy - io_turn
            if candy == 0:
                print('Компьютер победил и забрал конфеты последним!')
                break
            elif candy < 0:
                print('Попытка зачтена. Компьютер победил и забрал конфеты последним!')
                break
            else:
                print('Осталось конфет: ', candy)
            hum_turn = int(input('Сколько конфет заберем?: '))
            if 1 <= hum_turn <= 28:
                print('Хорошо, такой ход возможен.')
            else:
                print('Мошенничество! Игра остановлена - ты проиграл!.')
                break
            candy = candy - hum_turn
            if candy == 0:
                print('Ты победил и забрал конфеты последним!')
                break
            elif candy < 0:
                print('Больше, чем есть не заберешь. Но ты победил и забрал остаток конфет последним!')
                break
            else:
                print('Хорошо, осталось ', candy, ' конфет')
winner = game_lottery('Игра началась.')
