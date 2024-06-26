#!/usr/bin/python3
"""
api reddit
"""
import requests


def recurse(subreddit, after=None):
    """mbc2"""
    headers = {"User-Agent": "haruma/1.0"}
    params = {"after": after}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, allow_redirects=False,
                            headers=headers, params=params)
    all_posts = []
    if response.status_code == 200:
        data = response.json()
        after = data["data"]["after"]
        if after is None:
            return all_posts
        for post in data["data"]["children"]:
            all_posts.append(post["data"]["title"])
        nnext = recurse(subreddit, after)
        all_posts.extend(nnext)
        return all_posts
    return None
