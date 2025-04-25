from fractions import Fraction
import math


def decimal_to_fraction(x, max_denominator=10**6):
    """
    Convert a decimal number to its best rational approximation under max_denominator.
    Warns the user if the resulting denominator reaches max_denominator.

    Returns:
        Fraction
    """
    f = Fraction(x).limit_denominator(max_denominator)
    if f.denominator == max_denominator:
        print(
            f"⚠️ Warning: Maximum denominator {max_denominator} reached. Result may be a coarse approximation."
        )
    return f


def fraction_to_decimal(frac):
    """
    Convert a Fraction to float.
    """
    return float(frac)


def fraction_to_mixed(frac):
    """
    Convert improper Fraction to a mixed number (whole + remainder/denominator).
    Returns: (whole:int, remainder:Fraction)
    """
    whole = frac.numerator // frac.denominator
    remainder = Fraction(frac.numerator % frac.denominator, frac.denominator)
    return whole, remainder


def mixed_to_fraction(whole, remainder):
    """
    Convert a mixed number (int + Fraction) back to improper Fraction.
    """
    return Fraction(
        whole * remainder.denominator + remainder.numerator, remainder.denominator
    )


def generate_fraction_approximations(x, max_denominator=256, max_steps=20):
    """
    Generates a sorted list of approximate fractions using power-of-two denominators.

    Returns:
        List of dicts with:
            - numerator, denominator
            - fraction
            - approx
            - error (absolute)
    """
    int_part = math.floor(x)
    frac_part = x - int_part
    max_power = int(math.log2(max_denominator))
    denominators = [2**i for i in range(2, max_power + 1)]
    if len(denominators) > max_steps:
        raise ValueError(
            f"Needs {len(denominators)} steps; exceeds limit of {max_steps}."
        )

    results = []
    for d in denominators:
        n = round(frac_part * d)
        f = Fraction(n, d)
        approx_val = int_part + n / d
        abs_err = abs(x - approx_val)
        pct_err = (abs_err / x) * 100
        results.append(
            {
                "numerator": n,
                "denominator": d,
                "fraction": f,
                "approx": approx_val,
                "error": abs_err,
                "percent_error": pct_err,
            }
        )

    results.sort(key=lambda e: e["error"])
    return results
