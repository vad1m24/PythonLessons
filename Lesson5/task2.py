#  Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (здесь только буквы).
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open("accordion_1.txt", "r") as file:
    my_text = file.read()

print(my_text)

def compression(w):
    new_str = ''
    i = 0
    count = 1
    while i < len(w) - 1:
        if i + 1 < len(w) and w[i] == w[i + 1]:
            count += 1
            i += 1
        else:
            new_str += str(count) + w[i]
            i += 1
            count = 1
    return new_str
new_str = compression(my_text)
print(new_str)

with open("accordion_2.txt", "w") as file:
    file.write(new_str)


with open("accordion_2.txt", "r") as file:
    new_text = file.read()

def recovery(w):
    recov_str = ''
    count = ''
    for element in w:
        if element.isdigit():
            count += element
        else:
            recov_str += element * int(count)
            count = ''
    return recov_str
recov_str = recovery(new_text)

with open("accordion_3.txt", "w") as file:
    file.write(recov_str)
