import requests
import os
from dotenv import load_dotenv
from termcolor import colored
load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")
def get_weather_data(city):
    if not city or not api_key:
        print("City or API key is missing.")
        return None
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    print(f"City: {city}")
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
def display_weather(city):
    weather_data = get_weather_data(city)

    if weather_data:
        main = weather_data["main"]
        weather = weather_data["weather"][0]
        wind = weather_data["wind"]
        city_name = weather_data["name"]
        country = weather_data["sys"]["country"]
        print(colored(f"Weather in {city_name}, {country}:", "cyan"))
        print(colored(f"Temperature: {main['temp']}°C", "yellow"))
        print(colored(f"Weather: {weather['description'].capitalize()}", "green"))
        print(colored(f"Humidity: {main['humidity']}%", "blue"))
        print(colored(f"Wind Speed: {wind['speed']} m/s", "magenta"))
    else:
        print("Could not retrieve weather data.")
if __name__ == "__main__":
    city = input(colored("Enter the name of the city: ", "yellow"))
    display_weather(city)
