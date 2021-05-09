#!/usr/bin/python3
"""
Return the list of all hot posts of a subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after="done"):
    """
        thi is a recursive function 
        returns all hot posts 
    """
    # seeting user agent
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    # alter url with the new value of after
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after != "done":
        url = url + "?after={}".format(after)
    response = requests.get(url, headers=headers, allow_redirects=False)

    # adding the newly added top posts 
    sub_titles = response.json().get('data', {}).get('children', [])
    if not sub_titles:
        return None
    else:
        for i in sub_titles:
            hot_list.append(i.get('data').get('title'))

    # new value after
    after = response.json().get('data').get('after')
    if not after:
        return hot_list
    return (recurse(subreddit, hot_list, after))
