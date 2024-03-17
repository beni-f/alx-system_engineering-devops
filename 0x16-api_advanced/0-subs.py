#!/usr/bin/python3
"""
    0-subs.py
"""
import requests


def number_of_subscribers(subreddit):
    """
        Returns the number of subscirbers in a given subreddit
    """
    url = "https://reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'MyBot/0.0.1'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subs = data['data']['subscribers']
        return subs
    elif response.status_code == 404:
        return 0
    else:
        return 0
