#!/usr/bin/python3
"""
Module defining number_of_subscribers function

"""
import requests

BASE_URL = 'https://www.reddit.com/'
HEADERS = {'User-Agent': 'My Custom one'}


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""

    response = requests.get("{}r/{}/about.json".format(BASE_URL,
                            subreddit), headers=HEADERS, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return int(response.json().get('data').get('subscribers'))
