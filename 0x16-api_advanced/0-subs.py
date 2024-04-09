#!/usr/bin/python3
import requests
"""
0-subs.py
"""


def number_of_subscribers(subreddit):
    """
       Returns the number of subscribers for a given reddit
    """
    url = f'https://api.reddit.com/r/{subreddit}/about'
    headers = {'User-Agent': 'MyBot/0.1'}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        return data['data'].get('subscribers', 0)
    return 0
