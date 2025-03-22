import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# API Key (Replace with your actual OpenWeatherMap API key)
API_KEY = "your_apid86e50f9d0d236ca834a3f2e39b9aee6"

# Function to fetch weather data
def get_weather(city):
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        return None

st.title("Real-Time Weather Dashboard")

city = st.text_input("Enter city name:", "New York")

if st.button("Get Weather"):
    weather_data = get_weather(city)

    if weather_data:
        temp = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        weather = weather_data["weather"][0]["description"]

        st.subheader(f"Weather in {city}")
        st.write(f"🌡️ Temperature: {temp}°C")
        st.write(f"💧 Humidity: {humidity}%")
        st.write(f"☁️ Condition: {weather.capitalize()}")

        # Save data for visualization
        df = pd.DataFrame(
            {"Metric": ["Temperature", "Humidity"], "Value": [temp, humidity]}
        )

        # Plot bar chart
        fig, ax = plt.subplots()
        ax.bar(df["Metric"], df["Value"], color=["red", "blue"])
        ax.set_ylabel("Value")
        st.pyplot(fig)

    else:
        st.error("⚠️ Unable to fetch data. Please try again.")
