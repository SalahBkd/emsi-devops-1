#!/usr/bin/python3
"""
Getting the top 10 hot posts of a subreddit
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
    response = requests.get(url, headers=headers, allow_redirects=False).json()
    sub_titles = response.get('data', {}).get('children', [])
    if not sub_titles:
        print(None)
    for i in sub_titles:
        print(i.get('data').get('title'))
