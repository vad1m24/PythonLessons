# Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр.
# Через строку нельзя решать.

number = float(input('Введите число: \n'))
number = number * 10 ** 10
sum_num = 0
while number > 0:
    sum_num = sum_num + number % 10
    number = number // 10
print(int(sum_num))
