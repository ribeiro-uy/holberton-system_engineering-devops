#!/usr/bin/python3
""" Project 0x16. API advanced: Task 0 """
import requests


def number_of_subscribers(subreddit):
    """ Function that queries the Reddit API
    and returns the number of subscribers """

    headers = {'User-Agent': 'SoyYo!'}
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        return res.json().get('data').get('subscribers')
    else:
        return 0
