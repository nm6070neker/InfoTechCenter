#Gasoline Branch

import random

# -----------------------------
# GAS LEVEL SETTINGS
# -----------------------------
QUARTER_TANK_THRESHOLD = 25  # percent

def get_gas_level():
    """Simulates reading the car's gas level."""
    return random.randint(0, 100)

def check_gas_level():
    gas_level = get_gas_level()
    print(f"\n🚗 Current fuel level: {gas_level}%")

    if gas_level <= QUARTER_TANK_THRESHOLD:
        print("⛽ WARNING: Fuel is at or below 1/4 tank!")
        return True
    else:
        print("✅ Fuel level is above 1/4 tank.")
        return False

# -----------------------------
# GAS STATION SYSTEM
# -----------------------------
def get_nearby_gas_stations():
    """Simulates nearby gas stations and their details."""
    stations = [
        "Shell",
        "Chevron",
        "BP",
        "Exxon",
        "Mobil",
        "Circle K",
        "Speedway"
    ]

    gas_stations = []

    for station in stations:
        gas_stations.append({
            "name": station,
            "price": round(random.uniform(3.10, 4.50), 2),
            "open": random.choice([True, False]),
            "slurpees": random.choice([True, False]),
            "snacks": random.choice([True, False])
        })

    return gas_stations

def display_gas_stations(stations):
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
    open_stations = [s for s in stations if s["open"]]

    if not open_stations:
        return None

    return min(open_stations, key=lambda x: x["price"])

# -----------------------------
# MAIN PROGRAM
# -----------------------------
low_gas = check_gas_level()

if low_gas:
    stations = get_nearby_gas_stations()
    display_gas_stations(stations)

    best_station = find_cheapest_open_station(stations)

    if best_station:
        print(
            f"\n⭐ Recommended Stop:\n"
            f"{best_station['name']} — ${best_station['price']} per gallon\n"
            f"Open ✅ | "
            f"{'Slurpees 🥤' if best_station['slurpees'] else 'No Slurpees'} | "
            f"{'Snacks 🍿' if best_station['snacks'] else 'No Snacks'}"
        )
    else:
        print("\n❌ No gas stations are currently open nearby.")
else:
    print("\n🚘 No need to search for gas stations right now.")
