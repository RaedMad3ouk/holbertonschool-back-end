#!/usr/bin/python3
"""Write a Python script that, using REST API
and export data in the JSON format. """
import json
import requests

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com"

    res1 = requests.get("{}/users".format(api_url))
    data1 = res1.json()
    emp_dic = {}

    for user in data1:
        res2 = requests.get("{}/users/{}/todos".format(api_url, user["id"]),
                            params={"_expand": "user"})
        data2 = res2.json()
        emp_dic[user["id"]] = []
        for task in data2:
            dic_task = {"username": user["username"], "task": task["title"],
                        "completed": task["completed"]}
            emp_dic[user["id"]].append(dic_task)

    with open("todo_all_employees.json", "w")as jsfile:
        json.dump(emp_dic, jsfile)
