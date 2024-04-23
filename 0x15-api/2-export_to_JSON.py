#!/usr/bin/python3

"""
json format
"""

from json import loads, dumps
from requests import get
from sys import argv
if __name__ == "__main__":

    employee_id = argv[1]
    file_name = f"{employee_id}.json"
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos/"\
        .format(employee_id)
    user_url = "https://jsonplaceholder.typicode.com/users/{}"\
        .format(employee_id)

    response_todo = get(todo_url)
    response_user = get(user_url)

    list_emp = response_todo.json()
    user_name = response_user.json().get('username')
    temp_data = []
    all_data = {}
    for i in list_emp:
        temp_dic = {}
        temp_dic["task"] = i.get('title')
        temp_dic["completed"] = i.get('completed')
        temp_dic["username"] = user_name
        temp_data.append(temp_dic)
    all_data[str(list_emp[0].get('userId'))] = temp_data
    print(all_data)
    with open(file_name, mode="w") as fd:
        fd.write(dumps(all_data))
