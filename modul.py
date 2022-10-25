import csv
import json
from pathlib import Path
import re


def start_the_point(point):
    employees = read_csv()
    if point == 1:
        emp = find_employee(int(input("Введите ID сотрудника: ")))
        print(emp)
    elif point == 2:    
        result = find_emp_post(employees)
        print(result)
    elif point == 3:
        result = find_employees_by_salary_range(employees)
        print(result)
    elif point == 4:
        id = input('Введите ID: ')
        last_name = input('Введите фамилию: ')
        first_name = input('Введите Имя: ')
        position = input('Введите Должность: ')
        phone_number = input('Введите Номер телефона: ')
        salary = input('Введите Зарплату: ')
        create(id, last_name, first_name, position, phone_number, salary)
    elif point ==5:
        emp = int(input('Введите ID сотрудника: '))
        delete(emp, employees)

    elif point == 7:
        print('Ты молодец, так держать')
    else:
        print(
            '\nТакого пункта нет.\nCоответствуйте меню.')

def read_csv() -> list:
    employee = []
    with open(Path.cwd() / 'database.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = {}
            temp["id"] = int(row[0])
            temp["last_name"] = row[1]
            temp["first_name"] = row[2]
            temp["position"] = row[3]
            temp["phone_number"] = row[4]
            temp["salary"] = float(row[5])
            employee.append(temp)
    return employee


def read_json() -> list:
    employee = []
    with open(Path.cwd() / 'database02.json', 'r', encoding='utf-8') as fin:
        for line in fin:
            temp = json.loads(line.strip())
            employee.append(temp)
    return employee


def write_csv(employees: list):
    with open(Path.cwd() / 'database.csv', 'w', encoding='utf-8') as fout:
        csv_writer = csv.writer(fout)
    for employee in employees:
        csv_writer.writerow(employee.values())


def write_json(employees: list):
    with open(Path.cwd() / 'database02.json', 'w', encoding='utf-8') as fout:
        for employee in employees:
            fout.write(json.dumps(employee) + '\n')


def find_employees_by_salary_range(employees: list) -> list:
    result = []
    lo, hi = get_salary_range()
    for employee in employees:
        if lo <= employee["salary"] <= hi:
            result.append(employee)
    return result

def get_salary_range():
    lo = int(input('Введите начало диапазона зарплаты: '))
    hi = int(input('Введите конец диапазона зарплаты: '))
    return (lo, hi)

def find_emp_post(employees: list) -> list:
    result = []
    post = input('Введите должность: ')
    for employee in employees:
        if employee["position"] == post:
            result.append(employee)
    return result 

def find_employee(id):
    employees = read_csv()

    for employee in employees:
        if employee['id'] == id:
            return employee

def create(id = '', last_name = '', first_name = '', position = '', phone_number = '', salary = ''):
    if(id == ''):
        print("Error: NO id")
        return
    if(last_name == ''):
        print("Error: NO last_name")
        return
    if(first_name == ''):
        print("Error: NO first_name")
        return
    if(position == ''):
        print("Error: NO position")
        return
    if(phone_number == ''):
        print("Error: NO phone_number")
        return
    if(salary == ''):
        print("Error: NO salary")
        return
    db = []
    new_row = [id, last_name,
               first_name, position, phone_number, salary]
    db.append(new_row)
    
    addinf_new(new_row)

def delete(emp:int, employees:list):
    for employee in employees:
        if employee['id'] == emp:
            employees.remove(employees[emp])
    write_csv(employees)


#в процесе, заебавсь
def addinf_new(new_row):
    with open('database.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_row)