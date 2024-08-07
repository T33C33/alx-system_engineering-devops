#!/usr/bin/python3
'''
Employee data from API
'''
import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            employee_id = int(sys.argv[1])
            employee_info = requests.get(
                '{}/users/{}'.format(REST_API, employee_id)).json()
            tasks_info = requests.get('{}/todos'.format(REST_API)).json()
            employee_name = employee_info.get('name')
            tasks = list(filter(lambda x: x.get('userId') == employee_id,
                                tasks_info))
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    employee_name,
                    len(completed_tasks),
                    len(tasks)
                )
            )
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print('\t {}'.format(task.get('title')))
