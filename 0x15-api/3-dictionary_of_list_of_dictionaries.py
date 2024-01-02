#!/usr/bin/python3
"""
This script retrieves information about employees'
TODO list progress using a REST API and exports it to a JSON file.
"""
import json
import requests

if __name__ == "__main__":
    """URL for API"""
    url = "https://jsonplaceholder.typicode.com/"
    """Get users ID from command line arguments"""
    users = requests.get(url + "users").json()

    """Create JSON data structure & Write data to JSON file"""
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
