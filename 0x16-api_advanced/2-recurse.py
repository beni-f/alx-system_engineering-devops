#!/usr/bin/python3

"""
    Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """Querying Reddit API, and returns all
    hot articles for a given subreddit."""

    url = "https://api.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    if after:
        url += "?after={}".format(after)

    resp = requests.get(url, headers=headers)
    data = resp.json()

    if resp.status_code == 200:
        if "error" in data:
            return None
        children = data['data']['children']
        for child in children:
            hot_list.append(child['data']['title'])
        after = data['data']['after']
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
