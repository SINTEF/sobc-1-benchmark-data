'''
Example showing how to load and plot the wave added thrust coefficient, CTAW, as a function of the
wave length to ship length ratio, for head and following waves at a model speed of 1.364 m/s
(Fig. 12 in the paper).

Each marker is one run. The repeated runs in wave 8051 are shown as separate markers, and the line
goes through the mean value for each wave.
'''

from pathlib import Path

import pandas as pd
import plotly.graph_objects as go

DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"

SPEED = 1.364 # Model speed [m/s]. Other speeds (0.773, 1.0 and 1.5) are only tested in a few waves

# Categorical colors, in fixed order
CONDITIONS = {
    "head": ("Head waves", "#2a78d6"),
    "following": ("Following waves", "#eb6834"),
}

TEXT_PRIMARY = "#0b0b0b"
TEXT_SECONDARY = "#52514e"
GRID_COLOR = "#e4e3df"
SURFACE = "#fcfcfb"


def added_thrust_figure(speed=SPEED):
    df = pd.read_csv(DATA_FOLDER / "self_propulsion_runs.csv")

    # Only valid runs at the propulsion point, at the selected speed
    df = df[
        (df["V nominal [m/s]"] == speed)
        & (df["loading"] == "propulsion point")
        & (df["status"].isin(["OK", "OK - REP"]))
        & (df["condition"] != "calm")
    ]

    fig = go.Figure()

    for condition, (label, color) in CONDITIONS.items():
        runs = df[df["condition"] == condition].sort_values("lambda/LPP [-]")
        mean = runs.groupby("lambda/LPP [-]", as_index=False)["CTAW from t [-]"].mean()

        fig.add_trace(go.Scatter(
            x=mean["lambda/LPP [-]"],
            y=mean["CTAW from t [-]"],
            name=label,
            legendgroup=condition,
            mode="lines",
            line=dict(color=color, width=2),
            hoverinfo="skip",
        ))

        fig.add_trace(go.Scatter(
            x=runs["lambda/LPP [-]"],
            y=runs["CTAW from t [-]"],
            name=label,
            legendgroup=condition,
            showlegend=False,
            mode="markers",
            marker=dict(size=8, color=color, line=dict(color="white", width=2)),
            customdata=runs[["run", "wave_id"]],
            hovertemplate=(
                f"{label}<br>"
                "λ/L<sub>PP</sub> = %{x:.2f}<br>"
                "C<sub>TAW</sub> = %{y:.2f}<br>"
                "Run %{customdata[0]}, wave %{customdata[1]}<extra></extra>"
            ),
        ))

        # Direct label at the end of each curve, so the curves are not identified by color alone
        fig.add_annotation(
            x=mean["lambda/LPP [-]"].iloc[-1], y=mean["CTAW from t [-]"].iloc[-1],
            text=label, showarrow=False, xanchor="left", xshift=10, font=dict(size=13, color=TEXT_SECONDARY),
        )

    fig.update_layout(
        title=dict(
            text=f"Wave added thrust coefficient, V = {speed} m/s (model scale)",
            font=dict(size=18, color=TEXT_PRIMARY),
        ),
        template="plotly_white",
        paper_bgcolor=SURFACE,
        plot_bgcolor=SURFACE,
        font=dict(color=TEXT_SECONDARY),
        hovermode="closest",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
        margin=dict(t=100, r=140),
        height=500,
    )
    fig.update_xaxes(
        title="Wave length to ship length ratio, λ/L<sub>PP</sub> [-]",
        gridcolor=GRID_COLOR, zeroline=False, showline=True, linecolor=TEXT_SECONDARY,
    )
    fig.update_yaxes(
        title="Added thrust coefficient, C<sub>TAW</sub> [-]",
        gridcolor=GRID_COLOR, zeroline=True, zerolinecolor="#a3a29d", showline=True, linecolor=TEXT_SECONDARY,
    )

    return fig


if __name__ == "__main__":
    added_thrust_figure().show()
