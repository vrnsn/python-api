#!/usr/bin/python
import json
import requests
import pprint

rest_url_base = "https://hx-cluster.dcv.svpod/coreapi/v1/"

headers = {"Content-Type": "application/json", "Authorization": "Bearer {0}".format(access_token)}

def get_account_info():

    header = {"Content-Type": "application/json"}
    rest_url = "https://hx-cluster.dcv.svpod/aaa/v1/auth?grant_type=password"
    content = { "username": "demouser@DCV.SVPOD", "password": "C1sco12345", "client_id": "HxGuiClient", "client_secret": "Sunnyvale", "redirect_uri": "http://localhost:8080/aaa/redirect"}
    response = requests.post(rest_url, json=content, verify=False)

    if response.status_code == 201:
        return json.loads(response.content.decode("utf-8"))
    else:
        return None


account_info = get_account_info()

if account_info is not None:
    access_token = account_info["access_token"]
    print("Your bearer information is: ")
    for k, v in account_info.items():
        print("{0}: {1}".format(k, v))
else:
    print("Something went wrong")

def get_clusters():

    rest_url = "{}clusters".format(rest_url_base)
    response = requests.get(rest_url, headers = headers, verify=False)

    if response.status_code == 200:
        return json.loads(response)
    else:
        return(response.status_code)


cluster_info = get_clusters()
print (cluster_info)
