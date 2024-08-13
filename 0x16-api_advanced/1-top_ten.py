#!/usr/bin/python3

"""
the titles of the first 10
"""

import requests

def top_ten(subreddit):
    """
    function that queries the Reddit API
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    # Reddit API now requires a more specific User-Agent
    user_agent = {'User-agent': 'MyBot/0.0.1'}
    params = {'limit': 10}
    
    # Updated URL to use the OAuth endpoint
    url = f'https://oauth.reddit.com/r/{subreddit}/hot'

    # You need to replace 'YOUR_ACCESS_TOKEN' with a valid OAuth token
    headers = {
        **user_agent,
        'Authorization': 'bearer YOUR_ACCESS_TOKEN'
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()

        for post in data.get('data', {}).get('children', []):
            print(post.get('data', {}).get('title'))

    except Exception:
        print("None")