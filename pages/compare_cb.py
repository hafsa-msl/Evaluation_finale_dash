import pandas as pd
import plotly.graph_objects as go
from dash import Input, Output, callback

df = pd.read_csv("datas/avocado.csv")


def make_figure(region, y_range):
    filtered = df[df["region"] == region].sort_values("Date")
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=filtered["Date"], y=filtered["AveragePrice"], mode="lines")
    )
    fig.update_layout(
        title=f"Prix moyen dans le temps - {region}",
        xaxis_title="Date",
        yaxis_title="Prix moyen ($)",
        yaxis=dict(range=y_range),
    )
    return fig


@callback(
    Output("graph1", "figure"),
    Output("graph2", "figure"),
    Input("region1-dropdown", "value"),
    Input("region2-dropdown", "value"),
)
def update_graphs(region1, region2):
    # Même échelle Y pour les deux graphiques
    r1 = df[df["region"] == region1]["AveragePrice"]
    r2 = df[df["region"] == region2]["AveragePrice"]
    y_range = [min(r1.min(), r2.min()) - 0.1, max(r1.max(), r2.max()) + 0.1]
    return make_figure(region1, y_range), make_figure(region2, y_range)
