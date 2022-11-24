from db import *


with open('employees.json', 'w') as db:
    json.dump(employees, db, indent=4)


