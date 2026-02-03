import random

def get_nearby_gas_stations():
    """
    Simulates nearby gas stations, prices, open/closed status,
    and whether they have slurpees and snacks.
    """
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
    print("\n⛽ Nearby Gas Stations:")
    for station in stations:
        status = "OPEN ✅" if station["open"] else "CLOSED ❌"
        slurpee = "Slurpees 🥤" if station["slurpees"] else "No Slurpees"
        snacks = "Snacks 🍿" if station["snacks"] else "No Snacks"

        print(
            f"- {station['name']}: "
            f"${station['price']} | {status} | {slurpee} | {snacks}"
        )

def find_best_station(stations):
    open_stations = [s for s in stations if s["open"]]

    if not open_stations:
        return None

    return min(open_stations, key=lambda x: x["price"])

# Run once
stations = get_nearby_gas_stations()
display_gas_stations(stations)

best = find_best_station(stations)

if best:
    print(
        f"\n⭐ Best OPEN Gas Station: {best['name']} "
        f"(${best['price']} per gallon)"
    )
else:
    print("\n❌ No gas stations are currently open nearby.")
