# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
from random import random

def sequence(list1, list2, list3):
    return list1, list2, list3
try:
    x = int(input('Введите размер целочисленного списка (не более 20 элементов): '))
    if x <= 20:
        max_numb = int(input('Введите максимальное значение списка (от 0 до 10): '))
        if 0 <= max_numb <= 10:
            num_list = [0] * x
            dupl_list = []
            excl_list = []
            for i in range(x):
                num_list[i] = int(random() * max_numb)
            for a in range(x - 1):
                for b in range(a + 1, x):
                    if num_list[a] == num_list[b]:
                        dupl_list.append(num_list[a])
                        a += 1
                        b += 1
            dupl_list = list(set(dupl_list))
            excl_list = list(set(num_list) - set(dupl_list))
            print(sequence(num_list, dupl_list, excl_list))
except:
    print('Введены некорректные значения')