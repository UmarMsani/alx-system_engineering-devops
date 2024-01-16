#!/usr/bin/python3
"""Function to query a list of all hot posts on given Reddit subreddit"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    Queries the Reddit API and returns all hot posts of the subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles.
        count (int): The count of posts.
        after (str): The Reddit API parameter for pagination.

    Returns:
        list or None: A list containing the titles of hot articles
        or None if no results are found.
    """
    import requests

    # Make a request to the Reddit API
    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"count": count, "after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)

    # Check if the request was successful (status code less than 400)
    if sub_info.status_code >= 400:
        return None

    # Extract information from the JSON response
    hot_l = hot_list + [child.get("data").get("title")
                        for child in sub_info.json()
                        .get("data")
                        .get("children")]

    info = sub_info.json()

    # Check if there are more pages (after is not None)
    if not info.get("data").get("after"):
        return hot_l

    # Recursive call to fetch the next page
    return recurse(subreddit, hot_l, info.get("data").get("count"),
                   info.get("data").get("after"))
