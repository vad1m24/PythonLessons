#  Задайте список из вещественных чисел.
#  Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
def diff_of_num(x, y, z):
    return x, y, z
try:
    num_list = [5.5, 8.4, 6.2, 7.9, 2.7, 0.3, 4.6]
    max_value = 0
    min_value = 10**10
    for i in range(1, int(len(num_list))):
        if (num_list[i] > num_list[i - 1]) and (num_list[i] > max_value):
            max_value = num_list[i]
        elif (num_list[i] < num_list[i - 1]) and (num_list[i] < min_value):
            min_value = num_list[i]
    diff_values = (max_value - min_value) % 1
    print(diff_of_num(max_value, min_value, round(diff_values, 3)))
except:
    print('Введены некорректные значения')
