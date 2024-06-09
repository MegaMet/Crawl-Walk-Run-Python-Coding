import requests
import smtplib
import os

STOCK_NAME = "IBM"
COMPANY_NAME = "IBM"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "Z9HTYQX27HLIOINK"
NEWS_API_KEY = "cf11fea3630b459996d77249f87bc260"

# EMAIL = os.environ("Email")
# PASSWORD = os.environ("PASSWORD")

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : STOCK_API_KEY
}

new_params = {
    "q" : COMPANY_NAME,
    "apiKey" : NEWS_API_KEY
}

response = requests.get(STOCK_ENDPOINT, stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = None
if (difference > 0):
    up_down = "🔺"
else:
    up_down = "🔻"
print(difference)

diff_percent = round((difference / yesterday_closing_price) * 100)
print(diff_percent)

if abs(diff_percent < 1):
    response = requests.get(NEWS_ENDPOINT, new_params)
    articles = response.json()["articles"]
    first_three = articles[:3]

    # formatted_articles_list = [f"\n{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}.\nBreif: {article['description']}\n" for article in first_three]
    formatted_articles = ""
    for article in first_three:
        formatted_articles += f"\n{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}.\nBreif: {article['description']}\n"

    print(formatted_articles)

    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user=EMAIL, password=PASSWORD)
    #     connection.sendmail(from_addr=EMAIL,
    #                         to_addrs=EMAIL,
    #                         msg=f"Subject:Stock Price Change!\n\nTop 3 articles realated to {COMPANY_NAME}:\n{formatted_articles_list}")

