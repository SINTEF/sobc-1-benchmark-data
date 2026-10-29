# Model propulsion tests in head and following waves (2025)

## Introduction
This folder contains the results from the following paper:

> Steen, S., Portillo-Juan, A., Saettone, S. (2025): *Model propulsion tests in head and following waves of a bulk carrier*. Applied Ocean Research, Volume 154, 104405. [DOI](https://doi.org/10.1016/j.apor.2024.104405), [Link](https://www.sciencedirect.com/science/article/pii/S0141118724005261)

The paper is open access. Please see it for a full description of the test setup, the analysis and a discussion of the results. A short summary is given below, followed by a description of the data files.

The data includes the tables in the paper, and the data behind the figures: the results for each run, the load-variation results, the propeller open water curve and the measured waves.

## Test setup
Self-propulsion tests were performed in calm water and in regular head and following waves, in the large towing tank at the Marine Technology Centre in Trondheim (250 x 10.5 x 5 m). The hull model was a 1:32 scale model of SOBC-1, loaded to the design waterline (draught 11.0 m in full scale), with a 4-bladed propeller with diameter 210.9 mm. See [`main_particulars.json`](./main_particulars.json) for the main particulars of the ship and propeller, and the [2021 calm water tests](./../2021%20-%20calm%20water%20resistance%20and%20propulsion/) for more details on the hull model.

- **Connection to the carriage:** the model was towed with a stiff spring arrangement (natural period in surge 15.6 s in model scale), free to heave and pitch. The tow force $F_D$ was measured by two force transducers.
- **Speeds:** 0.773, 1.000, 1.364 and 1.500 m/s in model scale, corresponding to $F_n$ = 0.099, 0.129, 0.176 and 0.193 (based on $L_{WL}$).
- **Waves:** 21 regular waves with wave length to ship length ratio $\lambda/L_{PP}$ from 0.2 to 2.0 and constant steepness $H/\lambda$ = 1/40, in both head and following waves.
- **Propeller loading:** for calm water at all speeds, and for waves 8051, 8110, 8160 and 8210 at 1.364 m/s, the propeller loading was varied in three steps: zero thrust, the full-scale propulsion point, and zero tow force (the model-scale propulsion point). The other conditions were tested at (approximately) the full-scale propulsion point. In waves, it was difficult to hit the propulsion point exactly, as the tow force varied strongly with time.
- **Speed variation:** waves 8004, 8051, 8110, 8160 and 8210 were tested at all four speeds. The other waves were only tested at 1.364 m/s.
- **Repeatability:** wave 8051 at 1.364 m/s was repeated five times in both head and following waves, to estimate the precision errors (Table 4).

### Conventions
- Coordinate system: right-handed, fixed in the moving towing carriage, with $x$ positive towards the bow, $y$ towards starboard and $z$ downwards. Wave elevation is positive up.
- Heading: 180° is head waves and 0° is following waves.
- Wave IDs follow Table 3 in the paper. In the original data files, the last digit of some wave IDs differs from the paper (e.g. 8050 instead of 8051). These have been changed to the IDs used in the paper. The first three digits identify each wave uniquely.

## Files

| File | Content | In paper |
|------|---------|----------|
| [`main_particulars.json`](./main_particulars.json) | Main particulars of ship and propeller, test setup, and constants used in the analysis | Tables 1 and 2 |
| [`tables/table_3_waves.csv`](./tables/table_3_waves.csv) | Nominal wave parameters | Table 3 |
| [`tables/table_4_precision_errors.csv`](./tables/table_4_precision_errors.csv) | Precision errors for wave 8051 | Table 4 |
| [`data/open_water.csv`](./data/open_water.csv) | Open water curve of the model propeller | Fig. 3 |
| [`data/wave_calibration.csv`](./data/wave_calibration.csv) | Nominal and measured wave parameters, and encounter frequencies | - |
| [`data/self_propulsion_runs.csv`](./data/self_propulsion_runs.csv) | Measured and derived results for each run (112 runs) | Figs. 5-7 and 10-28 |
| [`data/load_variation.csv`](./data/load_variation.csv) | Results from the conditions with varied propeller loading: thrust deduction, and resistance at zero thrust | Figs. 8, 9 and 11 |

All files are comma-separated, with one header row, and the unit in square brackets in the column names. All values in `data/` are in **model scale**. Values are given with up to 7 significant digits.

### Which data to use for the figures in the paper

| Figure | Content | File and columns |
|--------|---------|------------------|
| 3 | Open water diagram | `data/open_water.csv` |
| 5-7 | $F_D$ vs. $T$ | `data/self_propulsion_runs.csv`: `FD [N]`, `T [N]` |
| 8 | $1-t$ with precision error | `data/load_variation.csv`: `1-t [-]`, `1-t precision error [-]` |
| 9 | $C_{AW}$ from linear extrapolation to zero thrust | `data/load_variation.csv`: `CAW extrapolated [-]` |
| 10 | $C_{AW}$ using the thrust deduction fraction | `data/self_propulsion_runs.csv`: `CAW from t [-]` |
| 11 | $C_{TAW}$ from linear extrapolation to zero thrust | `data/load_variation.csv`: `CTAW extrapolated [-]` |
| 12 | $C_{TAW}$ using the thrust deduction fraction | `data/self_propulsion_runs.csv`: `CTAW from t [-]` |
| 13 | Difference between $C_{TAW}$ and $C_{AW}$ | `data/self_propulsion_runs.csv`: `CTAW from t [-]` - `CAW from t [-]` |
| 14, 15 | $K_T$ and $K_Q$ | `data/self_propulsion_runs.csv`: `KT [-]`, `KQ [-]` |
| 16 | $K_Q$ with amplitude | `data/self_propulsion_runs.csv`: `KQ [-]`, `KQ amplitude [-]` |
| 17, 18 | $J$ with amplitude | `data/self_propulsion_runs.csv`: `J [-]`, `J amplitude [-]` |
| 19, 20 | Effective wake fraction | `data/self_propulsion_runs.csv`: `w [-]` (and `KT [-]` for Fig. 20) |
| 21-24 | $\eta_0$, $\eta_H$, $\eta_R$ and $\eta_D$ | `data/self_propulsion_runs.csv`: `eta0 [-]`, `etaH [-]`, `etaR [-]`, `etaD [-]` |
| 25-27 | Heave, pitch and surge RAOs | `data/self_propulsion_runs.csv`: `RAO heave [-]`, `RAO pitch [-]`, `RAO surge [-]` |
| 28 | Surge velocity amplitude | `data/self_propulsion_runs.csv`: `surge velocity amplitude [m/s]` |

The figures are plotted against $\lambda/L_{PP}$, which is the column `lambda/LPP [-]`. Most figures show the runs at the propulsion point (`loading` = `propulsion point`), with the status `OK` or `OK - REP`.

## Example plot
The folder [`example_plots`](./example_plots/) contains a `Python` script, [`plot_added_thrust.py`](./example_plots/plot_added_thrust.py), that shows how to load the data and plot the wave added thrust coefficient $C_{TAW}$ as a function of $\lambda/L_{PP}$, for head and following waves at 1.364 m/s (as in Fig. 12). It uses [Pandas](https://pandas.pydata.org/) and [Plotly](https://plotly.com/python/), and the plot opens in the web browser. Each marker is one run, and the line goes through the mean value for each wave. The same approach can be used for the other quantities in `data/self_propulsion_runs.csv`, by changing the column name.

The script needs Python 3.10 or newer, and the packages `numpy`, `pandas` and `plotly`. Run the commands below in a terminal, from the `example_plots` folder.

With uv:

```
uv run plot_added_thrust.py
```

With pip, create a virtual environment and install the packages (only needed once):

```
python -m venv .venv
.venv\Scripts\activate            # Windows
source .venv/bin/activate         # macOS and Linux
pip install numpy pandas plotly
```

Then run the script with the virtual environment active:

```
python plot_added_thrust.py
```

## Description of the files

### `tables/table_3_waves.csv` (Table 3)
The nominal parameters of the 21 regular waves, in full scale and model scale. The wave length is the deep-water wave length, $\lambda = g T^2 / (2\pi)$. The column `tested at all speeds` marks the waves that are in bold type in the paper, which were tested at all four speeds. Note that the measured waves differ somewhat from the nominal values, see `data/wave_calibration.csv`.

### `tables/table_4_precision_errors.csv` (Table 4)
Precision errors for wave 8051 at 1.364 m/s, from five repeated runs, in percent of the mean value. With $t_s$ the two-tailed Student's t-distribution value for N-1 degrees of freedom and 95% probability, $S_x$ the standard deviation of the repeated measurements, $N$ = 5 the number of measurements and $M$ the mean value:

$$e_{ss} = \frac{t_s S_x}{M}, \qquad e_{sm} = \frac{t_s S_x}{\sqrt{N} M}$$

### `data/open_water.csv` (Fig. 3)
Open water curve of the model propeller, measured at a constant propeller speed of 7.3 Hz (average Reynolds number $2.1 \cdot 10^5$). The open water curve from calm water is used to find $J$, $K_{Q0}$ and $\eta_0$ in waves, by thrust identity.

| Column | Description |
|--------|-------------|
| `J [-]` | Advance ratio, $J = V_A / (n D)$ |
| `KT [-]` | Thrust coefficient, $K_T = T / (\rho n^2 D^4)$ |
| `KQ [-]` | Torque coefficient, $K_Q = Q / (\rho n^2 D^5)$ |
| `eta0 [-]` | Open water efficiency, $\eta_0 = J K_T / (2\pi K_Q)$ |
| `KT/J^2 [-]` | Thrust loading. Empty for $J$ = 0 |

### `data/wave_calibration.csv`
Nominal and measured (calibrated) wave height and period for each wave. The analysis in the paper uses the measured values. The wave length, steepness and $\lambda/L_{PP}$ are computed from the measured period.

| Column | Description |
|--------|-------------|
| `wave_id` | Wave ID, as in Table 3 |
| `H nominal ... [m]`, `H measured ... [m]` | Nominal and measured wave height, full scale and model scale |
| `T nominal ... [s]`, `T measured ... [s]` | Nominal and measured wave period, full scale and model scale |
| `lambda full scale [m]`, `lambda model scale [m]` | Deep-water wave length, from the measured period |
| `H/lambda [-]` | Wave steepness, from the measured height and period |
| `lambda/LPP [-]` | Wave length to ship length ratio, with $L_{PP}$ = 190 m |
| `c model scale [m/s]` | Wave phase velocity |
| `fe head V=... [Hz]`, `fe following V=... [Hz]` | Encounter frequency in model scale, for each speed. Negative values in following waves mean that the ship is faster than the waves |

### `data/self_propulsion_runs.csv`
One row for each run. The derived quantities were computed by the authors from the measured values, as described in the paper. All values are time averages over the run, except the amplitudes.

**Identification of the run:**

| Column | Description |
|--------|-------------|
| `run` | Run number. 1xxx is calm water, 2xxx is head waves and 3xxx is following waves |
| `status` | `OK`, `OK - REP` (repetition runs for the uncertainty analysis), or `NOT OK` (runs 3152 and 3153, which should not be used) |
| `condition` | `calm`, `head` or `following` |
| `heading [deg]` | 180 for head waves, 0 for following waves. Calm water runs have the heading of the test series they belong to |
| `wave_id` | Wave ID, as in Table 3. Empty for calm water |
| `loading` | Propeller loading: `propulsion point` (full-scale propulsion point), `zero thrust` or `zero tow force` (model-scale propulsion point). For the calm water runs, this is inferred from the measured thrust and tow force. For runs in waves, it is from the test log |
| `V nominal [m/s]` | Nominal model speed |
| `V [m/s]` | Measured model speed |
| `Fn [-]` | Froude number |
| `wave T [s]`, `wave H [m]` | Measured wave period and height (model scale, from the wave calibration) |
| `lambda/LPP [-]` | Wave length to ship length ratio, from the measured period |
| `k [1/m]` | Wave number |

**Measured values:**

| Column | Description |
|--------|-------------|
| `n [rps]` | Propeller rotational speed |
| `T [N]` | Propeller thrust |
| `Q [Nm]` | Propeller torque |
| `FD [N]` | Tow force |
| `T amplitude [N]`, `Q amplitude [Nm]`, `n amplitude [rps]`, `FD amplitude [N]` | Amplitudes in waves |
| `wave 10m T [s]`, `wave 10m H [m]` | Wave period and height measured in the run, with the stationary wave probe 10 m from the wave maker |
| `wave carriage 1 T [s]`, `wave carriage 1 H [m]`, `wave carriage 2 T [s]`, `wave carriage 2 H [m]` | Wave period (encounter period) and height measured with the two wave probes on the carriage |
| `heave amplitude [m]`, `pitch amplitude [deg]`, `surge amplitude [m]`, `surge velocity amplitude [m/s]` | Motion amplitudes in waves |
| `RAO heave [-]`, `RAO pitch [-]`, `RAO surge [-]` | Response amplitude operators. Heave and surge: motion amplitude divided by the wave amplitude. Pitch: pitch amplitude (in radians) divided by $k \zeta_a$. The wave amplitude $\zeta_a$ is from the wave probe 10 m from the wave maker |

The amplitudes are from the authors' post-processing of the time series.

**Resistance and added resistance:**

| Column | Description |
|--------|-------------|
| `R from t [N]` | Resistance, $R = T (1-t) + F_D$, using the thrust deduction fraction in `t used [-]` |
| `T from R from t [N]` | Thrust at the self-propulsion point, $R / (1-t)$ |
| `RAW from t [N]` | Added resistance in waves, $R - R_{calm}$ |
| `TAW from t [N]` | Added thrust in waves, $T - T_{calm}$, using `T from R from t` |
| `CAW from t [-]` | Added resistance coefficient, $C_{AW} = R_{AW} / (\rho g \zeta_a^2 B^2 / L_{PP})$ |
| `CTAW from t [-]` | Added thrust coefficient, $C_{TAW} = T_{AW} / (\rho g \zeta_a^2 B^2 / L_{PP})$ |

The calm water values $R_{calm}$ and $T_{calm}$ are from the calm water runs 1002, 1010, 1020 and 1030 at the same speed, for both head and following waves. In $C_{AW}$ and $C_{TAW}$, the wave amplitude $\zeta_a$ is half the measured wave height (`wave H [m]`), and the values $B$ = 1.009375 m (32.3 m in full scale) and $L_{PP}$ = 5.9375 m are used.

**Propulsive coefficients:**

| Column | Description |
|--------|-------------|
| `J geometric [-]` | $V / (n D)$ |
| `J [-]` | Advance ratio from thrust identity: $J$ that gives the measured $K_T$ in the open water curve |
| `J amplitude [-]` | Amplitude of $J$ |
| `KT [-]`, `KT amplitude [-]` | Thrust coefficient and its amplitude |
| `KQ [-]`, `KQ amplitude [-]` | Torque coefficient and its amplitude |
| `KQ0 [-]` | Open water torque coefficient at `J [-]` |
| `t used [-]` | Thrust deduction fraction used for this run (see below) |
| `w [-]` | Effective wake fraction, $w = 1 - J / J_{geometric}$ |
| `eta0 [-]` | Open water efficiency, $\eta_0 = J K_T / (2\pi K_{Q0})$ |
| `etaH [-]` | Hull efficiency, $\eta_H = (1-t)/(1-w)$ |
| `etaR [-]` | Relative-rotative efficiency, $\eta_R = K_{Q0} / K_Q$ |
| `etaB [-]` | Propeller efficiency behind the ship, $\eta_B = \eta_0 \eta_R$ |
| `etaD [-]` | Propulsive efficiency, $\eta_D = \eta_H \eta_0 \eta_R$ |
| `CTh [-]` | Thrust loading coefficient, $C_{Th} = 8 K_T / (\pi J^2)$ |

The thrust deduction fraction is found from the linear relation between tow force and thrust, for the conditions with varied propeller loading (see `data/load_variation.csv`). For calm water and for the waves with varied loading (8051, 8110, 8160 and 8210 at 1.364 m/s), `t used` is the value found for that condition. For all other runs in waves, it is the average of the values found in waves with the same heading: 0.1075 in head waves and 0.1044 in following waves.

All the relations given in the tables above have been checked against the values in the file.

### `data/load_variation.csv` (Figs. 8, 9 and 11)
One row for each condition where the propeller loading was varied: the five calm water conditions and seven wave conditions.

| Column | Description |
|--------|-------------|
| `condition`, `heading [deg]`, `V nominal [m/s]`, `wave_id`, `lambda/LPP [-]` | The condition |
| `runs` | The runs used, separated by `;` |
| `t [-]`, `1-t [-]` | Thrust deduction fraction, from the slope of the linear fit of $F_D$ vs. $T$: $t = (T - F_D - F_{D,T=0})/T$ |
| `1-t precision error [-]` | Precision error of $1-t$, shown as error bars in Fig. 8 |
| `R extrapolated [N]` | Resistance, found as the tow force at zero thrust by linear extrapolation |
| `T extrapolated [N]` | Thrust at the self-propulsion point, $R / (1-t)$ |
| `RAW extrapolated [N]`, `TAW extrapolated [N]` | Added resistance and added thrust |
| `CAW extrapolated [-]`, `CTAW extrapolated [-]` | Added resistance and added thrust coefficients |
