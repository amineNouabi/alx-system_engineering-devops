#!/usr/bin/python3
"""
Module defining number_of_subscribers function

"""
from requests import get

BASE_URL = 'https://www.reddit.com/'
HEADERS = {'User-Agent': 'Mozilla/5.0'}


def top_ten(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""

    response = get("{}r/{}/hot.json?limit=10".format(BASE_URL, subreddit),
                   headers=HEADERS, allow_redirects=False)
    if int(response.status_code) / 100 != 2:
        print(None)
        return
    data = response.json().get('data').get('children')
    for post in data:
        print(post.get('data').get('title'))
