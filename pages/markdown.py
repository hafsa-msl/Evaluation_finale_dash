import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

dash.register_page(__name__, path="/markdown", name="Aide en ligne")


def read_md(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H2(
                    "Présentation de Dash",
                    className="text-center text-white p-3",
                    style={
                        "backgroundColor": "#6b0f1a",
                        "backgroundImage": "repeating-linear-gradient(45deg, transparent, transparent 10px, rgba(255,255,255,.05) 10px, rgba(255,255,255,.05) 20px)",
                    },
                )
            )
        ),
        dbc.Row(
            dbc.Col(
                dbc.Accordion(
                    [
                        dbc.AccordionItem(
                            dcc.Markdown(read_md("expli1.md")),
                            title="Accueil",
                        ),
                        dbc.AccordionItem(
                            dcc.Markdown(read_md("expli2.md")),
                            title="Layout",
                        ),
                        dbc.AccordionItem(
                            dcc.Markdown(read_md("expli3.md")),
                            title="Callback",
                        ),
                    ],
                    always_open=False,
                ),
                className="mt-3",
            )
        ),
    ],
    fluid=True,
)
