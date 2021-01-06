import requests
import sys

def user(username):
    resUser = requests.get('https://api.chatwind.ga/v1/user?username=' + username)
    return resUser.json()

def servers():
    resServers = requests.get('https://api.chatwind.ga/v1/servers.json')
    return resServers.json()
