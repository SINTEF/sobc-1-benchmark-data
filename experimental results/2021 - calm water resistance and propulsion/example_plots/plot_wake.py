'''
Example showing how to load and plot the measured wake field in the propeller plane. The axial wake
is shown as colored contours, and the in-plane (tangential and radial) wake as vectors.

The plot uses the same convention as the figures in the report: the propeller plane is seen with 0 deg
at the top and 90 deg (starboard) to the right. Positive tangential wake points in the direction of
increasing angle, and positive radial wake points outwards.
'''

import numpy as np
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

from common import (
    WAKE_FOLDER, LOADING_CONDITIONS, SEQUENTIAL_BLUE, COLORS,
    TEXT_PRIMARY, TEXT_SECONDARY, GRID_COLOR, SURFACE,
)

VECTOR_SCALE = 0.75 # Length of the vectors, in units of propeller radius, per unit wake
AXIAL_WAKE_RANGE = (0.0, 0.8) # Same color range for all conditions, so the plots can be compared


def load_wake_grid(condition):
    '''Returns the radii, angles and wake components as 2D arrays with shape (n_radii, n_angles)'''
    df = pd.read_csv(WAKE_FOLDER / f"{condition}_wake_measurements.csv")

    radii = np.sort(df["r/R0 [-]"].unique())
    angles = np.sort(df["angle [deg]"].unique())

    df = df.sort_values(["r/R0 [-]", "angle [deg]"])
    shape = (len(radii), len(angles))

    components = {
        name: df[f"{name} [-]"].to_numpy().reshape(shape) for name in ("w_ax", "w_t", "w_r")
    }

    return radii, angles, components


def interpolate_polar(radii, angles, values, r, theta):
    '''
    Linear interpolation of values on the measurement grid, first along the angle and then along the
    radius. Points outside the measured radii are returned as NaN.
    '''
    along_angle = np.array([np.interp(theta, angles, row) for row in values])

    result = np.full(r.shape, np.nan)
    inside = (r >= radii[0]) & (r <= radii[-1])

    index = np.clip(np.searchsorted(radii, r[inside]) - 1, 0, len(radii) - 2)
    fraction = (r[inside] - radii[index]) / (radii[index + 1] - radii[index])

    columns = np.flatnonzero(inside)
    result[inside] = (1 - fraction) * along_angle[index, columns] + fraction * along_angle[index + 1, columns]

    return result


def to_cartesian(r, angle_deg):
    '''0 deg at the top, 90 deg to the right'''
    angle = np.radians(angle_deg)
    return r * np.sin(angle), r * np.cos(angle)


def circle(r, n=361):
    return to_cartesian(r, np.linspace(0, 360, n))


