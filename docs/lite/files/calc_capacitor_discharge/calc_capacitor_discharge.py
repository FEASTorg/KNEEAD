# calc_capacitor_discharge.py

import math
import numpy as np
import matplotlib.pyplot as plt


def solve_time(V0, Vt, R, C):
    if Vt >= V0:
        raise ValueError("Threshold voltage must be less than initial voltage.")
    return -R * C * math.log(Vt / V0)


def solve_resistance(V0, Vt, t, C):
    if Vt >= V0:
        raise ValueError("Threshold voltage must be less than initial voltage.")
    return -t / (C * math.log(Vt / V0))


def initial_power(V0, R):
    return (V0**2) / R


def time_constant(R, C):
    return R * C


def total_energy(C, V0):
    return 0.5 * C * V0**2


def plot_discharge(V0, Vt, R, C, t_end=None):
    """
    Enhanced capacitor discharge visualization:
    - Voltage (red)
    - Power (blue)
    - Energy dissipated (green)
    - τ markers and annotated reference points
    """
    tau = time_constant(R, C)
    if t_end is None:
        t_end = 5 * tau
    t_safe = solve_time(V0, Vt, R, C)

    t_vals = np.linspace(0, t_end, 500)
    dt = t_vals[1] - t_vals[0]
    v_vals = V0 * np.exp(-t_vals / tau)
    p_vals = (v_vals**2) / R
    e_vals = np.cumsum(p_vals) * dt  # Energy dissipated over time

    fig, ax1 = plt.subplots(figsize=(10, 5))

    # Voltage plot (left y-axis)
    ax1.plot(t_vals, v_vals, color="red", lw=2, label="Voltage: $V(t)$")
    ax1.set_xlabel("Time (s)", fontsize=12)
    ax1.set_ylabel("Voltage (V)", fontsize=12, color="red")
    ax1.tick_params(axis="y", labelcolor="red")

    # Reference lines
    ax1.axhline(V0, linestyle="--", color="#6A5ACD", alpha=0.6, label=f"Y = {V0} V")
    ax1.axhline(Vt, linestyle="--", color="#2E8B57", alpha=0.6, label=f"Y = {Vt} V")
    ax1.axvline(
        t_safe, linestyle="--", color="#1E90FF", alpha=0.6, label=f"X = {t_safe:.2f} s"
    )

    # τ markers
    for i in range(1, 6):
        ax1.axvline(i * tau, linestyle="--", color="gray", alpha=0.3)
        ax1.text(
            i * tau,
            V0 + 3,
            f"{i}τ",
            ha="center",
            va="bottom",
            fontsize=9,
            color="gray",
        )

    # Power + Energy on right axis
    ax2 = ax1.twinx()
    ax2.set_ylabel("Power (W) / Energy (J)", fontsize=12)

    # Power curve (blue)
    ax2.plot(t_vals, p_vals, color="blue", lw=1.8, label="Power: $P(t)$")

    # Energy fill and curve (green)
    ax2.fill_between(
        t_vals,
        0,
        p_vals,
        color="#a6d8a8",
        alpha=0.5,
        label="Energy Area: $\int P(t) \, dt$",
    )
    ax2.plot(t_vals, e_vals, color="green", lw=2, label="Energy: $E(t)$")

    ax2.tick_params(axis="y", labelcolor="blue")

    # Annotations
    ax1.annotate(
        r"Initial Charge Voltage:  $Y = V_0$",
        xy=(t_safe / 0.75, V0),
        xytext=(t_safe / 0.75, V0 * 0.75),
        arrowprops=dict(arrowstyle="->", color="black"),
        fontsize=11,
        color="black",
        ha="left",
        va="bottom",
    )

    ax1.annotate(
        r"Safety Threshold Voltage:  $Y = V_t$",
        xy=(t_safe * 0.5, Vt),
        xytext=(t_safe * 0.5, Vt + 22),
        arrowprops=dict(arrowstyle="->", color="black"),
        fontsize=11,
        color="black",
        ha="left",
        va="top",
    )

    ax1.annotate(
        r"Discharge Time:  $X = t_{\mathrm{safe}}$",
        xy=(t_safe, Vt / 0.5),
        xytext=(t_safe + t_end * 0.1, Vt + 12),
        arrowprops=dict(arrowstyle="->", color="black"),
        fontsize=11,
        color="black",
        ha="left",
    )

    # Title, grid, and merged legend
    fig.suptitle(
        "Capacitor Discharge: Voltage, Power, and Energy Dissipation", fontsize=14
    )
    ax1.grid(True, linestyle="--", alpha=0.5)

    # Merge both legends
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax1.legend(
        lines_1 + lines_2,
        labels_1 + labels_2,
        loc="upper right",
        fontsize=10,
        handleheight=1.2,
    )

    plt.tight_layout(pad=2)
    plt.show()
