#!/usr/bin/python3
"""
return the list of all hot posts of a subreddit
"""
import requests
def recurse(subreddit, hot_list=[], count=0):
    """
    the recurse function is recursive function that returs the title of all hot posts in subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent':'me'})
    response= requests.get(url,headers=headers,allow_redirects=False).json()
    sub_titles=response.get('data', {}).get('children', [])
    if not sub_titles:
        return None
    if len(sub_titles)==count:
        return hot_list
    if not hot_list:
        hot_list.append(sub_titles[-1].get('data').get('title'))
        del sub_titles[-1]
        count +=1
        return recurse(subreddit,hot_list,count)
    else : 
        # to remove all the previous titles from sub_titles
        for i in range(count):
            del sub_titles[-1]
        hot_list.append(sub_titles[-1].get('data').get('title'))
        del sub_titles[-1]
        count +=1
        return recurse(subreddit,hot_list,count)
