#!/usr/bin/python3
"""Write a Python script that, using REST API
returns the csv presentation
"""
import csv
import requests
import sys


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com"
    emp_id = sys.argv[1]

    res = requests.get("{}/users/{}/todos".format(api_url, emp_id),
                       params={"_expand": "user"})
    data = res.json()
    employee_name = data[0]["user"]["username"]
    with open("{}.csv".format(emp_id), "w", newline="") as csvfile:
        spamwriter = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        for task in data:
            spamwriter.writerow([emp_id,
                                 employee_name,
                                 str(task["completed"]), task["title"]])
