from easygui import *
from input import *
from out import *
from out import result_output
from rational_calc import *

var1 = ''
def start_inteface():
    msg ="Добро пожаловать в калькулятор\nВыберете один из пунтов"
    title = "Калькулятор"
    choices = ["Операции с рациональными числами", "Операции над комплексными числами"]
    choice = choicebox(msg, title, choices)
    choice_interface(choice)
    return str(choice)

def choice_interface (choice):
    global var1
    if choice == "Операции с рациональными числами":
        try:
            text = "Введите данные через пробел\nПример: "
            title = "Операции с рациональными числами"
            d_text = '' # Тут будут вводиться данные
            output = enterbox(text, title, d_text)
            var1 = output[2] # Тут создаем переменную, которую поже будем считывать
            input_numbers(output)
            if output:
                message = str(output) + " = " + str(result_output(ration_nums, el_1, el_3, el_4)) + "\n\nХотите рассчитать снова?"# тут передать данные из функции Вадима
                title = "Решение"
                output = ynbox(message, title,("Да","Нет"))
                if output:
                    choice_interface("Операции с рациональными числами")
                else:
                    choice_interface(start_inteface())
            else:
                choice_interface(start_inteface())
        except:
            exceptionbox()
    elif choice == "Операции над комплексными числами":
        try:
            text = "Введите данные через пробел\nПример: "
            title = "Операции над комплексными числами"
            d_text = "( x1 + iy 1 ) + ( x2 + iy2 ) = ( x1 + x2 ) + i( y1 + y2 )" # Тут берем данные
            output = enterbox(text, title, d_text)
            if output:
                message = str(output) + "=" + "подставить решение\n\nХотите рассчитать снова?" # тут передать данные из функции Вадима
                title = "Решение"
                output = ynbox(message, title,("Да","Нет"))
                if output:
                    choice_interface("Операции над комплексными числами")
                else:
                    choice_interface(start_inteface())
            else:
                choice_interface(start_inteface())
        except:
            exceptionbox()
    return var1
choice_interface(start_inteface())