#!/usr/bin/python3
"""Python script to export data in the JSON format"""
import json
import requests

if __name__ == '__main__':
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_resp = requests.get(users_url)
    users = users_resp.json()

    users_dict = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        user_todos_url = f"{users_url}/{user_id}/todos"
        todos_resp = requests.get(user_todos_url)

        tasks = todos_resp.json()
        users_dict[user_id] = []
        for task in tasks:
            task_completed = task.get('completed')
            task_title = task.get('title')
            users_dict[user_id].append({
                "task": task_title,
                "completed": task_completed,
                "username": username
            })

    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f)
