import requests
import sys

def user(username):
    resCheck = requests.get('https://api.chatwind.ga/v1/user?username=' + username)
    return resCheck.json()
