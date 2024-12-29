# Weather_App_PythonProject
A command-line weather application where the user can input a city name, and the app fetches and displays the current weather.

## Objective
Create a command-line weather application where the user can input a city name, and the app fetches and displays the current weather.

## Features
### User Input
Prompt the user to enter a city name.

### API Integration
Use a free weather API like
OpenWeatherMap
to fetch real-time weather data.
Parse the API response to display relevant information like temperature, humidity, and weather description.

### Error Handling
Handle errors such as invalid city names or network issues.

## How it Works
How It Works:
### API Endpoint:
The script uses the WeatherAPI endpoint:
http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no
Replace {API_KEY} with your actual API key and {city} with the city name.

### Weather Data:
The app retrieves the current temperature, weather condition, humidity, and wind speed.
It uses the current weather endpoint from WeatherAPI.

### Error Handling:
The app handles invalid city names or network issues gracefully.
It displays relevant error messages for troubleshooting.

### User Interaction:
Users can input a city name to fetch the weather.
Typing exit quits the program.
