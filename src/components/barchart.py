from dash import Dash, html, dcc
import plotly.express as px
from . import ids

DATA= px.data.medals_long()

def render(app: Dash) -> html.Div:
    fig = px.bar(DATA, x="medal", y="count", color="nation", text="nation")
    return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)