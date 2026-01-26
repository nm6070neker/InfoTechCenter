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

import random

# Normal speed in perfect conditions
NORMAL_SPEED = 70

# Weather conditions
weather_conditions = [
    "Sunny",
    "Rainy",
    "Windy",
    "Icy",
    "Cloudy",
    "Stormy",
    "Snowy",
    "Foggy"
]

# Speed limits by weather
speed_limits = {
    "Sunny": 70,
    "Cloudy": 65,
    "Windy": 60,
    "Rainy": 55,
    "Foggy": 50,
    "Stormy": 45,
    "Snowy": 40,
    "Icy": 30
}

# Choose today's weather
today_weather = random.choice(weather_conditions)
max_speed = speed_limits[today_weather]

# Calculate reduction
speed_reduction = NORMAL_SPEED - max_speed

# Car output
print("🚗 Car System Online")
print(f"🌦 Weather detected: {today_weather}")
print(f"⚙️ Maximum safe speed: {max_speed} mph")

if speed_reduction > 0:
    print(f"⬇️ Reduce speed by {speed_reduction} mph for safety.")
else:
    print("✅ No speed reduction needed. Conditions are ideal!")
