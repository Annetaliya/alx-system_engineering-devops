#!/usr/bin/python3
''' extend your Python script to export data in json format '''

import csv
import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/" + user_id
    json_dict = requests.get(url).json()
    name_of = json_dict.get("username")
    user_task = requests.get("{}/todos".format(url))
    user_task = user_task.json()
    file_name = user_id + '.json'
    new_dict = {}
    new_dict[user_id] = []

    for items in user_task:
        second_dict = {}
        second_dict['task'] = items.get('title')
        second_dict['completed'] = items.get('completed')
        second_dict['username'] = name_of
        new_dict.get(user_id).append(second_dict)

    with open(file_name, 'w') as f:
        json.dump(new_dict, f)
