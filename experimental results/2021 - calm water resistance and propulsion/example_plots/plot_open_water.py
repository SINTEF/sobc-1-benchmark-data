'''
Example showing how to load and plot the open water characteristics of the propeller P1608.
'''

import pandas as pd
import plotly.graph_objects as go

from common import OPEN_WATER_FOLDER, COLORS, apply_style


def open_water_figure():
    df = pd.read_csv(OPEN_WATER_FOLDER / "P1608_open_water.csv")

    # The efficiency has no physical meaning when the thrust and torque are negative
    valid_efficiency = (df["KT [-]"] > 0) & (df["KQ [-]"] > 0)

    curves = [
        ("K<sub>T</sub>", df["J [-]"], df["KT [-]"]),
        ("10 K<sub>Q</sub>", df["J [-]"], 10 * df["KQ [-]"]),
        ("η<sub>0</sub>", df["J [-]"][valid_efficiency], df["eta0 [-]"][valid_efficiency]),
    ]

    fig = go.Figure()

    for i, ((name, x, y), color) in enumerate(zip(curves, COLORS)):
        fig.add_trace(go.Scatter(
            x=x,
            y=y,
            name=name,
            mode="lines+markers",
            line=dict(color=color, width=2),
            marker=dict(size=8, line=dict(color="white", width=2)),
            hovertemplate="%{y:.3f}",
        ))

        # Direct labels, so the curves are not identified by color alone. The efficiency is labelled
        # at its maximum, as its end point is close to the end of the torque curve.
        if i == 2:
            fig.add_annotation(
                x=x.loc[y.idxmax()], y=y.max(), text=name, showarrow=False,
                yanchor="bottom", yshift=10, font=dict(size=14),
            )
        else:
            fig.add_annotation(
                x=x.iloc[-1], y=y.iloc[-1], text=name, showarrow=False,
                xanchor="left", xshift=10, font=dict(size=14),
            )

    fig = apply_style(
        fig,
        title="Open water characteristics, propeller P1608 (model scale, n = 14 Hz)",
        x_title="Advance coefficient, J [-]",
        y_title="K<sub>T</sub>, 10 K<sub>Q</sub>, η<sub>0</sub> [-]",
    )
    fig.add_hline(y=0, line=dict(color="#a3a29d", width=1))

    return fig


if __name__ == "__main__":
    open_water_figure().show()
