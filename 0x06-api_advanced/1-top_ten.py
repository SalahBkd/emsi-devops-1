#!/usr/bin/python3
"""
Using Reddit API to get the top hot posts of a subreddit
"""
import requests


def top_ten(subreddit):
    """
        function prints the top hot posts of a subreddit
        and returns None if the subreddit is not valid
    """
    # setting user agent
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers=headers).json()
    sub_titles = response.get('data', {}).get('children', [])
    if not sub_titles:
        print(None)
    for t in sub_titles:
        print(t.get('data').get('title'))
