#!/usr/bin/python3
"""Python script to export data in the JSON format."""
import csv
import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/' + user_id
    user_response = requests.get(user_url)
    username = user_response.json().get('username')

    task_url = user_url + '/todos'
    task_response = requests.get(task_url)
    tasks = task_response.json()

    data = {user_id: []}
    for task in tasks:
        completed_status = task.get('completed')
        task_title = task.get('title')
        data[user_id].append({
            "task": task_title,
            "completed": completed_status,
            "username": username
        })

    with open('{}.json'.format(user_id), 'w') as file:
        json.dump(data, file)
