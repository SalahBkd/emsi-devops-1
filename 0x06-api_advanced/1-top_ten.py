#!/usr/bin/python3
import requests
import sys 
headers = {
    'authority': 'www.reddit.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'csv=1; edgebucket=N9VcU6IMPpQPQ1aBhZ; G_ENABLED_IDPS=google; reddit_session=313722963695%2C2021-04-30T09%3A56%3A32%2Cbb70f2ae81f2c313b2cdbc60f7b4d0586eb9d4bb; loid=0000000000404ejw1b.2.1561371399000.Z0FBQUFBQmdpOVJRNTV4YU5VWmVvLVJqRERFSUlBOF94OWRpUGkwSHN2bENndXB3NGVWaXBTWGlsSE1QcEFrbi1HaTZBRTZJZl93Z29iS2xfSzh5eDZVYmNmeE9JN0JSdG9OX1ZteTFYdHNDY0xoNUlQUGJjUXNfMDZPSG5GdUhrbDl3WlY2MVBCR2M; pc=zr; __aaxsc=1; token_v2=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MjAyODYxNTgsInN1YiI6IjMxMzcyMjk2MzY5NS1WVFQzcmdGdFNkaEZ6R1NQVktDUVdxWWsxVWMiLCJsb2dnZWRJbiI6dHJ1ZSwic2NvcGVzIjpbIioiLCJlbWFpbCIsInBpaSJdfQ.9zJfcFjw_sY7CDGgv8VzVV0jo9irVWcE_DRIRjdrT5I; session_tracker=chfjqjojhbgbraelfd.0.1620283520211.Z0FBQUFBQmdrNUNBZHotZlJQSlFKWGdadmMtbjlQakNtTVlieWxkR2xJLTRkSWd0ZlFyMFo1cW5DZWk4UmVEeVZ2dzI0dW1YTVUxY2VpbXBtNDhOOXQzUTUtUWVkSmE0OC00WG9wQjJ1VkpMSEQ5LTJjTEZCUnV2Vk9xMVBjRU1FaFZ6VnZya2NhaW8; aasd=3%7C1620282676438; recent_srs=t5_2s3qj%2Ct5_hds7r%2Ct5_2sdpm%2C',
}
def number_of_subscribers(subreddit):
	response = requests.get(f'https://www.reddit.com/r/{subreddit}/.json', headers=headers)
	response_json=response.json()
	if response :    
		return [item['data']['subreddit_subscribers'] for item in response_json['data']['children'][:1]][0]
	else :
		return 0
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Please pass an argument for the subreddit to search.")
	else:
		print("{:d}".format(number_of_subscribers(sys.argv[1])))
