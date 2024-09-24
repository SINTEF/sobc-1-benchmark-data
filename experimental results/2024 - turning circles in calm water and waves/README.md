# Turning circles for SOBC-1 in calm water and in regular waves

**WARNING: TEXT AND DATA UNDER CONSTRUCTION!**

## Introduction 
This folder contains results from a maneuvering test campaign performed in [SINTEF Ocean's ocean basin](https://www.sintef.no/en/all-laboratories/ocean-laboratory/) in February 2024. The goal of the tests was to perform a standard turning circle maneuver - which is useful for validating maneuvering simulations in calm water - and to quantify how the turning circle is affected by different wave conditions - inteded for more advanced simulation validation where the effect of waves are included. 

All wave conditions in this test campaign consisted of regular waves with different height, periods and directions relative to the start of the turning circle maneuver. 

## Model specification
The physical model used for this experiment was the same as the one used for estimating the calm water resistance in [this folder](./../2021%20-%20calm%20water%20resistance%20and%20populsion/). Please see the report in the linked folder for details on the main dimensions. In short, the model scale was 1:32, and the loading condition was the design water line, which corresponds to a draught of 11 m in full scale. 

### Rudder parameters
For turning circle test the maximum rudder deflections were set to +‐35 degrees. The rudder had a full‐scale steering rate of 2.32 deg/s corresponding to 13.13 deg/s for the hull model. This is in line with DnV’s criterion, which says that a rudder shall turn from ‐35 to +30 degrees in 28 seconds.

### Instrumentation
The following instrumentation and measurements are available for the performed tests:
- Optoelectronic positioning measuring system MoCap for measurement of motions in 6 DOF (degree of
freedom).
- Four 3‐axis linear accelerometers used for finding accelerations at the Points‐of‐Interest and quality
check of the MoCap system setup.
- Measurement of propeller rps, thrust and torque.
- Measurement of rudder angle.
- Measurement of rudder forces in surge and sway direction and rudder torsional moment.
- Rate gyro for measurement of roll, pitch and yaw rate.
- Relative waves at starboard and port side (at station 19.5).
- Fiction fan to compensate viscous resistance on the propellers.

The relative wave elevation in the fore ship is measured by a wave tape transducer glued onto the hull and
are located at station 19.5 on starboard and port side. This measurements are also used to document that the
start of the maneuvers are started at a wave crest/wave top.

Motion measurements form the MoCap system are sampled at 50 Hz. Since this is a digital signal, no filtering
is applied. All other measurements are sampled at 200 Hz with a low pass filter with cut‐off at 20 Hz.

During the tests, an on‐board autopilot controls the heading and the propeller RPS. The tests were carried out
with constant propeller revolutions to keep the average specified vessel speed.

## Results available

