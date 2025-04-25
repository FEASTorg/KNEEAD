# calc_dbm_watts_conversion.py

import math
import matplotlib.pyplot as plt
import numpy as np


def dbm_to_watts(dbm):
    """
    Convert decibel-milliwatts (dBm) to watts (W). Raises warning if input exceeds 110 dBm (~100 MW).

    Formula: W = 10 ** ((dBm - 30) / 10)
    """
    if dbm <= 0:
        raise ValueError("Input must be greater than 0 dBm.")
    if dbm > 110:
        raise ValueError(
            "Input exceeds 110 dBm (100 MW). Value is outside practical range."
        )
    return 10 ** ((dbm - 30) / 10)


def watts_to_dbm(watts):
    """
    Convert watts (W) to decibel-milliwatts (dBm).
    Raises warning if input is less than or equal to 0.
    Raises warning if input exceeds 100 MW (110 dBm).

    Formula: dBm = 10 * log10(W) + 30
    """
    if watts <= 0:
        raise ValueError("Power in watts must be greater than zero.")
    if watts > 1e8:
        raise ValueError(
            "Power exceeds 100 MW (110 dBm). Value is outside practical range."
        )
    return 10 * math.log10(watts) + 30


def plot_dbm_to_watts_curve(dbm_input):
    """
    Plot dBm to Watts curve with the given input value marked on the curve.
    """
    x_min = dbm_input - 6
    x_max = dbm_input + 2
    dbm_vals = np.linspace(x_min, x_max, 300)
    watt_vals = 10 ** ((dbm_vals - 30) / 10)

    highlight_watts = 10 ** ((dbm_input - 30) / 10)

    plt.figure(figsize=(7, 4))
    plt.plot(
        dbm_vals, watt_vals, linestyle="--", color="red", linewidth=2, label="dBm to W"
    )
    plt.scatter(
        [dbm_input],
        [highlight_watts],
        color="red",
        s=80,
        zorder=5,
        label=f"{dbm_input:.1f} dBm",
    )

    plt.title("dBm to Watts", fontsize=12)
    plt.xlabel("dBm")
    plt.ylabel("Watts")
    plt.grid(True, which="both", linestyle="--", alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.show()
