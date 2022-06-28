# -*- Coding: utf-8 -*-
# Author: heaton
# @Time: 2022/5/17 20:28
# @File: test.py
import json

import requests


def add():
    url = 'http://127.0.0.1:50000/erp/bill'

    url_header = {"Content-Type":"application/json"}

    payload ={
        "id":"",
        "orderQuantity": "10m",
        "materialType": "C35",
        "admixtureCombination":"",
        "slumps":"",
        "pouringType": "10",
        "pumpTruckHeight": 38,
        "pourSite": "",
        "planUseTime": "2022-05-20 07:00:00",
        "memo": "",
        "stationId":"",
        "station": "",
        "projectId": "",
        "projectName": "",
        "placer": "",
        "orderDate": "",
        "placerPhone": ""
    }
    resq = requests.post(url,headers=url_header,data=json.dumps(payload))
    print(resq.json())
    # print(resq.json()['add']['id'])

# add()

def login():
    login_url = "http://127.0.0.1:50000/temdata"
    payload = {"username":"hsw","password":"123"}
    url_header = {"Content-Type": "application/json"}
    respone = requests.post(login_url,headers=url_header,data=json.dumps(payload))
    print(respone.text)

login()