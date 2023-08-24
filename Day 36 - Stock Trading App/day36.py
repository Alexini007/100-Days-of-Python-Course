import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv("/Day 36 - Stock Trading App/.env")
STOCKS_API_KEY = os.environ.get("STOCKS_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

api_key = os.environ.get("api_key")
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

parameters = {
    "apikey": STOCKS_API_KEY,
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM"

}

response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]
close_yesterday = float(data_list[0]["4. close"])
close_2days_ago = float(data_list[58]["4. close"])

difference = close_yesterday - close_2days_ago
diff_percent = round((close_yesterday - close_2days_ago) / close_yesterday * 100)
up_down = None
if difference > 0:
    up_down = "🔼"
else:
    up_down = "🔽"

if (abs(close_yesterday - close_2days_ago) / close_yesterday) * 100 > 5:
    print("News")

    parameters2 = {
        "apikey": NEWS_API_KEY,
        "q": "IBM"
    }

    response = requests.get(url="https://newsapi.org/v2/everything", params=parameters2)
    response.raise_for_status()
    data2 = response.json()["articles"]  # from beginning to 2 -> so first 3 articles
    three_articles = data2[:3]
    print(three_articles[0]["description"])
    formatted_articles = [f"IBM:{up_down}{diff_percent}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in
                          three_articles]
    print(formatted_articles)
    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+17068072382",
            to="***"
        )

    print(message.status)



