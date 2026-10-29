# Calm water resistance and propulsion tests of SOBC-1 (2021)

## Introduction
This folder contains results from calm water resistance and propulsion tests of SOBC-1, performed in SINTEF Ocean's towing tank in May 2021. The full test report is found in [Preliminary_302006033-09_Model_Tests_SOBC-1.pdf](./Preliminary_302006033-09_Model_Tests_SOBC-1.pdf).

The tests were done with the hull model M3246A at scale 1:32.0, for two loading conditions:

| Loading condition | Description       | Draught AP / FP, full scale [m] |
|-------------------|-------------------|---------------------------------|
| `WL1`             | Ballast water line | 7.50 / 5.40                    |
| `DWL`             | Design water line  | 11.00 / 11.00                  |

The report covers resistance tests, propulsion tests, propeller open water tests and 3D wake measurements. The resistance, open water and wake results are available as machine-readable files (see below). **The propulsion test results are currently only available in the report.**

The model was fitted with a rudder and headbox, and a trip wire turbulence stimulator at station 19. No bilge keels were fitted on the model. An allowance for 0.35 m high bilge keels with length 0.3 x LPP is added as an appendage resistance in the full-scale prediction.

## Files

| File | Content | Source in report |
|------|---------|------------------|
| [`main_particulars.json`](./main_particulars.json) | Main particulars, hydrostatic corrections, resistance analysis parameters and appendage data for both loading conditions. Propeller particulars and wake test conditions | E-2, E-3, E-4.1, E-5, E-7, E-9, E-10 |
| [`open_water/P1608_open_water.csv`](./open_water/P1608_open_water.csv) | Open water characteristics of the propeller P1608, model scale | E-4.1 |
| [`wake_data/WL1_wake_measurements.csv`](./wake_data/WL1_wake_measurements.csv) | Measured axial, tangential and radial wake in the propeller plane, WL1 | E-9.1, E-9.2 |
| [`wake_data/WL1_wake_mean_values.csv`](./wake_data/WL1_wake_mean_values.csv) | Circumferential mean wake at each radius, WL1 | E-9.1, E-9.2 |
| [`wake_data/WL1_wake_harmonics_axial.csv`](./wake_data/WL1_wake_harmonics_axial.csv) | Harmonic analysis of the axial wake, WL1 | E-9.8 – E-9.10 |
| [`wake_data/WL1_wake_harmonics_radial.csv`](./wake_data/WL1_wake_harmonics_radial.csv) | Harmonic analysis of the radial wake, WL1 | E-9.11 – E-9.13 |
| [`wake_data/WL1_wake_harmonics_tangential.csv`](./wake_data/WL1_wake_harmonics_tangential.csv) | Harmonic analysis of the tangential wake, WL1 | E-9.14 – E-9.16 |
| [`wake_data/DWL_wake_measurements.csv`](./wake_data/DWL_wake_measurements.csv) | Measured axial, tangential and radial wake in the propeller plane, DWL | E-10.1, E-10.2 |
| [`wake_data/DWL_wake_mean_values.csv`](./wake_data/DWL_wake_mean_values.csv) | Circumferential mean wake at each radius, DWL | E-10.1, E-10.2 |
| [`wake_data/DWL_wake_harmonics_axial.csv`](./wake_data/DWL_wake_harmonics_axial.csv) | Harmonic analysis of the axial wake, DWL | E-10.8 – E-10.10 |
| [`wake_data/DWL_wake_harmonics_radial.csv`](./wake_data/DWL_wake_harmonics_radial.csv) | Harmonic analysis of the radial wake, DWL | E-10.11 – E-10.13 |
| [`wake_data/DWL_wake_harmonics_tangential.csv`](./wake_data/DWL_wake_harmonics_tangential.csv) | Harmonic analysis of the tangential wake, DWL | E-10.14 – E-10.16 |
| [`resistance_data/WL1_model_resistance.csv`](./resistance_data/WL1_model_resistance.csv) | Measured model resistance and model-scale coefficients, WL1 | E-5.1 |
| [`resistance_data/WL1_model_appendage_resistance.csv`](./resistance_data/WL1_model_appendage_resistance.csv) | Model-scale appendage resistance coefficients, WL1 | E-5.2 |
| [`resistance_data/WL1_ship_appendage_resistance.csv`](./resistance_data/WL1_ship_appendage_resistance.csv) | Full-scale appendage resistance coefficients, WL1 | E-5.3 |
| [`resistance_data/WL1_ship_resistance_coefficients.csv`](./resistance_data/WL1_ship_resistance_coefficients.csv) | Full-scale resistance coefficients, WL1 | E-5.4 |
| [`resistance_data/WL1_ship_resistance.csv`](./resistance_data/WL1_ship_resistance.csv) | Full-scale resistance, effective power, sinkage and trim, WL1 | E-5.5 |
| [`resistance_data/DWL_model_resistance.csv`](./resistance_data/DWL_model_resistance.csv) | Measured model resistance and model-scale coefficients, DWL | E-7.1 |
| [`resistance_data/DWL_model_appendage_resistance.csv`](./resistance_data/DWL_model_appendage_resistance.csv) | Model-scale appendage resistance coefficients, DWL | E-7.2 |
| [`resistance_data/DWL_ship_appendage_resistance.csv`](./resistance_data/DWL_ship_appendage_resistance.csv) | Full-scale appendage resistance coefficients, DWL | E-7.3 |
| [`resistance_data/DWL_ship_resistance_coefficients.csv`](./resistance_data/DWL_ship_resistance_coefficients.csv) | Full-scale resistance coefficients, DWL | E-7.4 |
| [`resistance_data/DWL_ship_resistance.csv`](./resistance_data/DWL_ship_resistance.csv) | Full-scale resistance, effective power, sinkage and trim, DWL | E-7.5 |

