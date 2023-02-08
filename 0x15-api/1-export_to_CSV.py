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
    import csv
    import requests
    import sys

    user_id = int(sys.argv[1])
    user = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        '{}'.format(user_id))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos' +
                         '?userId={}'.format(user_id))

    with open(f"{user_id}.csv", 'w', encoding='UTF8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        row = [user_id, user.json().get("username")]
        for task in todos.json():
            row.append(task.get("completed"))
            row.append(task.get("title"))
            writer.writerow(row)
            row.pop()
            row.pop()


if __name__ == '__main__':
    """ execute if not imported """
    main()
