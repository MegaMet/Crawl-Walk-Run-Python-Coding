import os
import requests

AMADUES_API_KEY = os.environ["AMADUES_API_KEY"]
AMADUES_API_SECRET = os.environ["AMADUES_API_SECRET"]

AMADUES_URL_ENDPOINT = "test.api.amadeus.com/shopping/flight-offers"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def find_flight(self):
        amadues_flight_params = {
            "currencyCode": "USD",
            "originDestinations": [
                {
                    "id": "1",
                    "originLocationCode": "NYC",
                    "destinationLocationCode": "MAD",
                    "departureDateTimeRange": {
                        "date": "2023-11-01",
                        "time": "10:00:00"
                    }
                }
            ],
            "travelers": [
                {
                    "id": "1",
                    "travelerType": "ADULT"
                }
            ],
            "sources": [
                "GDS"
            ],
            "searchCriteria": {
                "maxFlightOffers": 2,
                "flightFilters": {
                    "cabinRestrictions": [
                        {
                            "cabin": "BUSINESS",
                            "coverage": "MOST_SEGMENTS",
                            "originDestinationIds": [
                                "1"
                            ]
                        }
                    ]
                }
            }
        }
        amadues_header = {
            "client_id" : AMADUES_API_KEY,
            "client_secret" : AMADUES_API_SECRET
        }

        curl = "https://test.api.amadeus.com/v1/security/oauth2/token"
        H = {
            "Content-Type" : "application/x-www-form-urlencoded"
        }
        d = {
            "grant_type" : "client_credentials",
            "client_id" : AMADUES_API_KEY,
            "client_secret" : AMADUES_API_SECRET
        }

        response = requests.get(url=curl, json=d, headers=H)
        print(response.text)

        # response = requests.get(url= AMADUES_URL_ENDPOINT, json= amadues_flight_params, headers= amadues_header)
        # print(response.text)

"anothertk49@gmail.com"
"Zu3f!jWYtF.5XKb"