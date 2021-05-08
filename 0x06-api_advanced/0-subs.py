#!/usr/bin/python3
"""
0-subs : using reddit api to get number of subs for a specific subreddit
"""
import requests
def number_of_subscribers(subreddit):
    """ function to get the number of subs"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'me'})
    # getting response 
    response = requests.get(url, headers=headers,allow_redirects=False).json()
    subs = response.get('data', {}).get('subscribers')
    if not subs : 
        return 0 
    return subs
 
