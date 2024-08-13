#!/usr/bin/python3
"""
Function to print the titles of the first 10 hot posts for a given subreddit
"""
import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.
    """
    # Reddit API URL
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Custom User-Agent to avoid too many requests error
    headers = {
        "User-Agent": "linux:my_reddit_client:v1.0 (by /u/your_username)"
    }

    # Parameters to get only the first 10 posts
    params = {
        "limit": 10
    }

    try:
        # Make the request
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        # Check if the subreddit is valid
        if response.status_code == 404:
            print("None")
            return
        
        # Raise an exception for any other error
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Print the titles of the first 10 hot posts
        for post in data["data"]["children"]:
            print(post["data"]["title"])

    except requests.RequestException:
        print("None")