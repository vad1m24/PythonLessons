# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def simple_mult(list):
    return list
try:
    n = int(input('Введите значение целочсленной переменной: '))
    arr = []
    if n > 1:
        i = 2
        while i <= n:
            if n % i == 0:
                n = n // i
                arr.append(i)
                i = 1
            i += 1
    print(simple_mult(arr))
except:
    print('Введены некорректные значения')