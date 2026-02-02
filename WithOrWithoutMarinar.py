import random
import time

# -------------------------------------------------
# BASELINE VEHICLE SETTINGS
# -------------------------------------------------

# Normal driving speed when conditions are perfect
NORMAL_SPEED = 70


# -------------------------------------------------
# WEATHER SYSTEM DATA (Weather Branch)
# -------------------------------------------------
# This dictionary acts as the "Weather Branch" of the program.
# Each weather condition contains:
#   - max_speed: The highest safe speed for that condition
#   - level: Risk severity (Safe, Caution, Warning, Danger)
#   - message: Driver-facing status message
#
# The program will branch its behavior based on the weather chosen.

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


# -------------------------------------------------
# WEATHER SELECTION LOGIC
# -------------------------------------------------

# Randomly choose one weather condition from the dictionary keys
today_weather = random.choice(list(weather_data.keys()))

# Retrieve the data for the selected weather
data = weather_data[today_weather]

# Extract specific values for easier access
max_speed = data["max_speed"]
level = data["level"]
message = data["message"]

# Calculate how much the driver must slow down
# (Only applies if weather is worse than normal)
speed_reduction = NORMAL_SPEED - max_speed


# -------------------------------------------------
# DRIVER DASHBOARD DISPLAY
# -------------------------------------------------

print("🚗 Vehicle Safety System Online")
print("=" * 35)
print(f"🌦 Weather: {today_weather}")
print(f"⚠️ Risk Level: {level}")
print(f"🛣 Status: {message}")
print(f"⚙️ Max Safe Speed: {max_speed} mph")

# Only show speed reduction if slowing down is required
if speed_reduction > 0:
    print(f"⬇️ Reduce speed by {speed_reduction} mph")


# -------------------------------------------------
# NOTIFICATION & ALERT BRANCHING LOGIC
# -------------------------------------------------
# This section reacts differently depending on risk level.
# This is a classic conditional "branch" in programming.

if level == "Warning":
    # Warning-level conditions send a phone notification
    print("\n📱 Notification sent: Drive with caution.")

elif level == "Danger":
    # Dangerous conditions trigger emergency alerts and alarms
    print("\n🚨 EMERGENCY ALERT SENT TO PHONE")
    print("🔊 Alarm activated")

    # Simulate alarm beeps using a timed loop
    for _ in range(3):
        time.sleep(0.3)