All CSV files are comma-separated, with one header row. The resistance tables have one row per speed (7 to 17 knots in steps of 0.5 knots). The values are copied directly from the tables in the report, with the same precision. Column names follow the symbols used in the report, with the unit in square brackets. Many coefficients are given multiplied by a power of ten, as in the report. This is shown in the column name. For example, `CTM*10^3 [-]` holds the value of $C_{TM} \cdot 10^3$. To get $C_{TM}$, divide the column by 1000.

### Main particulars (`main_particulars.json`)
At the top level, the JSON file contains:

- `propeller`: the particulars of the propeller P1608 (full scale and model scale) and the open water test conditions (E-4.1).
- `wake_measurements`: the test conditions for the 3D wake measurements, which are common to both loading conditions.

For each loading condition (`WL1` and `DWL`), the JSON file contains:

- `principal_particulars`: the principal hull data in E-2.1 and E-3.1. Each entry gives the symbol, unit, full-scale value (`ship`) and model-scale value (`model`). The transverse projected area above the waterline, `AV`, is used for the air resistance and comes from the resistance reports (E-5.1 / E-7.1). Hydrostatic corrections are included.
- `hydrostatic_corrections`: the corrections to wetted surface, volume and LCB in E-2.2 and E-3.2.
- `resistance_analysis`: the constants used to scale the resistance from model to full scale. These are the form factor $1+k$, the air resistance coefficients $C_{AAM}$ and $C_{AAS}$, the correlation coefficient $C_A$, and the water temperatures and kinematic viscosities.
- `appendages_for_resistance_scaling`: appendage data used for the appendage resistance scaling in E-5.2/E-5.3 and E-7.2/E-7.3. The only appendage used is the bilge keels, which are only present in full scale.

