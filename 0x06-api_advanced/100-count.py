#!/usr/bin/python3

"""
Task 2, all the hot post
"""
import requests


def count_words(subreddit, word_list, after=None, count={}):
    """
       print 100 top posts
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url, headers={"User-Agent": "oussama99"},
                        allow_redirects=False,
                        params={'after': after})
    if after is None:
        for word in word_list:
            count[word] = 0

    if response.status_code == 200:
        after = response.json()['data']['after']
        if after is None:
            for word, value in count.items():
                if value != 0:
                    print('{}: {}'.format(word, value))
            return

        for post in response.json()['data']['children']:
            for word in word_list:
                string = post['data']['title']
                string_split = string.lower().split(' ')
                count[word] += string_split.count(word.lower())
        return count_words(subreddit, word_list, after, count)
    else:
        return
