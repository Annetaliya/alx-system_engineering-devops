#!/usr/bin/python3
''' extend your Python script to export data in the CSV format '''

import csv
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/" + user_id
    json_dict = requests.get(url).json()
    name_of = json_dict.get("username")
    user_task = requests.get("{}/todos".format(url))
    user_task = user_task.json()
    file_name = user_id + '.csv'

    with open(file_name, 'w') as csvfile:
        for items in user_task:
            csvfile.write('"{}","{}","{}","{}"\n'.format(items.get(
                "userId"), name_of, items.get("completed"),
                items.get("title")))
