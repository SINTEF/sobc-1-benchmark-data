'''
Script that loads in several cases and compares the paths of the ship.
'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

if __name__ == '__main__':

    cases_to_compare = [
        "../time_series/test2010_calm_water_turn_port.csv",
        "../time_series/test3110_wave_height_3.24_period_11.16_direction_0_turn_port.csv",
        "../time_series/test4020_wave_height_3.24_period_11.16_direction_90_turn_port.csv",
        "../time_series/test4070_wave_height_3.24_period_11.16_direction_180_turn_port.csv"
    ]

    case_names = [
        "calm water",
        "wave direction 0.0 degrees",
        "wave direction 90.0 degrees",
        "wave direction 180.0 degrees"
    ]

    w_plot = 16
    fig = plt.figure(figsize=(w_plot, w_plot / 1.85))
    ax = fig.add_subplot(111, aspect='equal')

    t_max = 250

    for case, name in zip(cases_to_compare, case_names):
        df = pd.read_csv(case)

        t = df["Time [s]"].to_numpy()
        t -= t[0]

        plot_indices = np.where(t < t_max)

        x = df["XPOS [m]"].to_numpy()
        y = -df["YPOS [m]"].to_numpy() # Reverse the axis, to view the data as if viewed from above

        x -= x[0]
        y -= y[0]
        
        plt.plot(x[plot_indices], y[plot_indices], label=name)

    plt.title("Effect of wave direction with wave height 3.24 m and period 11.16 s")

    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.legend()

    plt.show()