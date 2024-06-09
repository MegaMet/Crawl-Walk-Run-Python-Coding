import requests
import os
from datetime import datetime as dt

TOKEN = "iy54n1m35k9s"
USERNAME = "anothertk"
GRAPHID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
post_endpoint = f"{graph_endpoint}/{GRAPHID}"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" :"yes"
}

# response = requests.post(url= pixela_endpoint, json= user_params)
# print(response.text)

headers = {
    "X-USER-TOKEN" : TOKEN
}

graph_params = {
    "id" : GRAPHID,
    "name" : "Coding Graph",
    "unit" : "commit",
    "type" : "int",
    "color" : "sora"
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers= headers)
# print(response.text)

todays_date = dt.now()

post_params = {
    "date" : todays_date.strftime("%Y%m%d"),
    "quantity" : "1"
}

# response = requests.post(url=post_endpoint, json=post_params, headers= headers)
# print(response.text)

select_date = dt(year= 2024, month= 6, day= 1).strftime("%Y%m%d")

update_params = {
    "quantity" : "4"
}

# response = requests.put(url=f"{post_endpoint}/{select_date}", json=update_params, headers= headers)
# print(response.text)

response = requests.delete(url=f"{post_endpoint}/{select_date}", headers= headers)
print(response.text)
