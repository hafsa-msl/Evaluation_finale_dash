import pandas as pd
from dash import Input, Output, callback

df = pd.read_csv("datas/avocado.csv")

HIDDEN_COLS = ["Unnamed: 0", "4046", "4225", "4770", "Small Bags", "Large Bags", "XLarge Bags"]
DISPLAY_COLS = [c for c in df.columns if c not in HIDDEN_COLS]


@callback(
    Output("data-table", "data"),
    Input("region-dropdown", "value"),
    Input("type-dropdown", "value"),
)
def update_table(region, avocado_type):
    filtered = df[df["region"] == region]
    if avocado_type != "Tous":
        filtered = filtered[filtered["type"] == avocado_type]
    return filtered[DISPLAY_COLS].to_dict("records")