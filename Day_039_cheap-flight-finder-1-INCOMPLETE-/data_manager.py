import os
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    SHEETY_NUTRITIONIX_URL_ENDPOINT = "https://api.sheety.co/11b6ee99cff7ee830a6cd0edf6dff10e/workoutTracking/sheet1"

    SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
    SHEETY_PASSWORD = os.environ["SHEETY_PASSWORD"]
    SHEETY_AUTH_TOKEN = os.environ["SHEETY_AUTH_TOKEN"]

    def __init__(self):

        pass