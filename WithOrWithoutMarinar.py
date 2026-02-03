import random
from datetime import datetime, timedelta

def random_alarm_time(start="06:30", end="07:30"):
    """
    Generates a random alarm time between two times.

    Args:
        start (str): Earliest possible alarm time (HH:MM)
        end (str): Latest possible alarm time (HH:MM)

    Returns:
        str: Random alarm time in HH:MM format
    """
    start_time = datetime.strptime(start, "%H:%M")
    end_time = datetime.strptime(end, "%H:%M")

    # Convert time range to minutes
    start_minutes = start_time.hour * 60 + start_time.minute
    end_minutes = end_time.hour * 60 + end_time.minute

    # Pick a random minute in the range
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


# -----------------------------
# RANDOMIZED USER SETUP
# -----------------------------
normal_alarm_time = random_alarm_time("06:30", "07:30")
extra_time_for_gas = 15  # minutes needed to stop for gas

# Calculate new alarm
new_alarm = adjust_alarm_time(normal_alarm_time, extra_time_for_gas)

print(f"⏰ Random normal alarm time: {normal_alarm_time}")
print(f"⛽ Extra time for gas: {extra_time_for_gas} minutes")
print(f"✅ New alarm time (earlier): {new_alarm}")
