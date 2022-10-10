# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# V или
# ⋀ и
# ¬ не
try:
    print('Если значение верно - введите t, если ложно - введите f')
    t = True
    f = False
    x = bool(input('Введите значение X: '))
    y = bool(input('Введите значение Y: '))
    z = bool(input('Введите значение Z: '))
    leftSide = not (x or y or z)
    rightSide = not x and not y and not z
    result = leftSide == rightSide
    if (result == True):
        print('Утверждение верно')
    else:
        print('Утверждение ложно')
except:
    print('Введены некорректные данные')