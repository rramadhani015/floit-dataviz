from dash import Dash, html, dcc
from dash.dependencies import Input,Output
from . import ids


def render(app: Dash) -> html.Div:
    all_selections = ["option1","option2","option3"]

    @app.callback(
        Output(ids.SELECTIONS_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_BUTTON, "n_clicks")
    )
    def select_all_selections(_: int) -> list[str]:
        return all_selections

    return html.Div(
        children=[
            html.H6("dropdown options"),
            dcc.Dropdown(
                id=ids.SELECTIONS_DROPDOWN,
                options=[{"label":selection, "value": selection} for selection in all_selections],
                value=all_selections,
                multi=True
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_BUTTON
            )
        ]
    )