#!/usr/bin/python3
"""
Module defining recurse function

"""
import requests

BASE_URL = 'https://www.reddit.com/'
HEADERS = {'User-Agent': 'My-Custom-one'}


def recurse(subreddit, hot_list=[], after=""):
    """Queries the Reddit API and returns a list containing
        the titles of all hot articles for a given subreddit"""
    headers = requests.utils.default_headers()
    headers.update(HEADERS)
    params = {'after': after}
    response = requests.get("{}r/{}/hot.json".format(BASE_URL, subreddit),
                            headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code // 100 != 2:
        return None
    data = response.json().get('data').get('children')
    for post in data:
        hot_list.append(post.get('data').get('title'))
    after = response.json().get('data').get('after')
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
