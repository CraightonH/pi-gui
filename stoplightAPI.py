import requests

API_BASE_URL = 'http://192.168.1.239/stoplight'

def setRed():
    resp = requests.get(API_BASE_URL + '/red')

def setYellow():
    resp = requests.get(API_BASE_URL + '/yellow')

def setGreen():
    resp = requests.get(API_BASE_URL + '/green')

def cycle():
    resp = requests.get(API_BASE_URL + '/cycle')

def off():
    resp = requests.get(API_BASE_URL + '/off')
