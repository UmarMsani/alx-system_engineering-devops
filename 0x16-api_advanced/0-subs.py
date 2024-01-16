#!/usr/bin/python3
"""
Importing the 'get' function from the 'requests'
module for making HTTP requests.
"""

from requests import get, exceptions


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If not a valid subreddit, return 0.
    """
    # Check if the subreddit is None or not a string, return 0
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    # Identifying the user agent
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}

    # Identify the URL
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    # Make the request
    response = get(url, headers=user_agent)

    # Convert the response into JSON format
    json_response = response.json()

    # Try to get the number of subscribers
    try:
        return json_response.get('data').get('subscribers')
    # If you couldn't get it, return 0
    except exceptions.RequestException as e:
        return 0
