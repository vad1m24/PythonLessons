# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Функции FIND и COUNT юзать нельзя.

try:
    text1 = input('Введите основной текст: \n').split()
    text2 = input('Введите искомый текст: \n')
    text3 = []
    for i in range(len(text1)):
         if text2 not in text1[i]:
             text3.append(text1[i])
    print(text3)
except:
    print('Некорректный ввод')
