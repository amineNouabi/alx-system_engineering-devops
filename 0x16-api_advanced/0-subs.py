#!/usr/bin/python3
"""
Module defining number_of_subscribers function

"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')
