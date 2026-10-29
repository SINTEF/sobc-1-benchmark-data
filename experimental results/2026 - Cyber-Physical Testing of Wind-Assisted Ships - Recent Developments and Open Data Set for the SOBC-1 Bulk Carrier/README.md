# Cyber-physical testing of SOBC-1 with rotor sails (2026)

## Introduction
This folder contains the tabulated results from the following paper:

> Sauder, T. and Kramer, J. (2026): *Cyber-Physical Testing of Wind-Assisted Ships: Recent Developments and Open Data Set for the SOBC-1 Bulk Carrier*. Journal of Sailing Technology, Volume 11, Issue 1, pp. 453-480. The Society of Naval Architects and Marine Engineers. [Link](https://onepetro.org/JST/article/11/01/453/808430/Cyber-Physical-Testing-of-Wind-Assisted-Ships)

Please see the paper for a full description of the test setup, the test program and a discussion of the results. A short summary is given below, followed by a description of the data files.

## Test setup
The tests were performed in SINTEF Ocean's towing tank in September 2025, with the same hull model (M3246A, scale 1:32) as used in the [2021 calm water tests](./../2021%20-%20calm%20water%20resistance%20and%20propulsion/), at the design draught of 11.0 m. See that folder for the main particulars of the hull and propeller. Bilge keels were not fitted.

The tests were *cyber-physical*: the ship model was free-running, while the loads from four virtual rotor sails were computed in real time by a dynamic lifting line model (the open-source library [Stormbird](https://github.com/NTNU-IMT/stormbird)), and applied to the model by a cable-driven parallel robot (CDPR). The lifting line model used the measured ship motion as input, closing the loop at 200 Hz. In some tests, the aerodynamic loads on the superstructure were also included, using a simplified Blendermann model (see Table 1).

The main properties of the setup were:

- **Rotor sails:** four rotor sails, 35 m high with 5 m diameter, and a top end plate with 6 m diameter. The positions are given in the table below. All sails are 12.5 m from the centreline. The typical rotational speed was 180 rpm in 10 m/s wind and 100 rpm in 15 m/s wind.
- **Wind:** a power-law atmospheric boundary layer profile with exponent 1/9, as suggested by the ITTC guidelines for predicting the power savings of wind-powered ships.
- **Propulsion and steering:** the propeller rotational speed was controlled (not the power). Course keeping was ensured by an autopilot. The rudder angle and rudder loads were measured.
- **Friction correction:** a "towing" force $\tau_1$ was applied by the CDPR at deck level, in the direction of motion, to compensate for the too large frictional resistance in model scale: $\tau_1 = 3.1613 u + 4.8966 u^2$, in N, where $u$ is the forward speed in model scale in m/s (water temperature 18.6 °C).
- **Service speed:** the target service speed was 12.25 kn ± 0.2 kn. The propeller is idling (zero thrust) at 37.20 rpm at service speed.

| Sail | Side      | Longitudinal position from midship [m] |
|------|-----------|----------------------------------------|
| S1   | Port      | -56                                    |
| S2   | Port      | +14                                    |
| S3   | Starboard | -21                                    |
| S4   | Starboard | +44                                    |

### Conventions
- A body-fixed coordinate system $\{b\}$ = (B, $b_1$, $b_2$, $b_3$) is attached to the ship, with $b_1$ pointing forwards, $b_2$ towards starboard and $b_3$ downwards. The origin B is located at midship, on the centreplane and at deck level, 12.48 m above the waterline. The Earth-fixed system $\{n\}$ coincides with $\{b\}$ when the ship is at rest.
- Forces and moments are given in $\{b\}$, and moments are about B. As an example, the roll moment is positive when a positive (starboard) side force acts above deck.
- The true wind direction (TWD) is 0° for a wind propagating against the ship's direction of motion (head wind) and 180° for a wind propagating in the same direction as the ship (following wind). In all tests, the wind comes from the port side, so that a TWD of 90° gives a positive (starboard) side force.
- The drift angle is the yaw angle minus the course over ground.
- A positive rudder angle triggers a starboard turn.

### Values in the tables
- **Units:** all values are in full scale, except the CDPR configuration in Table 2, which is in model scale.
- **Averaging:** for the steady tests (Tables 3 to 8), the values are averages over the last 30 seconds of each test. The column `RudAngleStDev` gives the standard deviation of the rudder angle in the same window, which indicates how much the autopilot had to use the rudder to keep the course.
- **Repeatability:** a repeated reference test (TWD 120°, TWS 10 m/s) showed that the results are reproduced within about ±2% of the average value. The exceptions are quantities that are small in this condition: the rudder side force varied by up to 0.3 N (model scale), and the drift angle by up to 0.04°.

## Files
The tables are stored as comma-separated files in the [`tables`](./tables/) folder, with one file per table in the paper. The values are copied directly from the paper, with the same precision. The column names are the same as in the paper, with the unit in square brackets.

| File | Content | Table in paper | Section in paper |
|------|---------|----------------|------------------|
| [`table_1_superstructure_force_model.csv`](./tables/table_1_superstructure_force_model.csv) | Parameters of the superstructure force model | Table 1 | 2.5 |
| [`table_2_cdpr_configuration.csv`](./tables/table_2_cdpr_configuration.csv) | Geometry of the cable-driven parallel robot (CDPR), model scale | Table 2 | Appendix A |
| [`table_3_speed_power_calm_water.csv`](./tables/table_3_speed_power_calm_water.csv) | Speed-power curve in calm conditions, without sails (7000 series) | Table 3 | 3.1 |
| [`table_4_service_speed_nominal_sails.csv`](./tables/table_4_service_speed_nominal_sails.csv) | Service speed in 10 m/s and 15 m/s wind with four sails (2000 series) | Table 4 | 3.2 |
| [`table_5_maximum_sail_thrust.csv`](./tables/table_5_maximum_sail_thrust.csv) | Service speed with 100%, 90% and 50% of the thrust from the sails (3000 series) | Table 5 | 3.3 |
| [`table_6_alternative_sail_placements.csv`](./tables/table_6_alternative_sail_placements.csv) | Service speed with only the fore or only the aft sails (5000 series) | Table 6 | 3.4 |
| [`table_7_parametric_external_loads.csv`](./tables/table_7_parametric_external_loads.csv) | Parametric study with prescribed external side force and yaw moment (6000 series) | Table 7 | 3.5 |
| [`table_8_transient_companion_tests.csv`](./tables/table_8_transient_companion_tests.csv) | Steady tests at the initial and final wind conditions of the three transient scenarios (4000 series) | Table 8 | 3.6 |

The time series from the transient tests (Figures 11 to 14 in the paper) are not included.

## Description of the tables

### Table 1: Superstructure force model
Parameters of the superstructure force model, which is an adapted version of the model by Blendermann (1994). The forces depend on the apparent wind angle $\beta_A$ and the apparent wind speed $V_A$:

$$a(\beta_A) = 1 - \frac{\delta_B}{2}\left(1 - \frac{C_X(0)}{C_Y(\pi/2)}\right)\sin^2(2\beta_A)$$

$$X(\beta_A) = 0.5 \rho A_F V_A^2 \, C_X(0) \frac{\cos\beta_A}{a(\beta_A)}, \qquad Y(\beta_A) = 0.5 \rho A_L V_A^2 \, C_Y(\pi/2) \frac{\sin\beta_A}{a(\beta_A)}$$

$$N(\beta_A) = Y(\beta_A) \, x_{\text{eff}}, \qquad M(\beta_A) = Y(\beta_A) \, z_{\text{eff}}$$

where $X$, $Y$, $M$ and $N$ are the surge force, side force, roll moment and yaw moment, and $\rho$ is the air density.

| Column | Description |
|--------|-------------|
| `CX(0) [-]` | Surge force coefficient in head wind, from CFD of the superstructure without sails |
| `CY(pi/2) [-]` | Side force coefficient in beam wind, from CFD of the superstructure without sails |
| `delta_B [-]` | Empirical coefficient in the Blendermann model |
| `AF [m2]` | Frontal projected area |
| `AL [m2]` | Lateral projected area |
| `x_eff [m]` | Longitudinal position of the centre of effort, relative to midship |
| `z_eff [m]` | Vertical position of the centre of effort, relative to the deck |

### Table 2: CDPR configuration
Geometry of the cable-driven parallel robot that applies the sail loads to the model. The robot has six actuators on the towing carriage, connected to a frame on the deck of the model with thin lines. All lengths are in model scale.

| Column | Description |
|--------|-------------|
| `i [-]` | Actuator and line number |
| `p_i^n.n1 [m]`, `p_i^n.n2 [m]`, `p_i^n.n3 [m]` | Position of actuator $i$, expressed in the Earth-fixed system $\{n\}$ |
| `r_i^b.b1 [m]`, `r_i^b.b2 [m]`, `r_i^b.b3 [m]` | Attachment point of line $i$ on the ship model, expressed in the body-fixed system $\{b\}$ |

### Table 3: Speed-power curve in calm conditions
Six tests without wind and without sails, where the propeller rotational speed was increased from 28 to 71 rpm. Only the friction correction was applied by the CDPR.

| Column | Description |
|--------|-------------|
| `Test [-]` | Test number |
| `PropRPM [rpm]` | Propeller rotational speed |
| `PropThrust [kN]` | Propeller thrust |
| `PropTorque [kNm]` | Propeller torque |
| `ShipSpeed [kn]` | Ship speed |

### Tables 4, 5, 6 and 8: Tests with rotor sails
These tables have the same columns.

- **Table 4 (2000 series):** service speed with the four sails, for a TWS of 10 m/s (rotors at 180 rpm) and 15 m/s (rotors at 100 rpm), and TWD from 45° to 180°. When the speed was too high, the propeller rpm was reduced. If the propeller ended up idling, the rotor speed was reduced instead.
- **Table 5 (3000 series):** service speed with the four sails at 180 rpm, and 100%, 90% or 50% of the thrust from the sails. The wind speed was adjusted to reach the service speed. For 100% thrust from the sails, the propeller rpm was adjusted to give zero thrust.
- **Table 6 (5000 series):** service speed with only two sails, in 15 m/s wind, with rotors at 100 rpm and 180 rpm. The 50xx and 52xx series are with the fore sails only (S2 and S4), and the 51xx and 53xx series are with the aft sails only (S1 and S3). The table also contains the 22xx series from Table 4, with four sails in 15 m/s wind, for comparison.
- **Table 8 (4000 series):** steady tests at the initial and final wind conditions of the three transient scenarios in Section 3.6. The scenarios are based on wind measurements onboard a coastal vessel, for instance when crossing the outlet of a fjord. The 40xx series is without loads on the superstructure, and the 41xx series includes them. Tests xx40 and xx50 are the initial and final conditions for scenario 1, xx60 and xx70 for scenario 2, and xx80 and xx90 for scenario 3.

| Column | Description |
|--------|-------------|
| `Test [-]` | Test number |
| `TWD [deg]` | True wind direction (see Conventions) |
| `TWS [m/s]` | True wind speed |
| `AWA [deg]` | Apparent wind angle |
| `AWS [m/s]` | Apparent wind speed |
| `RotorRPM [rpm]` | Rotational speed of the rotor sails (common for all sails) |
| `PropRPM [rpm]` | Propeller rotational speed |
| `PropThrust [kN]` | Propeller thrust |
| `PropTorque [kNm]` | Propeller torque |
| `SailThrust [kN]` | Total sail force along $b_1$ (forwards) |
| `SailSideForce [kN]` | Total sail force along $b_2$ (towards starboard) |
| `SailRollMom [kNm]` | Sail roll moment about B |
| `SailPitchMom [kNm]` | Sail pitch moment about B |
| `SailYawMom [kNm]` | Sail yaw moment about B |
| `ShipSpeed [kn]` | Ship speed |
| `RollAngle [deg]` | Roll angle |
| `DriftAngle [deg]` | Drift angle (yaw angle minus course over ground) |
| `RudderAngle [deg]` | Mean rudder angle. Positive triggers a starboard turn |
| `RudAngleStDev [deg]` | Standard deviation of the rudder angle in the averaging window |
| `RudderForce [kN]` | Measured side force on the rudder. The data are consistent with positive towards starboard ($b_2$): a positive rudder angle gives a negative force |

### Table 7: Parametric study with external loads
A "sail-agnostic" study, where the external side force and yaw moment were prescribed directly by the CDPR, instead of being computed by a sail model. The side force was varied from 0 to 840 kN, and the yaw moment from -16.1 MNm (corresponding to sails at the aft part of the ship) to +16.1 MNm (fore sails). A roll moment proportional to the side force was applied, so that the side force acts 25 m above deck. The propeller rotational speed was kept constant at the value that gives the service speed without external loads (60.7 rpm according to the text in the paper, while the measured values in the table are about 60.5 rpm). The only external thrust was the friction correction.

| Column | Description |
|--------|-------------|
| `Test [-]` | Test number |
| `Ext surge [kN]` | Applied external force along $b_1$. This is the friction correction $\tau_1$, scaled to full scale (matches the formula above within 1%) |
| `Ext sway [kN]` | Applied external side force along $b_2$ |
| `Ext roll [kNm]` | Applied external roll moment about B |
| `Ext pitch [kNm]` | Applied external pitch moment about B |
| `Ext yaw [kNm]` | Applied external yaw moment about B |
| `Ship speed [kn]` | Ship speed |
| `Roll angle [deg]` | Roll angle |
| `Yaw angle [deg]` | Yaw angle |
| `Drift [deg]` | Drift angle (yaw angle minus course over ground) |
| `PropThrust [kN]` | Propeller thrust |
| `PropRPM [RPM]` | Propeller rotational speed |
| `PropTorque [kNm]` | Propeller torque |
| `RudderAng [deg]` | Mean rudder angle. Positive triggers a starboard turn |
| `RudderForce [kN]` | Measured side force on the rudder (same sign convention as in Tables 4-6 and 8) |
