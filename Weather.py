import requests

API_KEY = "d86e50f9d0d236ca834a3f2e39b9aee6"
CITY = "Dehli"  # Change to your desired city
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Weather: {data['weather'][0]['description']}")
else:
    print("Error:", response.status_code, response.json())

    import csv

weather_data = {
    "City": data["name"],
    "Temperature (°C)": data["main"]["temp"],
    "Humidity (%)": data["main"]["humidity"],
    "Weather": data["weather"][0]["description"]
}

import csv

filename = "weather_data.csv"
with open(filename, mode="a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=weather_data.keys())
    if file.tell() == 0:
        writer.writeheader()
    writer.writerow(weather_data)

print(f"Weather data saved to {filename}")

cities = ["Dehli", "London", "Punjab", "Sydney"]

for city in cities:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"{city}: {data['main']['temp']}°C, {data['weather'][0]['description']}")
    else:
        print(f"Failed to fetch data for {city}")

import csv
import schedule
import time
import random

cities = ["Dehli", "London", "Punjab", "Sydney"]

def fetch_weather_data():
    weather_records = []
    
    for city in cities:
        weather_data = {
            "City": city,
            "Temperature": f"{random.randint(10, 35)}°C",
            "Humidity": f"{random.randint(30, 80)}%",
            "Condition": random.choice(["Sunny", "Cloudy", "Rainy", "Snowy"])
        }
        weather_records.append(weather_data)

    with open("weather.csv", mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["City", "Temperature", "Humidity", "Condition"])
        
        if file.tell() == 0:
            writer.writeheader()
        
        writer.writerows(weather_records)
    
    print("Weather data updated:", weather_records)

schedule.every(1).hour.do(fetch_weather_data)

if __name__ == "__main__":
    fetch_weather_data() 
    while True:
        schedule.run_pending()
        time.sleep(60)  