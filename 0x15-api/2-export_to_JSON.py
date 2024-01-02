#!/usr/bin/python3
"""
This script retrieves information about an employee's
TODO list progress using a REST API and exports it to a JSON file.
"""
import json
import requests
import sys

if __name__ == "__main__":
    """Get user ID from command line arguments"""
    user_id = sys.argv[1]
    """URL for API"""
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    """Write data to JSON file"""
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
