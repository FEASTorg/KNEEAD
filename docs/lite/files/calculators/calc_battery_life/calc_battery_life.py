# calc_battery_life.py


def calc_battery_life(capacity_mAh, current_mA):
    """
    Calculate battery life in hours from battery capacity (mAh) and load current (mA).
    """
    if current_mA <= 0:
        raise ValueError("Current must be greater than 0 mA.")
    return capacity_mAh / current_mA


def format_battery_life(hours, unit="hours"):
    """
    Convert battery life from hours to the desired time unit.
    """
    if unit == "hours":
        return f"{hours:.2f} Hours"
    elif unit == "days":
        return f"{hours / 24:.2f} Days"
    elif unit == "weeks":
        return f"{hours / (24 * 7):.2f} Weeks"
    elif unit == "months":
        return f"{hours / (24 * 30):.2f} Months"
    elif unit == "years":
        return f"{hours / (24 * 365):.2f} Years"
    else:
        return f"{hours:.2f} Hours"
