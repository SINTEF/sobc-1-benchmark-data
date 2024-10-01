# Turning circles for SOBC-1 in calm water and in regular waves

**WARNING: TEXT AND DATA UNDER CONSTRUCTION!**

## Introduction 
This folder contains results from maneuvering tests performed in [SINTEF Ocean's ocean basin](https://www.sintef.no/en/all-laboratories/ocean-laboratory/), in February 2024. There were two main goals with the tests:

1) Measure the calm water maneuvering characteristics of SOBC-1
2) Quantify how the maneuvering is affected by different wave conditions.

The results are intended to be used for validating maneuvering simulations.

### Types of tests
All data currently shared is from turning circle tests. The vessel was first accelerated up to the design speed of 12 knots at a straight course, and then the rudder was set to a +/-35 degree deflection to initiate a turning circle.

This maneuver was performed for different wave conditions, where regular waves with different height, periods and directions relative to the start of the turning circle maneuver was generated in the ocean basin. 

## Model specification
The physical model used for this experiment was the same as the one used for measuring the calm water resistance, found [here](./../2021%20-%20calm%20water%20resistance%20and%20populsion/). Please see the report in the linked folder for details on the main dimensions. In short, the model scale was 1:32, and the loading condition was the design water line, which corresponds to a draught of 11 m in full scale. 

The rudder had a full‐scale steering rate of 2.32 deg/s corresponding to 13.13 deg/s for the scaled model. 

A friction fan was present during the model test to account for the difference in frictional resistance in model scale and full scale. The fan produced a thrust as a function of speed, continuously updated during the tests, such that the propeller was working at the correct propulsion point. This is similar to the so-called “tow force” during a propulsion test.

## Results available

The results are shared in the form of time series stored in `.csv` files. The variables in each file is the direct measurement from the tests, meaning that all values are in model scale. **Note**: the files have names that contain information about the wave condition tested. The wave condition parameters are given in full-scale values.

### Folder structure

The files are grouped into sub-folders where different parameters were varied. The groups are as follows:

- The folder "[calm water](./calm%20water/)" contains maneuvering tests without waves
- The folder "[different wave directions](./different%20wave%20directions/)" contain tests where the direction of the incoming waves were varied, while other parameters were kept fixed. The wave height was set to 3.24 m and the period to 11.16 seconds, measured in full-scale.
- The folder "[different wave lengths](./different%20wave%20lengths/)" contain tests where the both the height and period of the waves where varied, while the direction was set to head waves relative to the initial direction of the vessel. The wave height was varied between 2.1 m to 4.44 m, while the period was varied between 9.0 seconds to 13.06 seconds, measured in full-scale.
- The folder "[different wave steepness](./different%20wave%20steepness/)" contain tests where the period and direction was locked to 11.16 seconds and head waves respectively, while the wave height was varied between 3.88 m to 4.86 m in full scale. 

In addition, there is a folder called "[example_plots](./example_plots/)", which contains simple `Python` scripts that show how to load and plot the data using common libraries such as [Numpy](https://numpy.org/), [Matplotlib](https://matplotlib.org/) and [Pandas](https://pandas.pydata.org/). 

### Measured variables
Below is a list of instrumentation and measurements available for the performed tests, as well as the corresponding variable names in the `.csv` files for each measurement. 

- Optoelectronic positioning measuring system MoCap for measurement of motions in 6 degrees of
freedom. The position and rotations measurements are called `XPOS [m]`, `YPOS [m]`, `ZPOS [m]`,`ROLL [deg]`, `PITCH [deg]`, `YAW [deg]` in the `.csv` files., while the velocity measurements are called `TOTAL_SPEED [m/s]`, `SURGE_SPEED [m/s]` and `SWAY_SPEED [m/s]`.
- Four 3‐axis linear accelerometers used for finding accelerations at the Points‐of‐Interest and quality
check of the MoCap system setup. The placement of each accelerometer is described in the sub-section "Coordinate system" below. The measurements are called `ACC_1_X [m/s^2]`, `ACC_1_Y [m/s^2]`, `ACC_1_Z [m/s^2]`, `ACC_2_X [m/s^2]`, `ACC_2_Y [m/s^2]`, `ACC_2_Z [m/s^2]`, `ACC_3_Z [m/s^2]`, `ACC_3_X [m/s^2]`, `ACC_3_Y [m/s^2]`, `ACC_4_X [m/s^2]`, `ACC_4_Y [m/s^2]`, `ACC_4_Z [m/s^2]` in the `.csv` files.
- Rate gyro for measurement of roll, pitch and yaw rate. The measurements are called `GYRO_X [deg/s]`, `GYRO_Y [deg/s]` and `GYRO_Z [deg/s]` in the `.csv` file.
- Measurement of propeller revolutions per second, thrust and torque. The measurements are called `PROPELLER_REV [Hz]`, `PROPELLER_THRUST [N]` and `PROPELLER_TORQUE [N.m]` in the `.csv` files. In addition, there is a variable called `PROPELLER_REV_CTRL [Hz]` which is the control signal sent to the engine controller.
- Measurement of rudder angle. The measurement is called `RUDDER_ANGLE [deg]` in the `.csv` file. In addition, there is a variable called `RUDDER_ANGLE_CTRL [deg]` which is the control signal sent to the rudder servo.
- Measurement of rudder forces in surge and sway direction and rudder torsional moment. The measurements are called `FX_RUDDER [N]`, `FY_RUDDER [N]` and `MZ_RUDDER [N.m]` in the `.csv` files
- Relative waves at starboard and port side (at station 19.5, approximately 190 m from the aft perpendicular in full-scale). The measurements are called `RELATIVE_WAVES_STARBOARD [m]` and `RELATIVE_WAVES_PORT [m]` in the `.csv` files
- Friction fan to compensate viscous resistance on the propellers. The force from the friction fan is called `FAN_THRUST [N]` in the `.csv` files while the revolutions per second of the fan is called `FAN_REV [Hz]` and the control signal to the motor controller is called `FAN_REV_CTRL [Hz]`

The relative wave elevation in the fore ship is measured by wave tape transducers glued onto the hull and are located at station 19.5 on starboard and port side. This measurements are also used to document that the start of the maneuvers are started at a wave crest/wave top.

Motion measurements form the MoCap system are sampled at 50 Hz. Since this is a digital signal, no filtering is applied. All other measurements are sampled at 200 Hz with a low pass filter with cut‐off at 20 Hz.

During the tests, an on‐board autopilot controls the heading and the propeller RPS. The tests were carried out with constant propeller revolutions to keep the average specified vessel speed.

### Coordinate systems
To come!

