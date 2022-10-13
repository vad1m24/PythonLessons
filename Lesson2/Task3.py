# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# Нельзя юзать find или count.

text1 = input('Введите предложение 1: \n')
text2 = input('Введите предложение 2: \n')
count = 0
for duplicate in range(len(text2) - len(text1) + 1):
    if text1[duplicate:duplicate + len(text2)] == text2:
        count = count + 1
print(count)