LATITUDE = 22.845640
LONGITUDE = 89.540329
OWM_ENDPOINT_URL = "https://api.openweathermap.org/data/2.5/weather?"
\
import os
import requests
import smtplib

API_KEY = os.environ.get("API_KEY")
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

#lat={lat}&lon={lon}&appid={API key}
params_dic = {
    "lat" : LATITUDE,
    "lon" : LONGITUDE,
    "appid" : API_KEY
}

response = requests.get(OWM_ENDPOINT_URL, params= params_dic)
weather_data = response.json()
weather_id = weather_data["weather"][0]["id"]
if int(weather_id) < 700:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=f"Subject:Its Rain!\n\nBring an umbrella.")


