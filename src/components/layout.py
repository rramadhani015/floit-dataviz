from dash import Dash, html
import pandas as pd
from . import barchart,selections_dropdown

def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            # html.Div(className="dropdown-container",
            # children=[selections_dropdown.render(app)]),
            html.Div(
                className="dropdown-container",
                children=[selections_dropdown.render_category(app, data)]
            ),
            barchart.render(app, data)
        ]
    )