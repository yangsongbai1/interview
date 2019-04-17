import requests
import json


def add():
    url = 'http://127.0.0.1:5000/add'
    data = {
        "value_array": [
            {"value": 12},
            {"value": 18},
            {"value": 10}
        ]
    }
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(response.json())


def get_date():
    url = 'http://127.0.0.1:5000/get_date'
    response = requests.get(url)
    print(response.json())


def chat(msg):
    url = 'http://127.0.0.1:5000/chat'
    data = {
        "msg": msg
    }
    response = requests.post(url, data=data)
    print(response.json())


if __name__ == '__main__':
    add()
    get_date()
    chat('您好吗，再见了')