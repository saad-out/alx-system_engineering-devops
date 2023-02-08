#!/usr/bin/python3
"""
This script displays user's TODO list using {JSON} Placeholder REST API
"""


def export_csv(user, tasks):
    """
    Export TODO list into csv file
    """
    pass


def main():
    """
    Returns information about TODO list progress of given employee ID
    using a REST API
    """
    import csv
    import requests
    import sys

    user_id = int(sys.argv[1])
    user = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        '{}'.format(user_id))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos' +
                         '?userId={}'.format(user_id))

    export_csv(user.json(), todos.json())


if __name__ == '__main__':
    main()
