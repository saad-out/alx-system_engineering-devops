#!/usr/bin/python3
"""
This script exports data gathered from {JSON} placeholder REST API
in CSV format
"""


def main():
    """
    Returns all tasks owned by an employee based on ID in CSV format
    using a REST API
    """
    import requests
    import sys

    user_id = int(sys.argv[1])
    user = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        '{}'.format(user_id))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos' +
                         '?userId={}'.format(user_id))

    for task in todos.json():
        print('"{}","{}","{}","{}"'.format(user_id,
                                           user.json().get('username'),
                                           task.get('completed'),
                                           task.get('title')))


if __name__ == '__main__':
    main()
