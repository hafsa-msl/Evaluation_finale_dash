import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import dash_table, dcc, html

dash.register_page(__name__, path="/", name="Affichage des données")

df = pd.read_csv("datas/avocado.csv")

HIDDEN_COLS = ["Unnamed: 0", "4046", "4225", "4770", "Small Bags", "Large Bags", "XLarge Bags"]
DISPLAY_COLS = [c for c in df.columns if c not in HIDDEN_COLS]

regions = sorted(df["region"].unique())
types = sorted(df["type"].unique())

FONT = {"fontFamily": "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif", "fontSize": "14px"}

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Label("Sélectionner une région:", style=FONT),
                        dcc.Dropdown(
                            id="region-dropdown",
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
                        html.Label("Sélectionner un type:", style=FONT),
                        dcc.Dropdown(
                            id="type-dropdown",
                            options=[{"label": "Tous", "value": "Tous"}]
                            + [{"label": t, "value": t} for t in types],
                            value="Tous",
                            clearable=False,
                        ),
                    ],
                    xs=12,
                    md=6,
                ),
            ],
            className="mb-3 mt-3 px-3",
        ),
        dbc.Row(
            [
                dbc.Col(
                    dash_table.DataTable(
                        id="data-table",
                        columns=[{"name": c, "id": c} for c in DISPLAY_COLS],
                        style_header={
                            "fontWeight": "bold",
                            "backgroundColor": "#0d6efd",
                            "color": "white",
                            **FONT,
                        },
                        style_cell={
                            "textAlign": "left",
                            "padding": "6px",
                            **FONT,
                        },
                        style_data_conditional=[
                            {"if": {"row_index": "odd"}, "backgroundColor": "#f8f9fa"}
                        ],
                        page_size=10,
                                            )
                )
            ],
            className="px-3 pb-3",
        ),
    ],
    fluid=True,
)
