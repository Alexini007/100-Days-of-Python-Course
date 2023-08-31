import requests
from data_manager import *
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager
import os
from dotenv import load_dotenv


ORIGIN_CITY_IATA = "LON"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Authorization": BEARER
}

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()

    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        print(sheet_data)
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:

        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        notification_manager.send_emails(emails, message)

