#!/usr/bin/python3
"""
display todo list by id
"""

from json import loads
from requests import get
from sys import argv


if __name__ == "__main__":

    employee_id = argv[1]
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos/"\
        .format(employee_id)
    user_url = "https://jsonplaceholder.typicode.com/users/{}"\
        .format(employee_id)

    response_todo = get(todo_url)
    response_user = get(user_url)

    list_emp = response_todo.json()
    EMPLOYEE_NAME = response_user.json()['name']
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = len(list_emp)
    TASK_TITLE = ""
    for i in list_emp:
        if i['completed']:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE += i['title'] + "\n"

    print(f"Employee {EMPLOYEE_NAME} is done with tasks\
            {NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}")
    print(TASK_TITLE, end="")
