#!/usr/bin/python3
"""
api reddit
"""
import requests


def top_ten(subreddit):
    """ matchia 3icha"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    header = {"User-Agent": "haruma/v1"}
    response = requests.get(url, allow_redirects=False, headers=header)

    if response.status_code == 200:
        data = response.json()
        dictionary = data['data']['children']
        for i in dictionary:
            print(i['data']['title'])
    else:
        print("None")
