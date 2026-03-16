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
                    className="text-center text-white p-4 m-0",
                    style={
                        "backgroundImage": "url('/assets/dash.jpg')",
                        "backgroundSize": "cover",
                        "backgroundPosition": "center",
                        "fontVariant": "small-caps",
                        "letterSpacing": "3px",
                        "textShadow": "2px 2px 4px rgba(0,0,0,0.8)",
                        "fontSize": "2rem",
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
                            item_id="item-1",
                        ),
                        dbc.AccordionItem(
                            dcc.Markdown(read_md("expli2.md")),
                            title="Layout",
                            item_id="item-2",
                        ),
                        dbc.AccordionItem(
                            dcc.Markdown(read_md("expli3.md")),
                            title="Callback",
                            item_id="item-3",
                        ),
                    ],
                    active_item="item-2",
                    always_open=False,
                ),
                className="mt-3",
            )
        ),
    ],
    fluid=True,
)
