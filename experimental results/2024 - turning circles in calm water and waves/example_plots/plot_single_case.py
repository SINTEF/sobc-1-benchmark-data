'''
Simple example showing how to load a csv file, and plot the path, speed, rudder angle and forces.
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv("../time_series/test2010_calm_water_turn_port.csv") # Switch the path to load another case
    
    w_plot = 16
    fig = plt.figure(figsize=(w_plot, w_plot / 1.85))
    ax1 = fig.add_subplot(221, aspect='equal')
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)

    time_ax_list = [ax2, ax3, ax4]

    ax1.set_title("Path")
    ax1.plot(df["XPOS [m]"], -df["YPOS [m]"]) # plot negative y-axis to view the data as if the vessel is viewed from above
    ax1.set_xlabel("x [m]")
    ax1.set_ylabel("y [m]")

    ax2.plot(df["Time [s]"], df["TOTAL_SPEED [m/s]"], label="Total")
    ax2.plot(df["Time [s]"], df["SURGE_SPEED [m/s]"], label="Surge")
    ax2.plot(df["Time [s]"], df["SWAY_SPEED [m/s]"], label="Sway")
    ax2.set_xlabel("Time [s]")
    ax2.set_ylabel("Speed [m/s]")
    ax2.legend()

    ax3.plot(df["Time [s]"], np.abs(df["RUDDER_ANGLE [deg]"]))
    ax3.set_xlabel("Time [s]")
    ax3.set_ylabel("|Rudder angle| [deg]")
    ax3.set_ylim(-5, 40.0)

    ax4.plot(df["Time [s]"], df["PROPELLER_THRUST [N]"], label="Propeller thrust")
    ax4.plot(df["Time [s]"], df["FAN_THRUST [N]"], label="Fan thrust")
    ax4.plot(df["Time [s]"], df["FX_RUDDER [N]"], label="Rudder surge")
    ax4.plot(df["Time [s]"], df["FY_RUDDER [N]"], label="Rudder sway")
    ax4.set_ylim(-20, 25) # Force limits may be necessary to adjust for different cases
    ax4.set_xlabel("Time [s]")
    ax4.set_ylabel("Force [N]")
    ax4.legend()

    plt.show()