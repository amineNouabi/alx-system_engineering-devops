#!/usr/bin/python3
"""Gather data from an API"""

from json import dump
from requests import api
from sys import argv


if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com"
    todos = api.get("{}/todos".format(API_URL)).json()
    users = api.get("{}/users".format(API_URL)).json()

    with open("todo_all_employees.json", "w") as jsonfile:
        to_write = {}
        for user in users:
            USER_ID = user.get("id")
            USERNAME = user.get("username")
            to_write[USER_ID] = [{"username": USERNAME,
                                  "task": todo.get("title"),
                                  "completed": todo.get("completed")}
                                 for todo in todos
                                 if todo.get("userId") == USER_ID]
        dump(to_write, jsonfile)
