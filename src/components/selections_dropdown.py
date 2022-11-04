from dash import Dash, html, dcc
from . import ids

def render(app: Dash) -> html.Div:
    all_selections = ["option1","option2","option3"]
    return html.Div(
        children=[
            html.H6("dropdown options"),
            dcc.Dropdown(
                id=ids.SELECTIONS_DROPDOWN,
                options=[{"label":selection, "value": selection} for selection in all_selections],
                value=all_selections,
                multi=True
            )
        ]
    )