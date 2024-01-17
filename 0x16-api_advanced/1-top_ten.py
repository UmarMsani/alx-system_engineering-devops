#!/usr/bin/python3
"""
Importing requests module for making HTTP requests.
"""
from requests import get


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """

     # Check if the subreddit is None or not a string
    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    # Define the URL and headers for the Reddit API request
    url = 'https://reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}

    # Make a GET request to the Reddit API
    response = get(url, headers=headers)
    results = response.json()

    try:
        # Extract information from the JSON response
        data = results.get('data').get('children')

        # Print the titles of the first 10 hot posts
        for datii in data:
            print(datii.get('data').get('title'))

    except Exception:
        # Handle any exceptions and print "None" if an error occurs
        print("None")
