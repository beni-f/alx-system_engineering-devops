#!/usr/bin/python3
 
"""
2-recurse.py 
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
        returns a list containing the titles of all hot articles for a given subreddit
    """
    try:
        url = f'https://api.reddit.com/r/{subreddit}/hot'
        headers = {'User-Agent': 'MyBot/0.1'}
        params = {'limit': 100, 'after': after} if after else {'limit': 100}
        resp = requests.get(url, headers=headers, params=params)

        data = resp.json()
        children = data.get('data').get('children')

        for post in children:
            hot_list.append(post.get('data').get('title'))
        
        after = data.get('data').get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    except Exception:
        return None
    
import sys

if __name__ == '__main__':
    recurse = __import__('2-recurse').recurse
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")