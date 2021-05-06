#!/usr/bin/python3
"""
0-subs : using reddit api to get number of subs for a specific subreddit
"""
import requests
def number_of_subscribers(subreddit):
	url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
	headers = requests.utils.default_headers()
	headers.update({'User-Agent': 'me'})
	response = requests.get(url, headers=headers).json()
	subs = response.get('data', {}).get('subscribers')
	if subs : 
		return subs 
	return 0  
