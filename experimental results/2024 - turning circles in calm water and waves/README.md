# Turning circles for SOBC-1 in calm water and in regular waves

**WARNING: TEXT AND DATA UNDER CONSTRUCTION!**

## Introduction 
This folder contains results from maneuvering tests performed in [SINTEF Ocean's ocean basin](https://www.sintef.no/en/all-laboratories/ocean-laboratory/), in February 2024. There were two main goals with the tests:

1) Measure the calm water maneuvering characteristics of SOBC-1
2) Quantify how the maneuvering is affected by different wave conditions.

### Types of tests
All data currently shared is from turning circle tests. The vessel was first accelerated up to the design speed of 12 knots at a straight course, and then the rudder was set to a +/-35 degree deflection to initiate a turning circle with a fixed propeller rotational speed.

This maneuver was performed for different wave conditions, meaning regular waves with different height, periods and directions relative to the start of the turning circle maneuver. 

## Model specification
The physical model used for this experiment was the same as the one used for measuring the calm water resistance, found [here](./../2021%20-%20calm%20water%20resistance%20and%20populsion/). Please see the report in the linked folder for details on the main dimensions and geometry. In short, the model scale was 1:32, and the loading condition was the design water line, which corresponds to a draught of 11 m in full-scale. 

The rudder had a full‐scale steering rate of 2.32 deg/s corresponding to 13.13 deg/s for the scaled model. 

A *friction fan* was present during the tests to account for the difference in frictional resistance in model scale and full-scale. The fan produced a thrust as a function of speed, continuously updated during the tests, such that the propeller was working at the correct propulsion point. The effect of the friction fan is similar to the so-called "tow force" during a straight-ahead propulsion test.

## Results available

The results are shared in the form of time series stored in `.csv` files. The variables in files are the direct measurement from the tests, meaning that all values are in model scale. **Note**: the files have names that contain information about the wave condition tested. The wave condition parameters are given in full-scale values.

### Folder structure

The raw results from the the experiments are located in the "[time_series](./time_series/)" folder. Each file has a test number and a name that described the test conditions. An overview of conditions in the different tests are also found in the excel file [test_overview.xlsx](./test_overview.xlsx).

There is also a folder called "[example_plots](./example_plots/)", which contains simple `Python` scripts that show how to load and plot the data using common libraries such as [Numpy](https://numpy.org/), [Matplotlib](https://matplotlib.org/) and [Pandas](https://pandas.pydata.org/). 

### Measured variables
Below is a list of instrumentation and measurements available for the performed tests, as well as the corresponding variable names in the `.csv` files for each measurement. 

- Optoelectronic positioning measuring system MoCap for measurement of motions in 6 degrees of freedom. The position and rotations measurements are called `XPOS [m]`, `YPOS [m]`, `ZPOS [m]`,`ROLL [deg]`, `PITCH [deg]`, `YAW [deg]` in the `.csv` files, while the velocity measurements are called `TOTAL_SPEED [m/s]`, `SURGE_SPEED [m/s]` and `SWAY_SPEED [m/s]`.
- Four 3‐axis linear accelerometers used for finding accelerations at the Points‐of‐Interest and quality check of the MoCap system setup. The placement of each accelerometer is described in the sub-section "Coordinate system" below. The measurements are called `ACC_1_X [m/s^2]`, `ACC_1_Y [m/s^2]`, `ACC_1_Z [m/s^2]`, `ACC_2_X [m/s^2]`, `ACC_2_Y [m/s^2]`, `ACC_2_Z [m/s^2]`, `ACC_3_Z [m/s^2]`, `ACC_3_X [m/s^2]`, `ACC_3_Y [m/s^2]`, `ACC_4_X [m/s^2]`, `ACC_4_Y [m/s^2]`, `ACC_4_Z [m/s^2]` in the `.csv` files.
- Rate gyro for measurement of roll, pitch and yaw rate. The measurements are called `GYRO_X [deg/s]`, `GYRO_Y [deg/s]` and `GYRO_Z [deg/s]` in the `.csv` file.
- Measurement of propeller revolutions per second, thrust and torque. The measurements are called `PROPELLER_REV [Hz]`, `PROPELLER_THRUST [N]` and `PROPELLER_TORQUE [N.m]` in the `.csv` files. In addition, there is a variable called `PROPELLER_REV_CTRL [Hz]` which is the control signal sent to the engine controller.
- Measurement of rudder angle. The measurement is called `RUDDER_ANGLE [deg]` in the `.csv` file. In addition, there is a variable called `RUDDER_ANGLE_CTRL [deg]` which is the control signal sent to the rudder servo.
- Measurement of rudder forces in surge and sway direction and rudder torsional moment. The measurements are called `FX_RUDDER [N]`, `FY_RUDDER [N]` and `MZ_RUDDER [N.m]` in the `.csv` files
- Relative waves at starboard and port side (at station 19.5, approximately 190 m from the aft perpendicular in full-scale). The measurements are called `RELATIVE_WAVES_STARBOARD [m]` and `RELATIVE_WAVES_PORT [m]` in the `.csv` files
- Friction fan to compensate viscous resistance on the propellers. The force from the friction fan is called `FAN_THRUST [N]` in the `.csv` files while the revolutions per second of the fan is called `FAN_REV [Hz]` and the control signal to the motor controller is called `FAN_REV_CTRL [Hz]`

The relative wave elevation in the fore ship is measured by wave tape transducers glued onto the hull and are located at station 19.5 on starboard and port side. This measurements are also used to document that the start of the maneuvers are started at a wave crest/wave top.

Motion measurements form the MoCap system are sampled at 50 Hz. Since this is a digital signal, no filtering is applied. All other measurements are sampled at 200 Hz with a low pass filter with cut‐off at 20 Hz.

During the tests, an on‐board autopilot controls the heading and the propeller RPS. The tests were carried out with constant propeller revolutions to keep the average specified vessel speed.

### Coordinate system and placements
The position of the vessel is measured in a right-handed coordinate system placed in the middle of the ocean basin, with the z-axis pointing down. In other words, when the vessel is moving along the positive x-axis, a starboard turns means a turn towards the positive y-axis. **Note**: in the example plots, the y-axis is set to be negative, which means the turn direction will be as if the vessel is seen from above.

The wave direction is measured relative to the x-axis, where a positive angle represent a left-handed rotation around the z-axis. In other words, a +90 degrees wave direction means that the waves come from the port side, pushing the ship towards the starboard side relative to the initial path.

Most variables are reported in a ship-fixed coordinate system. This is located at the midpoint between the fore and aft perpendicular, at the base line (bottom of the vessel), and center line (midway between port and starboard). The x-axis is pointing towards the bow, the y-axis towards starboard side, and the z-axis downwards.

The measurements of the accelerations and relative wave amplitude comes from sensors placed at different locations. The locations are given in the table below:

| Sensor | x-position, full-scale [m] | y-position, full-scale [m] | z-position, full-scale [m] |
|--------|----------------------------|----------------------------|----------------------------|
| Accelerometer 1 | 221.4 | -0.2  | -17.0 |
| Accelerometer 2 | 140.3 | -12.0 | -3.8 |
| Accelerometer 3 | 119.1 | 12.3  | -10.5 |
| Accelerometer 4 | 31.1  | -12.2 | -11.5 |
| Starboard wave tape transducer| 189.9 | Flush to hull starboard | 0-10 |
| Port wave tape transducer | 190.1 | Flush to hull port | 0-10 |

The rudder torsional moment is measured around the rudder axis, i.e., the aft perpendicular.


