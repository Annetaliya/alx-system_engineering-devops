#!/usr/bin/python3
''' extend your Python script to export data in json format '''

import json
import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users/"
    json_dict = requests.get(url).json()
    file_name = 'todo_all_employees.json'
    new_dict = {}

    for items in json_dict:
        name = items.get('username')
        user_id = str(items.get('id'))
        user_data = requests.get('{}{}/todos'.format(url, user_id))
        user_data = user_data.json()
        new_dict[user_id] = []
        for item in user_data:
            second_dict = {}
            second_dict['username'] = name
            second_dict['task'] = item.get('title')
            second_dict['completed'] = item.get('completed')
            new_dict[user_id].append(second_dict)

    with open(file_name, 'w') as f:
        json.dump(new_dict, f)
