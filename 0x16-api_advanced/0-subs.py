#!/usr/bin/python3
"""
Module defining number_of_subscribers function
"""

import requests

BASE_URL = 'https://www.reddit.com/'
HEADERS = {'User-Agent': 'My-Custom-one'}


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""
    headers = requests.utils.default_headers()
    headers.update(HEADERS)
    response = requests.get("{}r/{}/about.json".format(BASE_URL,
                            subreddit), headers=headers, allow_redirects=False)
    if response.status_code // 100 != 2:
        return 0
    try:
        count = response.json().get('data').get('subscribers')
        if not count:
            return 0
        return count
    except Exception:
        return 0
