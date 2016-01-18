import requests

def request_get(url):
    return requests.get(url)


def request_post_(url , data , headers):
    return requests.post(url,data, headers=headers)




