import json

def del_el(msg):
    with open('employees.json', 'r') as file:
        data = json.load(file)
        for k, v in data.items():
            if v['Full name'] == msg:
                del data[k]
                break
    with open('employees.json', 'w')as file:
        json.dump(data, file, indent=4)
