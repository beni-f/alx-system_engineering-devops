#!/usr/bin/python3

"""
0-subs.py
"""

import requests


def number_of_subscribers(subreddit):
    """
       Returns the number of subscribers for a given reddit
    """
    try:
        url = f'https://api.reddit.com/r/{subreddit}/about'
        headers = {'User-Agent': 'MyBot/0.1'}
        resp = requests.get(url, headers=headers)
        data = resp.json()
        return data['data'].get('subscribers')
    except:
        return 0
