#Weather Branch

import random

weather_conditions = [
    "Sunny",
    "Rainy",
    "Windy",
    "Icy",
    "Cloudy",
    "Stormy",
    "Snowy"
]

today_weather = random.choice(weather_conditions)

print(f"Today's weather is {today_weather}.")
