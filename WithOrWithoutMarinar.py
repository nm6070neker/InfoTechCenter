#Weather Branch

import random
import time

NORMAL_SPEED = 70

# Weather system data
weather_data = {
    "Sunny": {
        "max_speed": 70,
        "level": "Safe",
        "message": "Clear conditions. Drive normally."
    },
    "Cloudy": {
        "max_speed": 65,
        "level": "Caution",
        "message": "Visibility slightly reduced."
    },
    "Windy": {
        "max_speed": 60,
        "level": "Caution",
        "message": "Strong winds may affect steering."
    },
    "Rainy": {
        "max_speed": 55,
        "level": "Warning",
        "message": "Wet roads detected. Reduced traction."
    },
    "Foggy": {
        "max_speed": 50,
        "level": "Warning",
        "message": "Low visibility detected."
    },
    "Stormy": {
        "max_speed": 45,
        "level": "Danger",
        "message": "Severe weather detected. Drive with extreme caution."
    },
    "Snowy": {
        "max_speed": 40,
        "level": "Danger",
        "message": "Snow-covered roads. High slip risk."
    },
    "Icy": {
        "max_speed": 30,
        "level": "Danger",
        "message": "Icy roads detected. Very dangerous conditions."
    }
}

# Select weather
today_weather = random.choice(list(weather_data.keys()))
data = weather_data[today_weather]

max_speed = data["max_speed"]
level = data["level"]
message = data["message"]

speed_reduction = NORMAL_SPEED - max_speed

# Display dashboard
print("🚗 Vehicle Safety System Online")
print("=" * 35)
print(f"🌦 Weather: {today_weather}")
print(f"⚠️ Risk Level: {level}")
print(f"🛣 Status: {message}")
print(f"⚙️ Max Safe Speed: {max_speed} mph")

if speed_reduction > 0:
    print(f"⬇️ Reduce speed by {speed_reduction} mph")

# Notification & alarm system
if level == "Warning":
    print("\n📱 Notification sent: Drive with caution.")
    
elif level == "Danger":
    print("\n🚨 EMERGENCY ALERT SENT TO PHONE")
    print("🔊 Alarm activated")
    
    for _ in range(3):
        time.sleep(0.3)

