#!/usr/bin/python3
"""
    2-recurse.py
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    url = "https://api.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    if after:
        url += "?after={}".format(after)

    
    response = requests.get(url, headers=headers)
    data = response.json()
    if response.status_code == 200:
        if "error" in data:
            return None
        children = data['data']['children']
        for child in children:
            hot_list.append(child['data']['title'])
        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
