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

    # Define User-Agent and parameters for the Reddit API request
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    # Make a GET request to the Reddit API
    response = get(url, headers=user_agent, params=params)
    fetch_data = response.json()

    try:
        # Extract information from the JSON response
        raw1 = fetch_data.get('data').get('children')

        # Print the titles of the first 10 hot posts
        for i in raw1:
            print(i.get('data').get('title'))

    except exceptions.RequestException as e:
        # Handle any exceptions and print "None" if an error occurs
        print("None")
