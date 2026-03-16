import dash
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
)

app.layout = dbc.Container([dash.page_container], fluid=True, className="p-0")

if __name__ == "__main__":
    app.run(debug=True)
