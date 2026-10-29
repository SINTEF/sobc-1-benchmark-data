'''
Creates all the example plots and writes them to a single html file, which can be opened in any
web browser.
'''

import webbrowser
from pathlib import Path

from common import LOADING_CONDITIONS
from plot_resistance import model_resistance_figure, full_scale_resistance_figure
from plot_open_water import open_water_figure
from plot_wake import wake_field_figure

OUTPUT_FILE = Path(__file__).resolve().parent / "sobc1_calm_water_results.html"


if __name__ == "__main__":
    figures = [
        model_resistance_figure(),
        full_scale_resistance_figure(),
        open_water_figure(),
    ] + [wake_field_figure(condition) for condition in LOADING_CONDITIONS]

    # The plotly javascript library is embedded once, in the first figure, so the file also works offline
    plots = [
        fig.to_html(full_html=False, include_plotlyjs=(i == 0))
        for i, fig in enumerate(figures)
    ]

    html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>SOBC-1 - calm water resistance, open water and wake results</title>
    <style>
        body {{ font-family: sans-serif; max-width: 1000px; margin: 2em auto; background: #fcfcfb; color: #0b0b0b; }}
        .plot {{ margin-bottom: 3em; }}
    </style>
</head>
<body>
    <h1>SOBC-1 - calm water resistance, open water and wake results</h1>
    <p>Model tests performed in SINTEF Ocean's towing tank in May 2021. Model scale 1:32.</p>
    {"".join(f'<div class="plot">{plot}</div>' for plot in plots)}
</body>
</html>
'''

    OUTPUT_FILE.write_text(html, encoding="utf-8")
    print(f"Plots written to {OUTPUT_FILE}")

    webbrowser.open(OUTPUT_FILE.as_uri())
