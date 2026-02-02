#BetaTestDev

# Welcome Branch
# This program simulates a basic operating system boot sequence
# Developer: Natalie Maher

# Libraries Imported Here
import sys      # Used to control terminal output (overwrite the same line)
import time     # Used to add delays for the boot animation

# ANSI color codes for terminal text formatting
CYAN = "\033[96m"     # Cyan color for headings
YELLOW = "\033[93m"   # Yellow color for the booting animation
GREEN = "\033[92m"    # Green color for successful access message
RESET = "\033[0m"     # Resets text color back to default

# Display welcome and version information
print(f"\n{CYAN}Welcome Branch - Developer: Natalie Maher{RESET}\n")
print(f"{CYAN}Welcome to InfoTech Center v.1.0{RESET}\n")

# Initialize counters for the boot sequence
x = 0                 # Controls how many times the loop runs
ellipsis = 0          # Controls the number of dots shown in the loading animation

# Loop runs until the boot sequence completes 20 cycles
while x != 20:
    x += 1            # Increment the loop counter

    # Create the boot message with animated dots
    ellipsisMessage = f"{YELLOW}InfoTechCenter OS Booting{'.' * ellipsis}{RESET}"
    ellipsis += 1     # Increase the number of dots each loop

    # Write the message to the same terminal line
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()    # Forces the output to appear immediately

    time.sleep(0.5)       # Pause to simulate loading time

    # Reset dots after three dots are displayed
    if ellipsis == 4:
        ellipsis = 0

    # Display final message when boot sequence is complete
    if x == 20:
        print(f"\n{GREEN}Operating System Booted Up - Retina Scanned - Access Granted{RESET}")

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

