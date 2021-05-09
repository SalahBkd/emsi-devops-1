#!/usr/bin/python3
"""
return the list of all hot posts of a subreddit
"""
import requests 



def recurse(subreddit, hot_list=[], after="done"):
    """
    the recurse function is recursive function that returs the title of all hot posts in subreddit 
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after != "done":
        url = url + "?after={}".format(after)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent':'me'})
    response = requests.get(url, headers=headers, allow_redirects=False)
    sub_titles=response.json().get('data', {}).get('children', [])
    if not sub_titles:
        return None
    else :
        # adding all the current fetched titles
        for i in sub_titles:
            hot_list.append(i.get('data').get('title'))
    after = response.json().get('data').get('after')
    if not after:
        return hot_list
    return recurse(subreddit,hot_list,after)
