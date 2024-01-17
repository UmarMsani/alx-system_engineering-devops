#!/usr/bin/python3

"""
Importing the 'get' function from 'requests' module for making HTTP requests.
"""

from requests import get


def count_words(subreddit, word_list=[], after=None, cleaned_dict=None):
    """
    Function that queries the Reddit API, parses title of all hot articles,
    and prints sorted count of given keywords (case-insensitive, delimited by
    spaces. Javascript should count as javascript, but java should not).
    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count in post titles.
        after (str): The parameter for the next page of the API results.
        cleaned_dict (dict): A dictionary to store the count of keywords.

    Returns:
        None
    """

    # Convert word_list to lowercase and remove duplicates
    temp = [i.casefold() for i in word_list]
    cleaned_word_list = list(dict.fromkeys(temp))

    # Initialize cleaned_dict if not provided
    if cleaned_dict is None:
        cleaned_dict = dict.fromkeys(cleaned_word_list)

    params = {'show': 'all'}

    # Check if the subreddit is None or not a string, return None
    if subreddit is None or not isinstance(subreddit, str):
        return None

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}

    # Define the URL for the Reddit API request
    url = 'https://www.reddit.com/r/{}/hot/.json?after={}'.format(subreddit,
                                                                  after)

    # Make a GET request to the Reddit API
    response = get(url, headers=user_agent, params=params)

    # Check if the request was successful (status code 200)
    if (response.status_code != 200):
        return None

    # Parse the JSON response
    all_data = response.json()
    raw1 = all_data.get('data').get('children')
    after = all_data.get('data').get('after')

    # If there is no 'after', print the sorted count and return
    if after is None:
        new = {k: v for k, v in cleaned_dict.items() if v is not None}
        for k in sorted(new.items(), key=lambda x: (-x[1], x[0])):
            print("{}: {}".format(k[0], k[1]))
        return None

    # Loop through the posts and count occurrences of keywords in the title
    for i in raw1:
        title = i.get('data').get('title')
        split_title = title.split()
        split_title2 = [i.casefold() for i in split_title]

        for j in split_title2:
            if j in cleaned_dict and cleaned_dict[j] is None:
                cleaned_dict[j] = 1
            elif j in cleaned_dict and cleaned_dict[j] is not None:
                cleaned_dict[j] += 1

    # Recursively call count_words for the next page
    count_words(subreddit, word_list, after, cleaned_dict)
