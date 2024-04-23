#!/usr/bin/python3

"""
json format
"""

from json import loads, dumps
from requests import get
from sys import argv

if __name__ == "__main__":

    file_name = "todo_all_employees.json"
    user_url = "https://jsonplaceholder.typicode.com/users/"
    response_user = get(user_url)

    list_user = response_user.json()
    all_data = {}

    for i in list_user:
        temp_data = []
        user_id = i.get('id')
        todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos/"\
            .format(str(user_id))
        response_todo = get(todo_url)
        todo_data = response_todo.json()
        for j in todo_data:
            temp_dic = {}
            temp_dic["username"] = i.get('username')
            temp_dic["task"] = j.get('title')
            temp_dic['completed'] = j.get('completed')
            temp_data.append(temp_dic)
        all_data[str(user_id)] = temp_data

    with open(file_name, mode="w") as fd:
        fd.write(dumps(all_data))
