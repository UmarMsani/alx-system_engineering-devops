#!/usr/bin/python3

"""
This script retrieves information about an employee's TODO list progress using a REST API.
"""

import sys
import requests

def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays the employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            todo_data = response.json()

            # Filter completed tasks
            completed_tasks = [task for task in todo_data if task.get('completed')]
            num_completed_tasks = len(completed_tasks)
            total_tasks = len(todo_data)

            # Get employee name
            employee_name = todo_data[0].get('name')

            print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")

            # Display completed tasks
            for task in completed_tasks:
                print(f"\t{task.get('title')}")

        else:
            print("Failed to fetch TODO list")

    except requests.RequestException as e:
        print(f"Request Exception: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
