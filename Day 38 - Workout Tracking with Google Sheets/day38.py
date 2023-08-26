import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv("./.env")
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
BEARER = os.environ.get("BEARER")
SHEETY = os.environ.get("SHEETY")

exercise_input = input("Tell which exercise you did today?: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Authorization": BEARER
}

parameters = {
 "query": exercise_input,
 "gender": "male",
 "weight_kg": 72.5,
 "height_cm": 167.64,
 "age": 30
}
response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=f"https://api.sheety.co/{SHEETY}/workoutTracking/workouts", json=sheet_inputs, headers=headers)

    print(sheet_response.text)