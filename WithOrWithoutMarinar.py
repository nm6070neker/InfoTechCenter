import random

def get_nearby_gas_stations():
    """
    Simulates nearby gas stations and gas prices.
    Prices are per gallon.
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
        price = round(random.uniform(3.10, 4.50), 2)
        gas_stations.append({
            "name": station,
            "price": price
        })

    return gas_stations

def display_gas_stations(stations):
    print("\n⛽ Nearby Gas Stations:")
    for station in stations:
        print(f"- {station['name']}: ${station['price']} per gallon")

def find_cheapest_station(stations):
    cheapest = min(stations, key=lambda x: x["price"])
    return cheapest

# Run once
stations = get_nearby_gas_stations()
display_gas_stations(stations)

cheapest = find_cheapest_station(stations)
print(
    f"\n💰 Cheapest Gas Station Nearby: "
    f"{cheapest['name']} at ${cheapest['price']} per gallon"
)
