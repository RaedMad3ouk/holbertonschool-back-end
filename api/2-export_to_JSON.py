#!/usr/bin/python3
"""Gathering the needed informations from the API."""
import json
import requests
from sys import argv

if __name__ == '__main__':
    resp_users = requests.get('https://jsonplaceholder.typicode.com/users')
    resp_todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    user_id = argv[1]

    json_dic = dict()
    json_list = list()
    small_dic = dict()
    for i in resp_users.json():
        if i['id'] == int(user_id):
            user_name = i['username']
    for i in resp_todos.json():
        if i['userId'] == int(user_id):
            small_dic = {}
            small_dic["task"] = i['title']
            small_dic["completed"] = i['completed']
            small_dic["username"] = user_name
            json_list.append(small_dic)
    json_dic[user_id] = json_list
    with open(f"{user_id}.json", 'w') as j_file:
        json.dump(json_dic, j_file)
