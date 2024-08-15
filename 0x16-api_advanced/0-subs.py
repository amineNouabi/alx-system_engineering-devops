#!/usr/bin/python3
"""
Module defining number_of_subscribers function

"""
import requests

BASE_URL = 'https://www.reddit.com/'


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""

    response = requests.get("{}r/{}/about.json".format(BASE_URL,
                            subreddit), allow_redirects=False)
    if response.status_code == 404:
        return 0
    return response.json().get('data').get('subscribers')
