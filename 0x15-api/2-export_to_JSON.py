#!/usr/bin/python3
"""Gather data from an API"""

from json import dump
from requests import api
from sys import argv


if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com"
    USER_ID = int(argv[1])
    todos = api.get("{}/todos?userId={}".format(API_URL, USER_ID)).json()
    employee = api.get("{}/users/{}".format(API_URL, USER_ID)).json()

    username = employee.get("username")

    with open("{}.json".format(USER_ID), "w") as jsonfile:
        dump({USER_ID: [{"task": todo.get("title"),
                         "completed": todo.get("completed"),
                         "username": username} for todo in todos]}, jsonfile)
