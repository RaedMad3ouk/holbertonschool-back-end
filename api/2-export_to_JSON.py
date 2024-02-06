#!/usr/bin/python3
"""Write a Python script that, using REST API
and render json file """
import json
import requests
import sys


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com"
    emp_id = sys.argv[1]

    res = requests.get("{}/users/{}/todos".format(api_url, emp_id),
                       params={"_expand": "user"})
    data = res.json()
    employee_name = data[0]["user"]["username"]
    emp_tasks = {emp_id: []}

    for task in data:
        task_dic = {"task": task["title"], "completed": task["completed"],
                    "username": employee_name}
        emp_tasks[emp_id].append(task_dic)

    with open("{}.json".format(emp_id), "w")as jsfile:
        json.dump(emp_tasks, jsfile)
