#!/usr/bin/python3
''' grtting subscribers '''

import requests


def number_of_subscribers(subreddit):
    '''a function that queries reddit api and returns subscribers '''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My Agent'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

    return 0
