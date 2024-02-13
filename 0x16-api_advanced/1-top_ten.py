#!/usr/bin/python3
"""
    1-top_ten.py
"""
import requests


def top_ten(subreddit):
    """
        Print the titles of the first 10 hot posts listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Beni Fissha'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data').get('children')

        for i, post in enumerate(posts[:10]):
            print('{}'.format(post.get('data').get('title')))
    else:
        return 0
