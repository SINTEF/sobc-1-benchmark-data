'''
Shared paths and plot styling for the example scripts.
'''

from pathlib import Path

DATA_FOLDER = Path(__file__).resolve().parent.parent

RESISTANCE_FOLDER = DATA_FOLDER / "resistance_data"
OPEN_WATER_FOLDER = DATA_FOLDER / "open_water"
WAKE_FOLDER = DATA_FOLDER / "wake_data"

LOADING_CONDITIONS = {
    "WL1": "WL1 - ballast, T<sub>AP</sub>/T<sub>FP</sub> = 7.5/5.4 m",
    "DWL": "DWL - design, T<sub>AP</sub>/T<sub>FP</sub> = 11.0/11.0 m",
}

# Categorical colors, in fixed order. The same loading condition always gets the same color.
COLORS = ["#2a78d6", "#eb6834", "#1baf7a"]
CONDITION_COLORS = {"WL1": COLORS[0], "DWL": COLORS[1]}

TEXT_PRIMARY = "#0b0b0b"
TEXT_SECONDARY = "#52514e"
GRID_COLOR = "#e4e3df"
SURFACE = "#fcfcfb"

# Sequential one-hue ramp (light -> dark) used for the axial wake. High wake = dark.
SEQUENTIAL_BLUE = [
    "#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec", "#5598e7", "#3987e5",
    "#2a78d6", "#256abf", "#1c5cab", "#184f95", "#104281", "#0d366b",
]


def apply_style(fig, title, x_title, y_title):
    '''Common layout for all line plots'''
    fig.update_layout(
        title=dict(text=title, font=dict(size=18, color=TEXT_PRIMARY)),
        template="plotly_white",
        paper_bgcolor=SURFACE,
        plot_bgcolor=SURFACE,
        font=dict(color=TEXT_SECONDARY),
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
        margin=dict(t=100),
        height=500,
    )
    fig.update_xaxes(title=x_title, gridcolor=GRID_COLOR, zeroline=False, showline=True, linecolor=TEXT_SECONDARY)
    fig.update_yaxes(title=y_title, gridcolor=GRID_COLOR, zeroline=False, showline=True, linecolor=TEXT_SECONDARY)

    return fig
