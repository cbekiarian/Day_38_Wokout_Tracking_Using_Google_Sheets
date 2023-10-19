import requests
import datetime as dt
import os

API_KEY = os.environ.get("API_KEY")
APP_ID = os.environ.get("APP_ID")
SHEETY_ENDPOINT =os.environ.get("SHEETY_ENDPOINT")

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
# SHEETY_ENDPOINT = "https://api.sheety.co/e11f87f0122ceda5ca43b5a02b935667/myWorkouts/workouts"

headers ={
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
entered_text = input("What exercise did you do?")
exercise_parameters = {
     "query":entered_text,
     "gender":"male",
     "weight_kg":82,
     "height_cm":172.82,
     "age":25
}

TOKEN = os.environ.get("TOKEN")
headers1 = {
    "Authorization": TOKEN }

response = requests.post(url=EXERCISE_ENDPOINT,json=exercise_parameters,headers=headers)
response.raise_for_status()
response=response.json()
exercises = response["exercises"]
print(response)


for element in exercises:
    type = element["user_input"]
    duration = element["duration_min"]
    calories = element["nf_calories"]
    sheety_parameters = {
        "workout": {
          "date": dt.datetime.now().strftime("%d/%m/%Y"),
          "time": dt.datetime.now().strftime("%X"),
          "exercise": type,
          "duration": duration,
          "calories": calories,

        }
    }
    response1 = requests.post(url=SHEETY_ENDPOINT, json=sheety_parameters,headers=headers1)
    response1.raise_for_status()
    print(response1)

