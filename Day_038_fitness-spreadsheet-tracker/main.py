import requests
import os
from datetime import datetime as dt

NUTRITIONIX_APIKEY = os.environ["NUTRITIONIX_APIKEY"]
NUTRITIONIX_APP_ID = os.environ["NUTRITIONIX_APP_ID"]
NUTRITIONIX_URL_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

SHEETY_NUTRITIONIX_URL_ENDPOINT = "https://api.sheety.co/11b6ee99cff7ee830a6cd0edf6dff10e/workoutTracking/sheet1"

SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
SHEETY_PASSWORD = os.environ["SHEETY_PASSWORD"]
SHEETY_AUTH_TOKEN = os.environ["SHEETY_AUTH_TOKEN"]

GENDER = "female"
WEIGHT_KG = "54.4311"
HEIGHT_CM = "162"
AGE = "27"

nutriionix_header = {
    "x-app-id" : NUTRITIONIX_APP_ID,
    "x-app-key" : NUTRITIONIX_APIKEY
}

# exercise = "I ran for 3 miles" #Test Strinng
exercise = input("Tell me what exercise you did: ")
todays_date = dt.now().strftime("%m/%d/%Y")
time = dt.now().strftime("%x")

nutriionix_params = {
    "query" : exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

nutriionix_response = requests.post(url= NUTRITIONIX_URL_ENDPOINT, headers= nutriionix_header, json=nutriionix_params)
print(nutriionix_response.json())
data = nutriionix_response.json()


for exercise in data["exercises"]:
    sheety_params = {
        "sheet1":{
            "date": todays_date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

print("\n")
print(sheety_params)


sheety_header = {
    "Authorization" : SHEETY_AUTH_TOKEN
}

sheety_response = requests.post(url= SHEETY_NUTRITIONIX_URL_ENDPOINT, json=sheety_params, headers= sheety_header)
print("\n")
print(sheety_response.text)
# #print(data)