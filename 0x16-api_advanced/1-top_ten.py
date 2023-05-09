#!/usr/bin/python3
'''retuens top hot 10 topics '''

import requests


def top_ten(subreddit):
    '''a function that queries the Reddit API and prints the titles of the
        first 10 hot posts listed for a given subreddit.
    '''
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'My Agent'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        results = response.json()

        for result in results['data']['children']:
            print(result['data']['title'])
    else:
        print(None)
