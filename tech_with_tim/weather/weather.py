import requests
import json

with open("config.json") as json_data_file:
    data = json.load(json_data_file)
print(data["API_KEY"])

#BASE_URL = "openweathermap.org"

#city = input("Enter a city name: ")
#request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
