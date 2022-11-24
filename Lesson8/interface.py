from easygui import *
from building_json import *
from searching_json import *

key = ''
def start_inteface():
    msg ="Добро пожаловать"
    title = "База данных работников"
    choices = ["Отбор сотрудников по ID", "Отбор сотрудников по ФИО", "Отбор сотрудников по полу", "Отбор сотрудников по дате рождения", "Отбор сотрудников по номеру телефона", "Отбор сотрудников по должности", "Отбор сотрудников по заработной плате", "Корректировка информации сотрудников", "Изменение списка сотрудников"]
    choice = choicebox(msg, title, choices)

    return str(choice)

def choice_interface (choice):
    global key

    return key
choice_interface(start_inteface())