#!/usr/bin/python3
""" querying from reddit api"""
from requests import get


def number_of_subscribers(subreddit):
    """ send get request and return
    the number of subscribers """
    if type(subreddit) not str:
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {'User-Agent': 'haruma'}
    response = get(url, header)
    if response.status_code == 200:
        r = response.json()
        return (response['data']['subscribers'])
    return (0)
