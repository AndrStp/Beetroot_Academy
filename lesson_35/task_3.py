"""
Task 3

Requests using multiprocessing

Download all comments from a subreddit of your choice using 
URL: https://api.pushshift.io/reddit/comment/search/ . 

As a result, store all comments in chronological order in JSON and dump 
it to a file. For this task use Threads for making requests to reddit API.
"""


import requests
import json
import time
import concurrent.futures


def main():
    data = get_json()
    comments = extract_info(data)
    save_json(comments)


def get_json() -> dict:
    """Return the JSON-dict from the api"""
    page = 'https://api.pushshift.io/reddit/comment/search/'
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(requests.get, page)
        r = future.result()
    return r.json()


def extract_info(data: dict) -> dict:
    """Return the JSON-dict with key 'comments'
    and the list of dicts with the following keys:
    author, comment, link, time"""
    comments_dict = {'comments': []}

    data_key = data.get('data')
    for el in data_key:
        temp = {}
        temp['author'] = el.get('author')
        temp['comment'] = el.get('body')
        temp['link'] = el.get('permalink')

        epoch_time = el.get('created_utc')
        temp['time'] = time.ctime(epoch_time)

        comments_dict.get('comments').append(temp)
    
    return comments_dict


def save_json(data: dict) -> None:
    """Dumps the data to the cooments.txt"""
    with open('comments.txt', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    main()