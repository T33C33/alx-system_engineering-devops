#!/usr/bin/python3
'''
gather employee data from API
'''
import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Make a GET request to retrieve the employee's information
    response = requests.get(f"{REST_API}/users/{employee_id}")
    employee = response.json()

    # Make a GET request to retrieve the employee's TODO list
    response = requests.get(f"{REST_API}/todos?userId={employee_id}")
    todos = response.json()

    # Count the number of completed tasks
    completed_tasks = [todo for todo in todos if todo.get('completed')]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos)

    # Display the employee TODO list progress
    print(f"Employee {employee['name']} is done with tasks ({number_of_done_tasks}/{total_number_of_tasks}):")
    for todo in completed_tasks:
        print(f"\t{todo['title']}")
