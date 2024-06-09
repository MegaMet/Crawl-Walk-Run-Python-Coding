import requests

parameter = {
    "amount" : 10,
    "type" : "boolean"
}

quiz_response = requests.get("https://opentdb.com/api.php", params= parameter)
quiz_response.raise_for_status()
data = quiz_response.json()
question_data = data["results"]

