#!/usr/bin/python3
import requests
def number_of_subscribers(subreddit):
	url = f"https://www.reddit.com/r/{subreddit}/about.json"
	headers = requests.utils.default_headers()
	headers.update({'User-Agent': 'me'})
	response = requests.get(url, headers=headers).json()
	subs = response.get('data', {}).get('subscribers')
	if subs : 
		return subs   
	else :
		return 0
