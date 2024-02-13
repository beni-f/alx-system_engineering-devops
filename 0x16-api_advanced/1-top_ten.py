#!/usr/bin/python3
"""
    1-top_ten.py
"""
import requests
def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Beni Fissha'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for i, post in enumerate(posts[:10]):
            print('{}'.format(post['data']['title']))
    else:
        return 0
