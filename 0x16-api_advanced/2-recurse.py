#!/usr/bin/python3
'''using recursion to query an API'''

import requests


def recurse(subreddit, hot_list=[]):
    '''Returns a list titles of all hot articles for a given subreddit'''
    url = "https://www.reddit.com/r/{}/hot.json?limit=50".format(subreddit)
    headers = {'User-Agent': 'My Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        results = response.json()

        for result in results['data']['children']:
            hot_list.append(result['data']['title'])

            if results['data']['after'] is not None:
                recurse(subreddit, hot_list=hot_list)
            return hot_list
    else:
        return None
