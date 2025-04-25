# calc_capacitance_conversion.py


def convert_capacitance(value, from_unit):
    """
    Convert input capacitance to all supported units.
    from_unit must be one of: 'pF', 'nF', 'uF', 'F'
    """
    units = {"pF": 1e-12, "nF": 1e-9, "uF": 1e-6, "F": 1}

    if from_unit not in units:
        raise ValueError("Invalid unit. Use 'pF', 'nF', 'uF', or 'F'.")

    # Convert to farads as base
    f_value = value * units[from_unit]

    # Convert to all units
    conversions = {
        "pF": f_value / units["pF"],
        "nF": f_value / units["nF"],
        "uF": f_value / units["uF"],
        "F": f_value,
    }

    return conversions


def decode_capacitor_code(code):
    """
    Decode a standard 3-digit capacitor code (e.g., '104' → 100nF).
    Returns value in pF.
    """
    code = str(code).strip()

    if len(code) != 3 or not code.isdigit():
        raise ValueError("Capacitor code must be a 3-digit number.")

    sig = int(code[:2])
    mult = int(code[2])
    pf = sig * (10**mult)

    return pf
