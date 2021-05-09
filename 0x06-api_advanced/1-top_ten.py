#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """
    printing the top hot posts of a subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'me'})
    response = requests.get(url, headers=headers, allow_redirects=False).json()
    sub_titles = response.get('data', {}).get('children', [])
    # test if we got some info from the subreddit
    if not sub_titles:
        print(None)
    for i in sub_titles:
        print(i.get('data').get('title'))

