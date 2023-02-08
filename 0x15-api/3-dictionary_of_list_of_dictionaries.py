#!/usr/bin/python3
"""
This script exports all users tasks using {JSON} Placeholder REST API
into a JSON file
"""


def user_tasks(user, tasks):
    """
    Returns dictionary of all tasks' info about a user
    """
    pass


def main():
    """
    Gather all tasks of of all employees in JSON format
    using a REST API
    """
    import requests
    import sys

    users = requests.get('https://jsonplaceholder.typicode.com/users/')
    content = {}

    for user in users.json():
        todos = requests.get('https://jsonplaceholder.typicode.com/todos' +
                             '?userId={}'.format(user.get('id')))
        content[str(user.get('id'))] = [user_tasks(user, todos.json())]


if __name__ == '__main__':
    main()
