#!/usr/bin/python3
"""
Query Reddit API for number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """ 
    function to get the number of subs
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})
    
    # getting response
    response = requests.get(url, headers=headers, allow_redirects=False).json()
    subs = response.get('data', {}).get('subscribers')
    if not subs:
        return 0
    return subs
