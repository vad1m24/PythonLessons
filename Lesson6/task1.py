# Создайте программу для игры в "Крестики-нолики".

import random

dot_empty = '_'
dot_human = 'X'
dot_ai = 'O'
current_player = 'O'
field = [dot_empty, dot_empty, dot_empty, dot_empty, dot_empty, dot_empty, dot_empty, dot_empty, dot_empty]
continues_game = True

def check_win():
    global continues_game

    def check_rows():
        global continues_game
        row_1 = field[0] == field[1] == field[2] != dot_empty
        row_2 = field[3] == field[4] == field[5] != dot_empty
        row_3 = field[6] == field[7] == field[8] != dot_empty

        if row_1 or row_2 or row_3:
            continues_game = False
            print(current_player + ' победил!')
        else:
            return None

    def check_columns():
        global continues_game
        column_1 = field[0] == field[3] == field[6] != dot_empty
        column_2 = field[1] == field[4] == field[7] != dot_empty
        column_3 = field[2] == field[5] == field[8] != dot_empty

        if column_1 or column_2 or column_3:
            continues_game = False
            print(current_player + ' победил!')
        else:
            return None

    def check_diagonals():
        global continues_game
        diagonal_1 = field[0] == field[4] == field[8] != dot_empty
        diagonal_2 = field[2] == field[4] == field[6] != dot_empty

        if diagonal_1 or diagonal_2:
            continues_game = False
            print(current_player + ' победил!')
        else:
            return None

    def check_draw():
        global continues_game
        if dot_empty not in field:
            continues_game = False
            print("Ничья!")
        else:
            return None

    check_rows()
    check_columns()
    check_diagonals()
    check_draw()

def check_valid_turn(move_verification):
    if field[move_verification] == dot_empty:
        return True
    else:
        return False

def make_turn():

    def make_turn_ai():
        play_move_ai = random.randrange(0, 8, 1)
        if check_valid_turn(play_move_ai) is True:
            field[play_move_ai] = current_player
            print_board()
        else:
            make_turn_ai()

    def make_turn_human():
        print_board()
        try:
            play_move = int(input("Введите координаты Вашего хода. Диапазон от 1 до 9\n"))
            if 0 < play_move < 10:
                play_move = play_move - 1
                if check_valid_turn(play_move) is True:
                    field[play_move] = current_player
                    print_board()
                else:
                    print("Ошибка, данная позиция уже занята! Попробуйте еще раз.")
                    make_turn_human()
            else:
                print("Ошибка, координаты вне диапазона (1 - 9)! Попробуйте еще раз.")
                make_turn_human()
        except:
            print("Проверьте вводимое значение - должны быть только целые числа!")
            make_turn_human()

    if current_player == dot_human:
        make_turn_human()
    else:
        make_turn_ai()

def choose_player(active_player):
    global current_player
    if active_player == dot_human:
        current_player = dot_ai
    else:
        current_player = dot_human
    print("Сейчас ход - " + current_player)
    return current_player

def print_board():
    print("\n")
    print(field[0] + " | " + field[1] + " | " + field[2] + "     1 | 2 | 3")
    print(field[3] + " | " + field[4] + " | " + field[5] + "     4 | 5 | 6")
    print(field[6] + " | " + field[7] + " | " + field[8] + "     7 | 8 | 9")
    print("\n")

def main_game():
    while continues_game is True:
        choose_player(current_player)
        make_turn()
        check_win()

if __name__ == "__main__":
    main_game()
