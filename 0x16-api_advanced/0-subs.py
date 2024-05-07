#!/usr/bin/python3
""" querying from reddit api"""
from requests import get


def number_of_subscribers(subreddit):
    """ send get request and return
    the number of subscribers """
    url = f"https://www.reddit.com/r/{subreddit}/top.json?limit=1"
    response = get(url)
    if response.status_code != 200:
        return (0)
    r = response.json()
    return (r['data']['children'][0]['data']['subreddit_subscribers'])
