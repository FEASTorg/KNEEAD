# calc_attenuator.py


def calc_pi_attenuator(att_db, z0):
    """
    Calculate resistor values for a Pi attenuator.

    Parameters:
        att_db (float): Desired attenuation in dB
        z0 (float): System impedance in ohms

    Returns:
        (R1, R2):
            R1 (float) = Shunt resistors (Ω)
            R2 (float) = Series resistor (Ω)
    """
    A = 10 ** (att_db / 20)
    R1 = z0 * (A + 1) / (A - 1)
    R2 = (z0 / 2) * (A - 1 / A)
    return R1, R2


def calc_tee_attenuator(att_db, z0):
    """
    Calculate resistor values for a Tee attenuator.

    Parameters:
        att_db (float): Desired attenuation in dB
        z0 (float): System impedance in ohms

    Returns:
        (R1, R2):
            R1 (float) = Series resistors (Ω)
            R2 (float) = Shunt resistor (Ω)
    """
    A = 10 ** (att_db / 20)
    R1 = z0 * (A - 1) / (A + 1)
    R2 = 2 * z0 * A / (A**2 - 1)
    return R1, R2


def calc_bridged_tee_attenuator(att_db, z0):
    """
    Calculate resistor values for a Bridged-Tee attenuator.

    Parameters:
        att_db (float): Desired attenuation in dB
        z0 (float): System impedance in ohms

    Returns:
        (R1, R2):
            R1 (float) = Bridge resistor (Ω)
            R2 (float) = Center shunt resistor (Ω)
    """
    A = 10 ** (att_db / 20)
    R1 = z0 * (A - 1)
    R2 = z0 / (A - 1)
    return R1, R2


def calc_reflection_attenuator(att_db, z0):
    """
    Calculate resistor values for a Reflection attenuator.

    Parameters:
        att_db (float): Desired attenuation in dB
        z0 (float): System impedance in ohms

    Returns:
        (R_gt, R_lt):
            R_gt (float) = Resistor value if R1 > Z0
            R_lt (float) = Resistor value if R1 < Z0
    """
    A = 10 ** (att_db / 20)
    R_gt = z0 * (A + 1) / (A - 1)
    R_lt = z0 * (A - 1) / (A + 1)
    return R_gt, R_lt