## Example plots
The folder [`example_plots`](./example_plots/) contains `Python` scripts that show how to load and plot the data, using [Pandas](https://pandas.pydata.org/), [Numpy](https://numpy.org/) and [Plotly](https://plotly.com/python/). The plots are interactive: hover over a curve or a measurement point to see the values.

| Script | What it plots |
|--------|---------------|
| [`plot_resistance.py`](./example_plots/plot_resistance.py) | Total model resistance $R_{TM}$ vs. model speed, and total full-scale resistance $R_{TS}$ vs. ship speed. Both loading conditions (WL1 and DWL) are shown in the same plot |
| [`plot_open_water.py`](./example_plots/plot_open_water.py) | Open water diagram of the propeller P1608: $K_T$, $10 K_Q$ and $\eta_0$ vs. $J$. $\eta_0$ is left out at $J$ = 1.1, where it has no physical meaning |
| [`plot_wake.py`](./example_plots/plot_wake.py) | Nominal wake field in the propeller plane, one plot per loading condition. The axial wake is shown as color contours, using the same color range for both conditions. The in-plane (tangential and radial) wake is shown as vectors. The view and the vector directions follow the wake figures in the report: 0° at the top, 90° (starboard) to the right, positive $w_t$ towards increasing angle and positive $w_r$ outwards. The contours are linearly interpolated between the measurement points. Hover over a measurement point to see the measured values |
| [`plot_all.py`](./example_plots/plot_all.py) | Makes all the plots above and writes them to a single file, `sobc1_calm_water_results.html`, which is opened in the web browser |
| [`common.py`](./example_plots/common.py) | Paths to the data, colors and plot styling shared by the scripts |

### How to run the scripts
The scripts need Python 3.10 or newer, and the packages `numpy`, `pandas` and `plotly`. Run the commands below in a terminal, from the `example_plots` folder.

#### With uv

```
uv run plot_all.py
```

The first time, uv reads the `pyproject.toml` file in the folder, creates a virtual environment in `.venv` and installs the packages. After that, the scripts start right away. There is no need to activate the virtual environment. The other scripts are run in the same way, e.g. `uv run plot_wake.py`.

#### With pip
Create a virtual environment and install the packages (only needed once):

```
python -m venv .venv
.venv\Scripts\activate            # Windows
source .venv/bin/activate         # macOS and Linux
pip install numpy pandas plotly
```

Then run the scripts with the virtual environment active:

```
python plot_all.py
```

In a new terminal, activate the virtual environment again before running the scripts.

#### What to expect
- `plot_all.py` writes all the plots to `sobc1_calm_water_results.html` in the `example_plots` folder, and opens it in your web browser. The file can be opened again later, or shared, without running Python.
- `plot_resistance.py`, `plot_open_water.py` and `plot_wake.py` open their plots directly in the web browser, without writing a file.

## Description of the resistance tables

### Scaling method
The hull model was towed at constant speeds and the total resistance measured. The model results are converted to full scale with the ITTC-57 form factor method (Appendix A in the report):

Model:

$$C_{TM} = \frac{R_{TM}}{\frac{1}{2}\rho_m V_M^2 S_m} = C_{FM}(1+k) + C_R + C_{AAM} + C_{BDM} + C_{AppM}$$

Ship:

$$C_{TS} = C_R + (C_{FS} + \Delta C_F)(1+k) + C_A + C_{AAS} + C_{BDS} + C_{AppS}$$

where $C_F = 0.075 / (\log_{10} R_n - 2)^2$ is the ITTC-57 friction line, the residuary resistance coefficient $C_R$ is assumed equal in model and full scale, and $\Delta C_F$ is the roughness allowance. All coefficients are made non-dimensional using the wetted surface $S$ of the hull. The ship values are for trial condition: a clean hull in calm sea water at 15 °C with density 1025.87 kg/m³.

### Model resistance (`*_model_resistance.csv`, E-5.1 / E-7.1)

| Column | Description |
|--------|-------------|
| `VS [knots]` | Full-scale ship speed |
| `VM [m/s]` | Model speed |
| `FN [-]` | Froude number, based on LWL |
| `RNM*10^-6 [-]` | Model Reynolds number |
| `RTM [N]` | Measured total model resistance |
| `CTM*10^3 [-]` | Total model resistance coefficient |
| `CFM*10^3 [-]` | Model frictional resistance coefficient (ITTC-57) |
| `CAppM*10^3 [-]` | Model appendage resistance coefficient |
| `CBDM*10^3 [-]` | Model transom stern resistance coefficient |
| `CR*10^3 [-]` | Residuary resistance coefficient |

### Appendage resistance, model (`*_model_appendage_resistance.csv`, E-5.2 / E-7.2) and ship (`*_ship_appendage_resistance.csv`, E-5.3 / E-7.3)
Appendage resistance coefficients, calculated for each appendage from its local Reynolds number, form factor and wake fraction (Appendix B in the report). The report has slots for six appendages. Only number 1 (bilge keels) is in use, so columns 2 to 6 are zero. The bilge keels are only present in full scale, so all model values are zero.

| Column | Description |
|--------|-------------|
| `VS [knots]` | Full-scale ship speed |
| `VM [m/s]` | Model speed |
| `CAppM1*10^3 [-]` ... `CAppM6*10^3 [-]` | Model resistance coefficient of appendage 1 to 6 |
| `CAppM*10^3 [-]` | Total model appendage resistance coefficient |
| `CAppS1*10^3 [-]` ... `CAppS6*10^3 [-]` | Full-scale resistance coefficient of appendage 1 to 6 |
| `CAppS*10^3 [-]` | Total full-scale appendage resistance coefficient |

### Ship resistance coefficients (`*_ship_resistance_coefficients.csv`, E-5.4 / E-7.4)

| Column | Description |
|--------|-------------|
| `VS [knots]` | Full-scale ship speed |
| `VM [m/s]` | Model speed |
| `FN [-]` | Froude number, based on LWL |
| `RNS*10^-9 [-]` | Full-scale Reynolds number |
| `CR*10^3 [-]` | Residuary resistance coefficient (same as in model scale) |
| `CFS*10^3 [-]` | Full-scale frictional resistance coefficient (ITTC-57) |
| `CVS*10^3 [-]` | Full-scale viscous resistance coefficient, $(C_{FS} + \Delta C_F)(1+k)$ |
| `CBDS*10^3 [-]` | Full-scale transom stern resistance coefficient |
| `CAppS*10^3 [-]` | Full-scale appendage resistance coefficient |
| `CTS*10^3 [-]` | Total full-scale resistance coefficient |

The total is $C_{TS} = C_R + C_{VS} + C_A + C_{AAS} + C_{BDS} + C_{AppS}$. The constants $C_A$ and $C_{AAS}$ are not columns in the table and are found in `main_particulars.json`.

### Ship resistance (`*_ship_resistance.csv`, E-5.5 / E-7.5)

| Column | Description |
|--------|-------------|
| `VS [knots]` | Full-scale ship speed |
| `VM [m/s]` | Model speed |
| `FN [-]` | Froude number, based on LWL |
| `RTS [kN]` | Total full-scale resistance, $R_{TS} = C_{TS} \frac{1}{2}\rho_s V_S^2 S_s$ |
| `PE [kW]` | Effective power, $P_E = R_{TS} V_S$ |
| `CADX [-]` | Merit (Admiralty) coefficient, $C_{ADX} = \nabla^{2/3} V^3 / P_E$. The report values match volume displacement in m³, speed in m/s and $P_E$ in kW |
| `Trim [deg]` | Dynamic trim, measured in the model test. Positive means bow up (trim by the stern) |
| `Sinkage AP [m]` | Dynamic sinkage at AP, full scale. Negative means downwards |
| `Sinkage FP [m]` | Dynamic sinkage at FP, full scale. Negative means downwards |

The sign of trim was checked against the sinkage columns: Trim ≈ (Sinkage FP − Sinkage AP) / LPP.

## Description of the open water table (`open_water/P1608_open_water.csv`, E-4.1)
The propeller model P1608 was driven by a dynamometer at a constant rate of revolution, $n$ = 14.0 Hz, while the advance speed was varied (Appendix D in the report). The results are in model scale, with no scaling applied. The average Reynolds number at 0.7R was $0.41 \cdot 10^6$. The propeller particulars are found in `main_particulars.json`.

| Column | Description |
|--------|-------------|
| `J [-]` | Advance coefficient, $J = V_A / (n D)$ |
| `KT [-]` | Thrust coefficient, $K_T = T / (\rho n^2 D^4)$ |
| `KQ [-]` | Torque coefficient, $K_Q = Q / (\rho n^2 D^5)$ |
| `eta0 [-]` | Open water efficiency, $\eta_0 = J K_T / (2 \pi K_Q)$ |
| `KT/J^2 [-]` | Thrust loading. Empty for $J = 0$, where it is undefined |

Note: at $J$ = 1.1, both $K_T$ and $K_Q$ are negative, so the reported $\eta_0$ = 4.780 has no physical meaning.

## Description of the wake tables
The nominal wake in the propeller plane was measured at 15 knots (full scale) for both loading conditions, with a five-hole spherical pitot tube attached to the propeller boss (Appendix F in the report). The measuring plane is perpendicular to the propeller shaft, and intersects the generator line of the propeller blade at 0.7R. All values are non-dimensionalised by the carriage speed $V$:

- Axial (Taylor) wake: $w_{ax} = 1 - V_A / V$, where $V_A$ is the axial velocity
- Tangential wake: $w_t = V_T / V$
- Radial wake: $w_r = V_R / V$

The angular position is 0 deg at the top vertical position, and 90 deg is to the starboard side. The radial position is given as $r/R_0$, where $R_0$ is the propeller radius. The wake was measured at $r/R_0$ = 0.398, 0.503, 0.702, 0.901 and 1.100.

### Wake measurements (`*_wake_measurements.csv`, E-9.1–E-9.2 / E-10.1–E-10.2)
In the report, the measurements are a wide table with one block of columns per radius, split over two pages. In the CSV files, they are stored in long format with one row per measurement point, sorted by radius and then by angle. The angle 360 deg is a repetition of 0 deg, as in the report.

| Column | Description |
|--------|-------------|
| `r/R0 [-]` | Radial position, relative to the propeller radius |
| `angle [deg]` | Angular position, 0 deg at top, 90 deg to starboard |
| `w_ax [-]` | Axial wake |
| `w_t [-]` | Tangential wake |
| `w_r [-]` | Radial wake |

### Mean wake (`*_wake_mean_values.csv`, E-9.1–E-9.2 / E-10.1–E-10.2)
The `Mean=` row at the bottom of each measurement table in the report, i.e. the circumferential mean of each wake component at each radius. The values match a trapezoidal integration of the measurements over the angle, divided by 360 deg. Since the angles are not evenly spaced, this differs from a simple average of the rows.

| Column | Description |
|--------|-------------|
| `r/R0 [-]` | Radial position, relative to the propeller radius |
| `w_ax mean [-]` | Mean axial wake |
| `w_t mean [-]` | Mean tangential wake |
| `w_r mean [-]` | Mean radial wake |

### Harmonic analysis (`*_wake_harmonics_{axial,radial,tangential}.csv`, E-9.8–E-9.16 / E-10.8–E-10.16)
For each radius, the circumferential variation of each wake component is expressed as a Fourier series (Appendix G in the report):

$$w(\phi) = A(0) + \sum_{i=1}^{\infty} \left[A(i) \cos i\phi + B(i) \sin i\phi \right] = A(0) + \sum_{i=1}^{\infty} C(i) \cos\left[i\phi - \alpha(i)\right]$$

where $C = \sqrt{A^2 + B^2}$ and $\alpha = \arctan(B/A)$. The report gives harmonic orders 1 to 14.

| Column | Description |
|--------|-------------|
| `r/R0 [-]` | Radial position. Rounded to two decimals in the report: 0.40, 0.50, 0.70, 0.90 and 1.10 correspond to the measured radii 0.398, 0.503, 0.702, 0.901 and 1.100 |
| `order i [-]` | Harmonic order. Order 0 holds the mean value $A(0)$ (`MEAN VALUE` in the report). B, C and phase are empty for this row |
| `A [-]` | Cosine amplitude $A(i)$ |
| `B [-]` | Sine amplitude $B(i)$ |
| `C [-]` | Amplitude $C(i)$ |
| `phase alpha [deg]` | Phase angle $\alpha(i)$, in the range 0 to 360 deg |

The mean value $A(0)$ from the harmonic analysis differs slightly from the mean values in the measurement tables (by up to about 0.015). The report does not say how the harmonic analysis interpolates between the measured angles, which is the likely cause. Both are given as in the report.
