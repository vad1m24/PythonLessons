#  Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
#  стоящих на нечётной позиции.
import random

def f_sum(x, y, z):
    return x, y, z

try:
    x = int(input('Введите размер целочисленного списка: '))
    max_numb = int(input('Введите максимальное значение списка: '))
    min_numb = int(input('Введите минимальное значение списка: '))
    num_list = []
    new_list = []
    sum_num = 0
    for i in range(x):
        num_list.append(random.randint(min_numb, max_numb))
    for y in range(len(num_list)):
        if y % 2 != 0:
            new_list.append(num_list[y])
            sum_num = sum_num + num_list[y]
    print(f_sum(num_list, new_list, sum_num))
except:
    print('Введены некорректные значения')
