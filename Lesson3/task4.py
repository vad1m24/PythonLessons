# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Нельзя использовать готовые функции.
def bin_num(dem, bin):
    return dem, bin
try:
    x = int(input('Введите целое число: '))
    y = ''
    n = x
    while x > 0:
        z = str(x % 2)
        y = z + y
        x = int(x / 2)
    print(bin_num(n, y))
except:
    print('Введены некорректные значения')