#!/usr/bin/env python3
import requests

ip = "185.223.125.151:7070"

ip2 = "localhost:8001"
def update_file(f, uuid):
    url = "http://" + ip2 + "/db/save/node?enc=0&id=" + uuid
    r = requests.post(url, data=f)
    uuid = r.json()["uuid"]


def save_file(f):
    url = "http://"+ip2+"/db/save/node?enc=0"
    r = requests.post(url, data=f)
    uuid = r.json()["uuid"]
    return uuid


def get(uuid):
    url = "http://"+ip2+"/db/get?id=" + uuid
    r = requests.post(url)
    return r.text


def save_to_main():
    pass



