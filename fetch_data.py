import requests
import csv
from datetime import datetime

# WeatherAPI credentials
API_KEY = 'db6cab3e340649858ed152506242611'  # Replace with your WeatherAPI key
CITY = 'Rawalpindi'
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&aqi=no"

def fetch_weather_data():
    try:
        response = requests.get(URL)
        print(f"Status Code: {response.status_code}")  # Debugging
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "Date": datetime.now().strftime("%Y-%m-%d"),
                "Time": datetime.now().strftime("%H:%M:%S"),
                "Temperature": data['current']['temp_c'],
                "Humidity": data['current']['humidity'],
                "Wind Speed": data['current']['wind_kph'],
                "Weather Condition": data['current']['condition']['text']
            }
            return weather_data
        else:
            print(f"Error fetching data: {response.text}")
            return None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

if __name__ == "__main__":
    print('Starting data collection...')
    with open('raw_data.csv', 'w', newline='') as csvfile:
        print("Writing data to raw_data.csv")
        writer = csv.DictWriter(csvfile, fieldnames=["Date", "Time", "Temperature", "Humidity", "Wind Speed", "Weather Condition"])
        writer.writeheader()
        for _ in range(5):  # Collect data for 5 consecutive iterations
            data = fetch_weather_data()
            if data:
                writer.writerow(data)
    print('Data collection completed.')
