#!/usr/bin/python3

"""
1-top_ten.py
"""

import requests


def top_ten(subreddit):
    """
        Prints the titles of the first 10 hot posts for a given subreddit
    """
    try:
        url = f'https://api.reddit.com/r/{subreddit}/hot'
        headers = {'User-Agent': 'MyBot/0.1'}
        resp = requests.get(url, headers=headers)
        data = resp.json()
        children = data.get('data').get('children')
        for post in children[:10]:
            print(post.get('data').get('title'))
    except Exception:
        print(None)
