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
    headers.update({'User-Agent':'me'})
    response= requests.get(url,headers=headers,allow_redirects=False).json()
    sub_titles=response['data']['children'][i]['data']['title']
    if response['data']['dist']!=0 :    
        for i in sub_titles:
            print(i)
    else:
        print('None')
	
