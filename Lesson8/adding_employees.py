from db import employees
import json


def building_adding_json(new_employee):
    keys = []
    with open('employees.json', 'r') as file:
        data = json.load(file)
        for k, v in data.items():
            keys.append(k)
    new_empl_key = int(keys[-1]) + 1
    print(new_empl_key)

    casted_phones = [int(item) for item in new_employee[6].split(sep=",")]
    information = {'Full name': new_employee[0], 'Sex': new_employee[1], 'Birth date': new_employee[2],
                   'Marital status': new_employee[3], 'Job title': new_employee[4], 'salary': int(new_employee[5]),
                   'Phone numbers': casted_phones}
    data[new_empl_key] = information

    print(data)

    with open('employees.json', 'w')as file:
        json.dump(data, file, indent=4)