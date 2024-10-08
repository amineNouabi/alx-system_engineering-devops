#!/usr/bin/python3
"""Gather data from an API and export to CSV"""

import csv
from requests import api
from sys import argv


if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com"
    USER_ID = int(argv[1])
    todos = api.get("{}/todos?userId={}".format(API_URL, USER_ID)).json()
    employee = api.get("{}/users/{}".format(API_URL, USER_ID)).json()

    username = employee.get("username")

    with open("{}.csv".format(USER_ID), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([USER_ID, username, todo.get("completed"),
                             todo.get("title")])
