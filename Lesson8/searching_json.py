import json

with open('employees.json', 'r') as file:
    data = json.load(file)

    for k, v in data.items():
        if v['Sex'] == 'M':
            print(v['Full name'], v['Phone numbers'])
        #print(v['Full name'], v['Sex'])