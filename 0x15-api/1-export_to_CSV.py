#!/usr/bin/python3

"""
csv format
"""

import csv
from json import loads
from requests import get
from sys import argv
if __name__ == "__main__":

    employee_id = argv[1]
    file_name = f"{employee_id}.csv"
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos/"\
        .format(employee_id)
    user_url = "https://jsonplaceholder.typicode.com/users/{}"\
        .format(employee_id)

    response_todo = get(todo_url)
    response_user = get(user_url)

    list_emp = response_todo.json()
    user_name = response_user.json().get('username')
    all_data = []
    for i in list_emp:
        temp_l = []
        temp_l.append(str(i.get('userId')))
        temp_l.append(user_name)
        temp_l.append(str(i.get('completed')))
        temp_l.append(i.get('title'))
        all_data.append(temp_l)
    with open(file_name, mode='w', newline='') as fd:
        writer = csv.writer(fd, quoting=csv.QUOTE_ALL)
        for row in all_data:
            writer.writerow(row)
