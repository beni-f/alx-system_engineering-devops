#!/usr/bin/python3
"""
    0-subs.py
"""
import requests
def number_of_subscribers(subreddit):
    """
        Return the number of subscribers for a given subreddit
    """
    url = "https://reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Beni Fissha'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subs = data.get('data').get('subscribers')
        return subs
    return 0

