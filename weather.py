# Import Modules
import requests, datetime

# This function displays temperature in specified city
def display_temp(city, temp):
    temp_fahrenheit = (temp * 9/5) + 32
    return f"{city} weather:\n{round(temp)} degrees Celsius\n{round(temp_fahrenheit)} degrees Fahrenheit"

# This function displays sunrise and sunset times at local time
def display_sunrise_sunset(t1, t2):
    sunrise = datetime.datetime.fromtimestamp(t1, datetime.UTC).time()
    sunset = datetime.datetime.fromtimestamp(t2, datetime.UTC).time()
    return f"Sunrise Time: {sunrise} local time\nSunset Time: {sunset} local time"

# This function displays general weather and humidity
def display_weather(weather, humidity):
    return f"Weather is {weather}\nHumidity: {humidity}%"

# This function converts wind degrees to direction and displays wind direction and speed
def wind_direction_and_speed(deg, speed):
    directions = {
        (351, 360): "North",
        (0, 10): "North",
        (11, 35): "North-northeast",
        (36, 55): "North-east",
        (56, 80): "East-northeast",
        (81, 100): "East",
        (101, 125): "East-southeast",
        (126, 145): "South-east",
        (146, 170): "South-southeast",
        (171, 190): "South",
        (191, 215): "South-southwest",
        (216, 235): "South-west",
        (236, 260): "West-southwest",
        (261, 280): "West",
        (281, 305): "West-northwest",
        (306, 325): "North-west",
        (326, 350): "North-northwest"
    }
    
    for degree in directions:
        if degree[0] <= deg <= degree[1]:
            return f"Wind direction is {directions[degree]}\nWind speed: {speed} km/h"


try:
    # Get city name from user
    city = input("Where are you? ").title()

    # Get data from open weather api
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=063971ec35861a2499274dd99509ae01").json()

    # Create some variables based api data
    temp_celsius = response["main"]["temp"]
    sunrise_time = response["sys"]["sunrise"] + response["timezone"]
    sunset_time = response["sys"]["sunset"] + response["timezone"]
    weather = response["weather"][0]["description"]
    humidity = response["main"]["humidity"]
    wind_degree = response["wind"]["deg"]
    wind_speed = round(response["wind"]["speed"])

except:
    print("Please, input correct city or country name.")
else:
    # Calling functions if correct name inputted by user
    print(display_temp(city, temp_celsius))
    print(display_sunrise_sunset(sunrise_time, sunset_time))
    print(display_weather(weather, humidity))
    print(wind_direction_and_speed(wind_degree, wind_speed))