# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random

def pair_of_numbers(x, y):
    return x, y

try:
    x = int(input('Введите размер целочисленного списка: '))
    max_numb = int(input('Введите максимальное значение списка: '))
    min_numb = int(input('Введите минимальное значение списка: '))
    num_list = []
    for i in range(x):
        num_list.append(random.randint(min_numb, max_numb))
    half_list = int(len(num_list)/2)
    if(int((len(num_list))%2)) != 0:
        half_list +=1
    new_list = []
    mult_num = 0
    n = -1
    for i in range(half_list):
        mult_num = num_list[i] * num_list[n]
        new_list.append(mult_num)
        i += 1
        n -= 1
    print(pair_of_numbers(num_list, new_list))
except:
    print('Введены некорректные значения')
