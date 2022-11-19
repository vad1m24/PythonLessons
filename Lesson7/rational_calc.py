# Калькулятор рациональных чисел
# пример 5 / 4 * 6 / 7 + 3 / 2 - 9
from fractions import Fraction

nums = ''
ration_nums = []
x = 1
el_1 = '*'
el_2 = '/'
el_3 = '-'
el_4 = '+'
condition = None

def input_numbers():
    global nums
    global condition
    nums = input("Введите выражение с рациональными целыми числами используя пробелы между символами и операциями: ")
    nums = nums.split(' ')
    for i in range(len(nums)):
        if nums[i] == el_1 or nums[i] == el_2 or nums[i] == el_3 or nums[i] == el_4:
            condition = True
        elif nums[i].isnumeric():
            condition = True
        else:
            print("Вводить можно лишь целые цифры и операции с ними!")
            input_numbers()
    rational_numbers()

def rational_numbers():
    global ration_nums
    for i in range(len(nums)):
        if nums[i].isnumeric():
            if (i+1) < len(nums):
                if nums[i+1] != el_2 and nums[i-1] != el_2:
                    ration_nums.append(Fraction(int(nums[i]), x))
            elif (i+1) == len(nums):
                if nums[i-1] != el_2:
                    ration_nums.append(Fraction(int(nums[i]), x))
        elif nums[i] == el_2:
            ration_nums.append(Fraction(int(nums[i - 1]), int(nums[i + 1])))
        else:
            ration_nums.append(nums[i])
    result_output()

def result_output():
    while True:
        for i in range(len(ration_nums)):
            if ration_nums[i] == el_1:
                result = ration_nums[i - 1] * ration_nums[i + 1]
                del ration_nums[i + 1]
                del ration_nums[i]
                del ration_nums[i - 1]
                ration_nums.insert(i - 1, result)
                break
        if el_1 not in ration_nums:
            break

    while True:
        for i in range(len(ration_nums)):
            if ration_nums[i] == el_3:
                result = ration_nums[i - 1] - ration_nums[i + 1]
                del ration_nums[i + 1]
                del ration_nums[i]
                del ration_nums[i - 1]
                ration_nums.insert(i - 1, result)
                break
        if el_3 not in ration_nums:
            break

    while True:
        for i in range(len(ration_nums)):
            if ration_nums[i] == el_4:
                result = ration_nums[i - 1] + ration_nums[i + 1]
                del ration_nums[i + 1]
                del ration_nums[i]
                del ration_nums[i - 1]
                ration_nums.insert(i - 1, result)
                break
        if el_4 not in ration_nums:
            break
    print(sum(ration_nums))

def main_rationals():
    input_numbers()

if __name__ == "__main__":
    main_rationals()