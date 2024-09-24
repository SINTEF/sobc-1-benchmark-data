'''
Script that loads in several cases and compares the paths of the ship.
'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

if __name__ == '__main__':

    cases_to_compare = [
        "../calm water/run_2010_calm_water_turn_to_starboard.csv",
        "../different wave lengths/run_3100_wave_height_2_10_period_9_00_turn_to_starboard.csv",
        "../different wave lengths/run_3110_wave_height_3_24_period_11_16_turn_to_starboard.csv",
        "../different wave lengths/run_3121_wave_height_3_72_period_11_97_turn_to_starboard.csv",
        "../different wave lengths/run_3130_wave_height_4_44_period_13_06_turn_to_starboard.csv",
    ]

    case_names = [
        "calm water",
        "wave height 2.1 m, period 9.00 s",
        "wave height 3.24 m, period 11.16 s",
        "wave height 3.72 m, period 11.97 s",
        "wave height 4.44 m, period 13.06 s",
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
        y = df["YPOS [m]"].to_numpy()

        x -= x[0]
        y -= y[0]
        
        plt.plot(x[plot_indices], y[plot_indices], label=name)

    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.legend()

    plt.show()