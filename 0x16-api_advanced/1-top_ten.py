#!/usr/bin/python3
"""
Module defining number_of_subscribers function

"""
import requests

BASE_URL = 'https://www.reddit.com/'
HEADERS = {'User-Agent': 'My-Custom-one'}


def top_ten(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""
    headers = requests.utils.default_headers()
    headers.update(HEADERS)
    response = requests.get("{}r/{}/hot.json?limit=9".format(BASE_URL,
                                                             subreddit),
                            headers=headers, allow_redirects=False)
    if response.status_code / 100 != 2:
        print(None)
        return
    data = response.json().get('data').get('children')
    for post in data:
        print(post.get('data').get('title'))
