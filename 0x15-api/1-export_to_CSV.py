#!/usr/bin/python3
"""
This script displays user's TODO list using {JSON} Placeholder REST API
"""


def export_csv(user, tasks):
    """
    Export TODO list into csv file
    """
    import csv

    file_name = "{}.csv".format(user.get('id'))
    with open(file_name, 'w', encoding='UTF8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks:
            row = [user.get('id'), user.get('username'),
                   task.get('completed'), task.get('title')]
            writer.writerow(row)


def main():
    """
    Returns information about TODO list progress of given employee ID
    using a REST API
    """
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
