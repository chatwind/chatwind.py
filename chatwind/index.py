import requests
import sys

baseURL = "https://api.chatwindapp.com/v1"

def user(username):
    resUser = requests.get(baseURL+'/user?username='+username)
    return resUser.json()

def servers():
    resServers = requests.get(baseURL+'/servers.json')
    return resServers.json()

def customcode(code):
    resCustomCode = requests.get(baseURL+'/customcode?code='+code)
    return resCustomCode.json()
