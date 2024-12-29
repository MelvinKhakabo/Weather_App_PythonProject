#code to get the weather of a city using the WeatherAPI

import requests

# Replace this with your actual WeatherAPI key
API_KEY = "09d47f5bf4a44d0785e130319242912"

def get_weather(city):
    # Base URL for WeatherAPI
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    
    try:
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Extract and display weather information
            location = data["location"]["name"]
            country = data["location"]["country"]
            temperature = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"]
            humidity = data["current"]["humidity"]
            wind_speed = data["current"]["wind_kph"]
            
            print(f"\nWeather in {location}, {country}:")
            print(f"  Temperature: {temperature}°C")
            print(f"  Condition: {condition}")
            print(f"  Humidity: {humidity}%")
            print(f"  Wind Speed: {wind_speed} km/h")
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def main():
    print("Welcome to the Weather App!")
    while True:
        city = input("\nEnter a city name (or type 'exit' to quit): ")
        if city.lower() == "exit":
            print("Goodbye!")
            break
        get_weather(city)

if __name__ == "__main__":
    main()

