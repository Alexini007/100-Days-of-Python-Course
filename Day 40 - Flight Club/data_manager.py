import requests
import os
from dotenv import load_dotenv

load_dotenv("./.env")
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
BEARER = os.environ.get("BEARER")
SHEETY = os.environ.get("BEARER")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Authorization": BEARER
}
class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheet_response = requests.get(
            url=f"https://api.sheety.co/{SHEETY}/copyOfFlightDeals/prices", headers=headers)
        self.destination_data = sheet_response.json()["prices"]
        return self.destination_data


    def update_destination_codes(self):
        for data in self.destination_data:
            print(data)
            new_data = {
                "price": {
                    "iataCode": data["iataCode"]
                }
            }
            sheet_response = requests.put(
                url=f"https://api.sheety.co/{SHEETY}/copyOfFlightDeals/prices/{data['id']}",
                headers=headers, json=new_data)
            print(sheet_response.text)

    def get_customer_emails(self):
        response = requests.get(url=f"https://api.sheety.co/{SHEETY}/copyOfFlightDeals/users", headers=headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data