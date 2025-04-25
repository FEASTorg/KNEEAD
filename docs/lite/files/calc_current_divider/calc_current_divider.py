# calc_current_divider.py


def parallel_resistance(resistors):
    """
    Calculate the equivalent resistance of resistors in parallel.

    Parameters:
    resistors (list of float): List of resistor values in ohms.

    Returns:
    float: Equivalent parallel resistance in ohms.
    """
    if not resistors or any(R <= 0 for R in resistors):
        raise ValueError("Resistors must be a list of positive non-zero values.")
    return 1 / sum(1 / R for R in resistors)


def current_through_branch(I_source, resistors, index):
    """
    Calculate the current through a specific resistor in a parallel network.

    Parameters:
    I_source (float): Total current supplied to the parallel network (in amps).
    resistors (list of float): Resistor values in ohms.
    index (int): Index of the resistor to compute current through.

    Returns:
    float: Current through the specified resistor (in amps).
    """
    if index >= len(resistors):
        raise IndexError("Index out of range of resistors list.")
    Rn = resistors[index]
    R_total = parallel_resistance(resistors)
    return I_source * (R_total / Rn)
