#!/usr/bin/python3
"""
This script retrieves information about an employee's
TODO list progress using a REST API and exports it to a CSV file.
"""
import csv
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

    """Write data to CSV file"""
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
