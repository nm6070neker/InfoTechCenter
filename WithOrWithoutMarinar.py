import random

def get_nearby_gas_stations():
    """
    Simulates nearby gas stations, prices, and open/closed status.
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
            "open": random.choice([True, False])
        })

    return gas_stations

def display_gas_stations(stations):
    print("\n⛽ Nearby Gas Stations:")
    for station in stations:
        status = "OPEN ✅" if station["open"] else "CLOSED ❌"
        print(
            f"- {station['name']}: "
            f"${station['price']} per gallon | {status}"
        )

def find_cheapest_open_station(stations):
    open_stations = [s for s in stations if s["open"]]

    if not open_stations:
        return None

    return min(open_stations, key=lambda x: x["price"])

# Run once
stations = get_nearby_gas_stations()
display_gas_stations(stations)

cheapest_open = find_cheapest_open_station(stations)

if cheapest_open:
    print(
        f"\n⭐ Cheapest OPEN Gas Station: "
        f"{cheapest_open['name']} at ${cheapest_open['price']} per gallon"
    )
else:
    print("\n❌ No gas stations are currently open nearby.")
