#!/usr/bin/python3
"""Extend your Python script to export data in the CSV format"""
import csv
import json
import requests
from sys import argv


if __name__ == '__main__':
    """Gets the name with the argument passed"""
    #  if type(argv[1]) == int:
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(argv[1])).json()
    USER_ID = r.get('id')
    USERNAME = r.get('username')
    """Gets tasks accomplished"""
    t = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                     .format(argv[1])).json()
    # now we will open a file for writing
    data_file = open("{}.csv".format(argv[1]), 'w')
    # create the csv writer object
    csv_writer = csv.writer(data_file)
    for key in t:
        TASK_COMPLETED_STATUS = key.get('completed')
        TASK_TITLE = key.get('title')
        # Writing data of CSV file
        csv_writer.writerow([int(argv[1]), r.get('username'),
                             key.get('completed'),
                             key.get('title')])
    data_file.close()
