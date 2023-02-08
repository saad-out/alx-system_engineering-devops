#!/usr/bin/python3
"""Request employee ID from API
"""
import csv
import requests
import sys

if __name__ == '__main__':
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
