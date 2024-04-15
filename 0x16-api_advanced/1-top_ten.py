#!/usr/bin/python3

"""
Importing requests module.
"""

import requests
import platform

def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("Invalid subreddit")
        return

    user_agent = {'User-agent': f'MyRedditScript/{platform.version()} (by /u/benjelloo)'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    response = requests.get(url, headers=user_agent, params=params)
    # response.raise_for_status()  # Raise an exception for HTTP errors
    all_data = response.json()

    raw_data = all_data.get('data', {}).get('children', [])

    for item in raw_data:
        print(item.get('data', {}).get('title'))
