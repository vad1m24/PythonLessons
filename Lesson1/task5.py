# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры.
# Отсортировать элементы по возрастанию слева направо и сверху вниз.

import random
try:
    print('Задайте размеры двумерного массива')
    x = int(input('Введите количество строк: '))
    y = int(input('Введите вколичество столбцов: '))
    maxNumber = int(input('Введите максимальное число массива: '))
    minNumber = int(input('Введите минимальное число массива: '))
    if (maxNumber > minNumber):
        doubleList = []
        for i in range(x):
            doubleList.append([])
            for j in range(y):
                doubleList[i].append(random.randint(minNumber, maxNumber))
        print(doubleList)
        finalList = sum(doubleList, [])
        finalList.sort()
        print(finalList)
    else:
        print('Ошибка, максимальное число не может быть больше минимального')
except:
    print('Введены некорректные данные')