#!/usr/bin/python3
"""
This script interacts with JSONPlaceholder API using the requests library.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints their titles.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves them in a CSV file.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()
        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                writer.writerow(
                    {'id': post['id'], 'title': post['title'], 'body': post['body']})


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
