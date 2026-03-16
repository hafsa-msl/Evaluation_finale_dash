import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import dcc, html

dash.register_page(__name__, path="/compare", name="Comparaison entre régions")

df = pd.read_csv("datas/avocado.csv")
regions = sorted(df["region"].unique())

layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H4(
                    "Prix moyen dans le temps",
                    className="text-white p-2 m-0",
                    style={"backgroundColor": "#0d6efd"},
                )
            ),
            className="mb-3 mt-3",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Badge("Région 1", color="primary", className="mb-1"),
                        dcc.Dropdown(
                            id="region1-dropdown",
                            options=[{"label": r, "value": r} for r in regions],
                            value=regions[0],
                            clearable=False,
                        ),
                    ],
                    xs=12,
                    md=6,
                ),
                dbc.Col(
                    [
                        dbc.Badge("Région 2", color="primary", className="mb-1"),
                        dcc.Dropdown(
                            id="region2-dropdown",
                            options=[{"label": r, "value": r} for r in regions],
                            value=regions[1] if len(regions) > 1 else regions[0],
                            clearable=False,
                        ),
                    ],
                    xs=12,
                    md=6,
                ),
            ],
            className="mb-3 px-3",
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="graph1"), xs=12, md=6),
                dbc.Col(dcc.Graph(id="graph2"), xs=12, md=6),
            ],
            className="px-3",
        ),
    ],
    fluid=True,
)
