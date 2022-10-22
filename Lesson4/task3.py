#  Задана натуральная степень k.
#  Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
#  и записать в файл многочлен степени k.
import random

def degree_num(k):
    try:
        k = int(input('Введите степень k: '))
        return k
    except:
        print('Введены некорректные значения')
degree = degree_num('Введите степень: ')

def polynomial():
    try:
        pln = []
        min_numb = 0
        max_numb = 100
        num = random.randint(min_numb, max_numb)
        if degree > 0:
            for i in range(degree + 1, 0, -1):
                num = random.randint(min_numb, max_numb)
                pln.append(num)
                if i-1 == 0:
                    break
                else:
                    pln.extend('x')
                    if i-1 == 1:
                        pln.extend('+')
                    else:
                        pln.extend('^')
                        pln.append(i-1)
                        pln.extend('+')
            pln.extend('=0')
        elif num == 0:
            pln = [num, '=', 0]
        else:
            print('ОШИБКА!')
            pln = [num, '!=', 0]
        return pln
    except:
        print('Введены некорректные значения')
list = polynomial()

print(list)

def add_file_txt():
    with open("polynomials", "a") as my_file:
        my_file.write(" ".join(map(str, list)))
    with open("polynomials", "a") as my_file:
        my_file.write("\n")
    return my_file
text = add_file_txt()