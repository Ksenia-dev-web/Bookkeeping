import datetime

from application.people import get_employees
from application.salary import calculate_salary

if __name__ == 'main':
    print('Begin')

print(datetime.datetime.now())
calculate_salary()
get_employees()
