#!/usr/bin/python3
"""
This script retrieves information about an employee's
TODO list progress using a REST API.
"""
import sys
import urllib.request
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    with urllib.request.urlopen(url + "users/{}".format(sys.argv[1])) as response:
        user = json.loads(response.read().decode())
    with urllib.request.urlopen(url + "todos?userId={}".format(sys.argv[1])) as response:
        todos = json.loads(response.read().decode())
    completed = [task['title'] for task in todos if task['completed']]
    print(f"Employee {user['name']} is done with tasks({len(completed)}/{len(todos)}):")
    for task_title in completed:
        print(f"\t{task_title}")
