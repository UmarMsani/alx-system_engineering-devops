#!/usr/bin/python3
"""
Importing the 'get' function from the 'requests'
module for making HTTP requests.
"""
from requests import get


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If not a valid subreddit, return 0.
    """
    # Check if the subreddit is None or not a string, return 0
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    # Define the User-Agent and URL for the Reddit API request
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    # Make a GET request to the Reddit API
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        # Extract the number of subscribers from the JSON response
        return results.get('data').get('subscribers')

    except Exception:
        # Handle any exceptions and return 0 if an error occurs
        return 0
