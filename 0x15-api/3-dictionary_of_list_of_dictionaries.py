#!/usr/bin/python3
"""
This script displays user's tasks using {JSON} Placeholder REST API
"""


def user_tasks(user, tasks):
    """
    Export TODO list into JSON file
    """
    pass


def main():
    """
    Gather all tasks of an employee based on ID in JSON format
    using a REST API
    """
    import requests
    import sys

    user_id = int(sys.argv[1])
    user = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        '{}'.format(user_id))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos' +
                         '?userId={}'.format(user_id))


if __name__ == '__main__':
    main()
