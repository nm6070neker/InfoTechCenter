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



#Weather Branch

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



#Gasoline Branch

import random
from datetime import datetime, timedelta

# ============================================================
# SETTINGS
# ============================================================

QUARTER_TANK_THRESHOLD = 25      # 1/4 tank fuel threshold
EXTRA_TIME_FOR_GAS = 15          # Minutes needed to stop for gas

# Wake-up time range (realistic morning window)
ALARM_START = "06:30"
ALARM_END = "07:30"


# ============================================================
# GAS LEVEL FUNCTIONS
# ============================================================

def get_gas_level():
    """
    Simulates reading the car's gas level (0–100%).
    """
    return random.randint(0, 100)


def check_gas_level():
    """
    Checks gas level and determines if fuel is low.

    Returns:
        bool: True if fuel is at or below 1/4 tank
    """
    gas_level = get_gas_level()
    print(f"\n🚗 Current fuel level: {gas_level}%")

    if gas_level <= QUARTER_TANK_THRESHOLD:
        print("⛽ WARNING: Fuel is at or below 1/4 tank!")
        return True
    else:
        print("✅ Fuel level is above 1/4 tank.")
        return False


# ============================================================
# ALARM FUNCTIONS
# ============================================================

def random_alarm_time(start, end):
    """
    Generates a random alarm time between two times.

    Args:
        start (str): Earliest alarm time (HH:MM)
        end (str): Latest alarm time (HH:MM)

    Returns:
        str: Random alarm time (HH:MM)
    """
    start_time = datetime.strptime(start, "%H:%M")
    end_time = datetime.strptime(end, "%H:%M")

    start_minutes = start_time.hour * 60 + start_time.minute
    end_minutes = end_time.hour * 60 + end_time.minute

    random_minutes = random.randint(start_minutes, end_minutes)

    hour = random_minutes // 60
    minute = random_minutes % 60

    return f"{hour:02d}:{minute:02d}"


def adjust_alarm_time(normal_alarm, extra_minutes):
    """
    Moves the alarm earlier to allow time for getting gas.
    """
    alarm_time = datetime.strptime(normal_alarm, "%H:%M")
    new_alarm_time = alarm_time - timedelta(minutes=extra_minutes)
    return new_alarm_time.strftime("%H:%M")


# ============================================================
# GAS STATION FUNCTIONS
# ============================================================

def get_nearby_gas_stations():
    """
    Simulates nearby gas stations with prices and features.
    """
    station_names = [
        "Shell",
        "Chevron",
        "BP",
        "Exxon",
        "Mobil",
        "Circle K",
        "Speedway"
    ]

    stations = []

    for name in station_names:
        stations.append({
            "name": name,
            "price": round(random.uniform(3.10, 4.50), 2),
            "open": random.choice([True, False]),
            "slurpees": random.choice([True, False]),
            "snacks": random.choice([True, False])
        })

    return stations


def display_gas_stations(stations):
    """
    Displays gas station details.
    """
    print("\n📍 Nearby Gas Stations:")

    for s in stations:
        status = "OPEN ✅" if s["open"] else "CLOSED ❌"
        slurpee = "Slurpees 🥤" if s["slurpees"] else "No Slurpees"
        snacks = "Snacks 🍿" if s["snacks"] else "No Snacks"

        print(
            f"- {s['name']}: "
            f"${s['price']} | {status} | {slurpee} | {snacks}"
        )


def find_cheapest_open_station(stations):
    """
    Finds the cheapest gas station that is currently open.
    """
    open_stations = [s for s in stations if s["open"]]

    if not open_stations:
        return None

    return min(open_stations, key=lambda x: x["price"])


# ============================================================
# MAIN PROGRAM
# ============================================================

# Step 1: Randomize normal wake-up time
normal_alarm_time = random_alarm_time(ALARM_START, ALARM_END)

# Step 2: Check fuel level
low_gas = check_gas_level()

print(f"\n⏰ Normal wake-up time: {normal_alarm_time}")

# Step 3: If gas is low, adjust alarm and show gas stations
if low_gas:
    new_alarm = adjust_alarm_time(normal_alarm_time, EXTRA_TIME_FOR_GAS)

    print(
        f"⛽ Extra time needed for gas: {EXTRA_TIME_FOR_GAS} minutes\n"
        f"✅ New alarm time: {new_alarm}"
    )

    stations = get_nearby_gas_stations()
    display_gas_stations(stations)

    best_station = find_cheapest_open_station(stations)

    if best_station:
        print(
            f"\n⭐ Recommended Gas Station:\n"
            f"{best_station['name']} — ${best_station['price']} per gallon\n"
            f"Open ✅ | "
            f"{'Slurpees 🥤' if best_station['slurpees'] else 'No Slurpees'} | "
            f"{'Snacks 🍿' if best_station['snacks'] else 'No Snacks'}"
        )
    else:
        print("\n❌ No gas stations are currently open nearby.")

else:
    print("\n🚘 No need to adjust alarm or search for gas stations.") 
    #Test