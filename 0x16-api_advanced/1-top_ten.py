#!/usr/bin/python3
""" Project 0x16. API advanced: Task 1 """
import requests


def top_ten(subreddit):
    """ Function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit."""

    headers = {'User-Agent': 'SoyYo!'}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10"
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        for element in res.json().get('data').get('children'):
            print(element.get('data').get('title'))
    else:
        return print(None)
