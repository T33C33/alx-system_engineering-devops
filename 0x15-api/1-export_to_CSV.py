#!/usr/bin/python3
"""Export data in the CSV format"""
import csv
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user_id
    response = requests.get(url_user)
    user_name = response.json().get('username')
    task_url = url_user + '/todos'
    response = requests.get(task_url)
    tasks = response.json()

    with open('{}.csv'.format(user_id), 'w') as csvfile:
        for task in tasks:
            completed = task.get('completed')
            title = task.get('title')
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user_id, user_name, completed, title))
