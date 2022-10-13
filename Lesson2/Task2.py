# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

N = int(input('Введите число: '))
x = 1
result = 1
arr = []
while x <= N:
    result = result * x
    x = x + 1
    arr.append(result)
print(arr)
