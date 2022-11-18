
str_num = input("Ввеедите выражение: ")
print(str_num)
element_1 = '*'
element_2 = '/'
element_3 = '-'
element_4 = '+'
a = ''
b = ''

while str_num.isnumeric() == False:
    for i in str_num:
        if i == element_1 or i == element_2:
            if i == element_1:
                index = str_num.find(element_1)
                j = 1
                k = 1
                while True:
                    if (index - j) <= 0:
                        break
                    elif str_num[index - j] == element_1 or str_num[index - j] == element_2 or str_num[index - j] == element_3 or str_num[index - j] == element_4:
                        break
                    elif (index - j) > 0:
                        j += 1
                    else:
                        break
                while True:
                    if (index + k) >= (len(str_num) - 1):
                        break
                    elif (str_num[index + k] == element_1) or (str_num[index + k] == element_2) or (str_num[index + k] == element_3) or (str_num[index + k] == element_4):
                        k -= 1
                        break
                    else:
                        k += 1
                ch = str_num[index - j:index + k + 1]
                if (str_num[index - j] != element_1 or str_num[index - j] != element_2 or str_num[index - j] != element_3 or str_num[index - j] != element_4) and ((index - j) >= 0):
                    a = str_num[index - j] + a
                elif str_num[index - j] == element_1 or str_num[index - j] == element_2 or str_num[index - j] == element_3 or str_num[index - j] == element_4:
                    a = (str_num[index - j + 1])
                    ch = str_num[index - j + 1:index + k]
                elif (index - j) > 0:
                    a = str_num[index - j]
                else:
                    a = str_num[index - 1]
                print(a)
                if  (str_num[index + k] != element_1) or (str_num[index + k] != element_2) or (str_num[index + k] != element_3) or (str_num[index + k] != element_4) and ((index + k) < len(str_num)):
                    b = str_num[index + k] + b
                elif (str_num[index + k] == element_1) or (str_num[index + k] == element_2) or (str_num[index + k] == element_3) or (str_num[index + k] == element_4):
                    b = str_num[index + k - 1]
                elif (index + k) < len(str_num):
                    b = int(str_num[index + k - 1])
                else:
                    b = int(str_num[index + 1])
                print(b)
                result = int(a) * int(b)
                a = ''
                b = ''
                print(result)
                if ch == 3:
                    str_num = str(result)
                else:
                    str_num = str_num.replace(ch, str(result))
                print(str_num)

            elif i == element_2:
                index = str_num.find(element_2)
                j = 1
                k = 1
                while True:
                    if (index - j) <= 0:
                        break
                    elif str_num[index - j] == element_1 or str_num[index - j] == element_2 or str_num[index - j] == element_3 or str_num[index - j] == element_4:
                        break
                    elif (index - j) > 0:
                        j += 1
                    else:
                        break
                while True:
                    if (index + k) >= (len(str_num) - 1):
                        break
                    elif (str_num[index + k] == element_1) or (str_num[index + k] == element_2) or (str_num[index + k] == element_3) or (str_num[index + k] == element_4):
                        k -= 1
                        break
                    else:
                        k += 1
                ch = str_num[index - j:index + k + 1]
                if (str_num[index - j] != element_1 or str_num[index - j] != element_2 or str_num[index - j] != element_3 or str_num[index - j] != element_4) and ((index - j) >= 0):
                    a = str_num[index - j] + a
                elif str_num[index - j] == element_1 or str_num[index - j] == element_2 or str_num[index - j] == element_3 or str_num[index - j] == element_4:
                    a = (str_num[index - j + 1])
                    ch = str_num[index - j + 1:index + k]
                elif (index - j) > 0:
                    a = str_num[index - j]
                else:
                    a = str_num[index - 1]
                print(a)
                if  (str_num[index + k] != element_1) or (str_num[index + k] != element_2) or (str_num[index + k] != element_3) or (str_num[index + k] != element_4) and ((index + k) < len(str_num)):
                    b = str_num[index + k] + b
                elif (str_num[index + k] == element_1) or (str_num[index + k] == element_2) or (str_num[index + k] == element_3) or (str_num[index + k] == element_4):
                    b = str_num[index + k - 1]
                elif (index + k) < len(str_num):
                    b = int(str_num[index + k - 1])
                else:
                    b = int(str_num[index + 1])
                print(b)
                result = int(a) / int(b)
                a = ''
                b = ''
                result = int(result)
                print(result)
                if ch == 3:
                    str_num = str(result)
                else:
                    str_num = str_num.replace(ch, str(result))
                print(str_num)

    for i in str_num:
        if i == element_3:
            index = str_num.find(element_3)
            j = 1
            k = 1
            while True:
                if (index - j) <= 0:
                    break
                elif str_num[index - j] == element_1 or str_num[index - j] == element_2 or str_num[index - j] == element_3 or str_num[index - j] == element_4:
                    break
                elif (index - j) > 0:
                    j += 1
                else:
                    break
            while True:
                if (index + k) >= (len(str_num) - 1):
                    break
                elif (str_num[index + k] == element_1) or (str_num[index + k] == element_2) or (str_num[index + k] == element_3) or (str_num[index + k] == element_4):
                    k -= 1
                    break
                else:
                    k += 1
            ch = str_num[index - j:index + k + 1]
            if (str_num[index - j] != element_1 or str_num[index - j] != element_2 or str_num[index - j] != element_3 or str_num[index - j] != element_4) and ((index - j) >= 0):
                a = str_num[index - j] + a
            elif str_num[index - j] == element_1 or str_num[index - j] == element_2 or str_num[index - j] == element_3 or str_num[index - j] == element_4:
                a = (str_num[index - j + 1])
                ch = str_num[index - j + 1:index + k]
            elif (index - j) > 0:
                a = str_num[index - j]
            else:
                a = str_num[index - 1]
            print(a)
            if  (str_num[index + k] != element_1) or (str_num[index + k] != element_2) or (str_num[index + k] != element_3) or (str_num[index + k] != element_4) and ((index + k) < len(str_num)):
                b = str_num[index + k] + b
            elif (str_num[index + k] == element_1) or (str_num[index + k] == element_2) or (str_num[index + k] == element_3) or (str_num[index + k] == element_4):
                b = str_num[index + k - 1]
            elif (index + k) < len(str_num):
                b = int(str_num[index + k - 1])
            else:
                b = int(str_num[index + 1])
            print(b)
            result = int(a) - int(b)
            a = ''
            b = ''
            print(result)
            if ch == 3:
                str_num = str(result)
            else:
                str_num = str_num.replace(ch, str(result))
            print(str_num)

    for i in str_num:
        if i == element_4:
            index = str_num.find(element_4)
            j = 1
            k = 1
            while True:
                if (index - j) <= 0:
                    break
                elif str_num[index - j] == element_1 or str_num[index - j] == element_2 or str_num[index - j] == element_3 or str_num[index - j] == element_4:
                    break
                elif (index - j) > 0:
                    j += 1
                else:
                    break
            while True:
                if (index + k) >= (len(str_num) - 1):
                    break
                elif (str_num[index + k] == element_1) or (str_num[index + k] == element_2) or (str_num[index + k] == element_3) or (str_num[index + k] == element_4):
                    k -= 1
                    break
                else:
                    k += 1
            ch = str_num[index - j:index + k + 1]
            if (str_num[index - j] != element_1 or str_num[index - j] != element_2 or str_num[index - j] != element_3 or str_num[index - j] != element_4) and ((index - j) >= 0):
                a = str_num[index - j] + a
            elif str_num[index - j] == element_1 or str_num[index - j] == element_2 or str_num[index - j] == element_3 or str_num[index - j] == element_4:
                a = (str_num[index - j + 1])
                ch = str_num[index - j + 1:index + k]
            elif (index - j) > 0:
                a = str_num[index - j]
            else:
                a = str_num[index - 1]
            print(a)
            if  (str_num[index + k] != element_1) or (str_num[index + k] != element_2) or (str_num[index + k] != element_3) or (str_num[index + k] != element_4) and ((index + k) < len(str_num)):
                b = str_num[index + k] + b
            elif (str_num[index + k] == element_1) or (str_num[index + k] == element_2) or (str_num[index + k] == element_3) or (str_num[index + k] == element_4):
                b = str_num[index + k - 1]
            elif (index + k) < len(str_num):
                b = int(str_num[index + k - 1])
            else:
                b = int(str_num[index + 1])
            print(b)
            result = int(a) + int(b)
            a = ''
            b = ''
            print(result)
            if ch == 3:
                str_num = str(result)
            else:
                str_num = str_num.replace(ch, str(result))
            print(str_num)
