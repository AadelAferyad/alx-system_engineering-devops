#!/usr/bin/python3
""" querying from reddit api"""
import requests


def number_of_subscribers(subreddit):
    """ send get request and return
    the number of subscribers """
    if not subreddit or not isinstance(subreddit, str):
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {'User-Agent': 'haruma'}
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        r = response.json()
        return (r['data']['subscribers'])
    return (0)
