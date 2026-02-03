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