def wake_field_figure(condition):
    radii, angles, w = load_wake_grid(condition)

    # --- Axial wake contours, interpolated onto a cartesian grid ---
    n_grid = 301
    x_grid = np.linspace(-radii[-1], radii[-1], n_grid)
    xx, yy = np.meshgrid(x_grid, x_grid)
    r_grid = np.hypot(xx, yy).ravel()
    theta_grid = np.degrees(np.arctan2(xx, yy)).ravel() % 360

    w_ax_grid = interpolate_polar(radii, angles, w["w_ax"], r_grid, theta_grid).reshape(xx.shape)

    fig = go.Figure()

    fig.add_trace(go.Contour(
        x=x_grid, y=x_grid, z=w_ax_grid,
        colorscale=[[i / (len(SEQUENTIAL_BLUE) - 1), c] for i, c in enumerate(SEQUENTIAL_BLUE)],
        zmin=AXIAL_WAKE_RANGE[0], zmax=AXIAL_WAKE_RANGE[1],
        contours=dict(start=AXIAL_WAKE_RANGE[0], end=AXIAL_WAKE_RANGE[1], size=0.05),
        line=dict(width=0),
        colorbar=dict(title=dict(text="w<sub>ax</sub> [-]", side="top"), len=0.8),
        hoverinfo="skip",
        showlegend=False,
    ))

    # --- Measured radii and propeller disk ---
    for r in radii:
        x, y = circle(r)
        fig.add_trace(go.Scatter(
            x=x, y=y, mode="lines", line=dict(color="white", width=1),
            hoverinfo="skip", showlegend=False,
        ))

    x, y = circle(1.0)
    fig.add_trace(go.Scatter(
        x=x, y=y, mode="lines", name="Propeller disk (r/R<sub>0</sub> = 1)",
        line=dict(color=TEXT_PRIMARY, width=1.5, dash="dash"), hoverinfo="skip",
    ))

    # --- In-plane wake vectors: tangential (increasing angle) and radial (outwards) ---
    r_mesh, angle_mesh = np.meshgrid(radii, angles[:-1], indexing="ij") # skip 360 deg, same as 0 deg
    w_t = w["w_t"][:, :-1]
    w_r = w["w_r"][:, :-1]

    x0, y0 = to_cartesian(r_mesh, angle_mesh)
    theta = np.radians(angle_mesh)
    u = w_r * np.sin(theta) + w_t * np.cos(theta)
    v = w_r * np.cos(theta) - w_t * np.sin(theta)

    quiver = ff.create_quiver(
        x0.ravel(), y0.ravel(), u.ravel(), v.ravel(),
        scale=VECTOR_SCALE, arrow_scale=0.25, angle=np.radians(25),
        name="In-plane wake (w<sub>t</sub>, w<sub>r</sub>)",
        line=dict(color=COLORS[1], width=1.5),
        hoverinfo="skip",
    )
    fig.add_traces(quiver.data)

    # Reference vector, for reading the length of the vectors
    x_ref, y_ref = 0.85, -1.2
    reference = ff.create_quiver(
        [x_ref], [y_ref], [0.1], [0.0], scale=VECTOR_SCALE, arrow_scale=0.25, angle=np.radians(25),
        line=dict(color=COLORS[1], width=1.5), hoverinfo="skip", showlegend=False,
    )
    fig.add_traces(reference.data)
    fig.add_annotation(
        x=x_ref, y=y_ref, text="0.1", showarrow=False, xanchor="right", xshift=-6,
        font=dict(color=TEXT_SECONDARY),
    )

    # --- Measurement points, with all measured values in the hover text ---
    fig.add_trace(go.Scatter(
        x=x0.ravel(), y=y0.ravel(),
        mode="markers",
        name="Measurement points",
        marker=dict(size=5, color="white", line=dict(color=TEXT_PRIMARY, width=1)),
        customdata=np.stack([r_mesh.ravel(), angle_mesh.ravel(), w["w_ax"][:, :-1].ravel(), w_t.ravel(), w_r.ravel()], axis=-1),
        hovertemplate=(
            "r/R<sub>0</sub> = %{customdata[0]:.3f}, angle = %{customdata[1]:.0f}°<br>"
            "w<sub>ax</sub> = %{customdata[2]:.3f}<br>"
            "w<sub>t</sub> = %{customdata[3]:.3f}<br>"
            "w<sub>r</sub> = %{customdata[4]:.3f}<extra></extra>"
        ),
    ))

    # --- Angle labels ---
    for angle, text in [(0, "0° (top)"), (90, "90° (SB)"), (180, "180°"), (270, "270° (PS)")]:
        x, y = to_cartesian(1.27, angle)
        fig.add_annotation(x=x, y=y, text=text, showarrow=False, font=dict(color=TEXT_SECONDARY))

    fig.update_layout(
        title=dict(
            text=f"Nominal wake field at 15 knots, {LOADING_CONDITIONS[condition]}",
            font=dict(size=18, color=TEXT_PRIMARY),
        ),
        template="plotly_white",
        paper_bgcolor=SURFACE,
        plot_bgcolor=SURFACE,
        font=dict(color=TEXT_SECONDARY),
        hovermode="closest",
        legend=dict(orientation="h", yanchor="bottom", y=1.0, xanchor="left", x=0),
        width=750,
        height=750,
    )

    axis = dict(range=[-1.45, 1.45], showgrid=False, zeroline=False, showticklabels=False, linecolor=GRID_COLOR)
    fig.update_xaxes(**axis)
    fig.update_yaxes(**axis, scaleanchor="x", scaleratio=1)

    return fig


if __name__ == "__main__":
    for condition in LOADING_CONDITIONS:
        wake_field_figure(condition).show()
