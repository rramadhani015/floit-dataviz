from dash import Dash, html

from . import barchart,selections_dropdown

def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(className="dropdown-container",
            children=[selections_dropdown.render(app)]),
            barchart.render(app)
        ]
    )