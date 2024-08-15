#!/usr/bin/python3
"""
Module defining count function

"""
import requests

BASE_URL = 'https://www.reddit.com/'
HEADERS = {'User-Agent': 'My-Custom-one'}


def count_words(subreddit, word_list, hot_list=[], after=""):
    """Queries the Reddit API and returns the number of times a word appears
                in the titles of all hot articles for a given subreddit"""
    headers = requests.utils.default_headers()
    headers.update(HEADERS)
    params = {'after': after, 'limit': 100}
    response = requests.get("{}r/{}/hot.json".format(BASE_URL, subreddit),
                            headers=headers, params=params,
                            allow_redirects=False)
    json = None
    try:
        if response.status_code // 100 != 2:
            raise Exception
        json = response.json()
    except Exception:
        print("")
        return
    posts = json.get('data').get('children')
    after = json.get('data').get('after')
    for post in posts:
        hot_list.append(post.get('data').get('title').lower())
    if after is not None:
        return count_words(subreddit, word_list, hot_list, after)
    word_count = {}
    word_list = list(set([word.lower() for word in word_list]))
    for word in word_list:
        word_count[word] = 0
    for title in hot_list:
        for word in word_list:
            word_count[word] += title.split(" ").count(word)
    for word, count in sorted(word_count.items(), key=lambda x: x[1],
                              reverse=True):
        if count:
            print("{}: {}".format(word, count))
    return hot_list
