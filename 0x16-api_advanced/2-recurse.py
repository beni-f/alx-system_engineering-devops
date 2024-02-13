#!/usr/bin/python3
"""
    2-recurse.py
"""

import requests
import sys

def get_hot_articles(subreddit, after=None):
    """Helper function to fetch hot articles for a subreddit."""
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
        titles = [child['data']['title'] for child in children]
        after = data['data']['after']
        if after:
            titles += get_hot_articles(subreddit, after)
        return titles

def recurse(subreddit, hot_list=[]):
    """Recursively fetch hot articles for a subreddit."""
    if get_hot_articles(subreddit):
        hot_list += get_hot_articles(subreddit)
        return hot_list
    return None
if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
else:
    result = recurse(sys.argv[1])
    if result is not None:
        print(len(result))
    else:
        print("None")


