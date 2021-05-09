#!/usr/bin/python3
"""
Getting number of subscribers for a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
        function returns number of subscribers
        and returns 0 for invalid subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # setting user agent
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    response = requests.get(url, headers=headers).json()
    subs = response.get('data', {}).get('subscribers')
    if not subs:
        return 0
    return subs
