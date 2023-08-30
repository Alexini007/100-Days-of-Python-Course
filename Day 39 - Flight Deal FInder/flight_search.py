import requests
from flight_data import FlightData
import os
from dotenv import load_dotenv

load_dotenv("./.env")
TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")


tequila_headers = {
    "apikey": TEQUILA_API_KEY,
}


class FlightSearch:
    def get_destination_code(self, city_name):
        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url="https://api.tequila.kiwi.com/locations/query", params=query, headers=tequila_headers)
        results = response.json()["locations"]
        code = results[0]["code"]
        print(code)
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }
        response = requests.get(url="https://api.tequila.kiwi.com/v2/search", headers=tequila_headers, params=parameters)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data