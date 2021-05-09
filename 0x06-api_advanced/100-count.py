#!/usr/bin/python3
import requests 
"""
return the list of all hot posts of a subreddit & counts reps
"""


def count_words(subreddit, word_list,after="done", count={}):
    """
       recursive function that returs the title
       counts
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    # turning the string into list
    
    if after != "done":
        url = url + "?after={}".format(after)
    #if not count:
    string=word_list.split(' ')
    if not count:
        for word in string:
            count[word]=0
    headers = requests.utils.default_headers()
    headers.update({'User-Agent':'me'})
    response = requests.get(url, headers=headers, allow_redirects=False)
    sub_titles=response.json().get('data', {}).get('children', [])
    
    if not sub_titles:
        return None
    else :
        # adding all the current fetched titles
        for i in sub_titles:
            for word in count.keys():
                new=i.get('data').get('title')
                count[word]+=new.count(word)
            if new.count(word)!=0:
                print ('===>',new.count(word))
    after = response.json().get('data').get('after')
    if not after:
        print(count)
        for word, value in count.items():
            print('{}:{}'.format(word,value))
        return
    else:
        return count_words(subreddit,word_list,after,count)
