#!/usr/bin/python3
"""Gather data from an API"""

from requests import api
from sys import argv


if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com"
    USER_ID = int(argv[1])
    todos = api.get("{}/todos?userId={}".format(API_URL, USER_ID)).json()
    employee = api.get("{}/users/{}".format(API_URL, USER_ID)).json()

    name = employee.get("title")
    completed_count = 0
    total_count = len(todos)

    for todo in todos:
        if todo.get("completed"):
            completed_count += 1

    print("Employee {} is done with ({}/{}):".format(name,
          completed_count, total_count))
    for todo in todos:
        if todo.get("completed"):
            print("\t {}".format(todo.get("title")))
