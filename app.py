import dash
import dash_bootstrap_components as dbc

# Import des modules callbacks (requis avec use_pages=True)
import pages.table_cb
import pages.compare_cb

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
)

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Affichage des données", href="/", active="exact")),
        dbc.NavItem(dbc.NavLink("Comparaison entre régions", href="/compare", active="exact")),
        dbc.NavItem(dbc.NavLink("Aide en ligne", href="/markdown", active="exact")),
    ],
    brand="Application des M2 MECEN",
    color="primary",
    dark=True,
)

app.layout = dbc.Container(
    [navbar, dash.page_container],
    fluid=True,
    className="p-0",
)

if __name__ == "__main__":
    app.run(debug=True)
