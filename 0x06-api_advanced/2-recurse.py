#!/usr/bin/python3

"""
Recursive function to get hot posts
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
        thi is a recursive function
        returns all hot posts
    """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url, headers={"User-Agent": "oussama9"},
                        allow_redirects=False,
                        params={'after': after})

    if response.status_code == 200:
        after = response.json()['data']['after']
        if after is None:
            return hot_list

        for post in response.json()['data']['children']:
            hot_list.append(post['data']['title'])
        return recurse(subreddit, hot_list, after)

    else:
        return None
