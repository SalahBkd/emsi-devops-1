#!/usr/bin/python3 
"""
1-top_ten

"""
import requests
def top_ten(subreddit):
    """
    printing the top hot posts of a subreddit.
    
    """
    url = "https://www.reddit.com/r/{}/top.json".format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent':'me'})
    response= requests.get(url,headers=headers,allow_redirects=False).json()
    if response['data']['dist']!=0 :    
        for i in range(10):
            print(response['data']['children'][i]['data']['title'])
    else:
        print('None')
	
