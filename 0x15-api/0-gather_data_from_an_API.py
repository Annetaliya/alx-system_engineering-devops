#!/usr/bin/python3
''' script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
'''
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/" + user_id
    json_dict = requests.get(url).json()
    name_of = json_dict.get("name")
    user_task = requests.get("https://jsonplaceholder.typicode.com/todos")
    user_task = user_task.json()
    total_task = 0
    completed_list = []
    complete_task = 0

    for item in user_task:
        if item.get('userId') == int(user_id):
            total_task += 1
            if item.get('completed') is True:
                complete_task += 1
                completed_list.append(item.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format(
        name_of, complete_task, total_task))

    for title in completed_list:
        print('\t {}'.format(title))
