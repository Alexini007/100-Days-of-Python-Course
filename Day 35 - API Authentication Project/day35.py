import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv("/Day 35 - API Authentication Project/.env")
api_key = os.environ.get("API_KEY")
account_sid = os.environ.get("SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": 60.674622,
    "lon": 17.141830,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]  # slice the data so we get only the first 12 hours


will_rain = False
for hour_data in weather_slice:
    if int(hour_data["weather"][0]["id"]) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_="+17068072382",
        to="***"
    )

    print(message.status)
