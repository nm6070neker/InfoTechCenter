# Gasoline Branch

import random

QUARTER_TANK_THRESHOLD = 25  # percent

def get_gas_level():
    """
    Simulates reading gas level from a car.
    """
    return random.randint(0, 100)

def check_gas_level():
    gas_level = get_gas_level()
    print(f"Current fuel level: {gas_level}%")

    if gas_level <= QUARTER_TANK_THRESHOLD:
        print("⛽ WARNING: Fuel is at or below 1/4 tank. Please refuel soon.")
    else:
        print("✅ Fuel level is above 1/4 tank.")

# Run once
check_gas_level()
