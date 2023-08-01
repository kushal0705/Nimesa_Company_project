import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch weather data. Status code:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error while fetching weather data:", e)
        return None