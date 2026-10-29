'''
Example showing how to load and plot the calm water resistance, in model scale and full scale, for
both loading conditions (WL1 and DWL).
'''

import pandas as pd
import plotly.graph_objects as go

from common import RESISTANCE_FOLDER, LOADING_CONDITIONS, CONDITION_COLORS, apply_style


def resistance_figure(file_suffix, x_column, y_column, title, x_title, y_title):
    fig = go.Figure()

    for condition, label in LOADING_CONDITIONS.items():
        df = pd.read_csv(RESISTANCE_FOLDER / f"{condition}_{file_suffix}.csv")

        fig.add_trace(go.Scatter(
            x=df[x_column],
            y=df[y_column],
            name=label,
            mode="lines+markers",
            line=dict(color=CONDITION_COLORS[condition], width=2),
            marker=dict(size=8, line=dict(color="white", width=2)),
            customdata=df["VS [knots]"],
            hovertemplate="%{y:.2f} (V<sub>S</sub> = %{customdata:.1f} kn)",
        ))

    return apply_style(fig, title, x_title, y_title)


def model_resistance_figure():
    '''Measured total resistance of the model, as a function of model speed'''
    return resistance_figure(
        file_suffix="model_resistance",
        x_column="VM [m/s]",
        y_column="RTM [N]",
        title="Model scale resistance (scale 1:32)",
        x_title="Model speed, V<sub>M</sub> [m/s]",
        y_title="Total model resistance, R<sub>TM</sub> [N]",
    )


def full_scale_resistance_figure():
    '''Predicted total resistance of the ship, as a function of ship speed'''
    return resistance_figure(
        file_suffix="ship_resistance",
        x_column="VS [knots]",
        y_column="RTS [kN]",
        title="Full scale resistance (trial condition)",
        x_title="Ship speed, V<sub>S</sub> [knots]",
        y_title="Total ship resistance, R<sub>TS</sub> [kN]",
    )


if __name__ == "__main__":
    model_resistance_figure().show()
    full_scale_resistance_figure().show()
