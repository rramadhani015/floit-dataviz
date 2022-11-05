from dash import Dash, html, dcc
from dash.dependencies import Input,Output
from ..data.loader import DataSchema
import plotly.express as px
import pandas as pd
from . import ids

# DATA= px.data.medals_long()

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART, "children"),
        Input(ids.CATEGORY_DROPDOWN, "value")
    )
    def update_barchart(category:list[str]) -> html.Div:
        filtered_data = data.query("category in @category")
        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.")
        
        def create_pivot_table() -> pd.DataFrame:
            pt = filtered_data.pivot_table(
                values=DataSchema.AVERAGE_RATING,
                columns=[DataSchema.CATEGORY],
                index=[DataSchema.SKU],
                aggfunc="mean",
                fill_value=0
            )
            return pt.reset_index().sort_values(DataSchema.SKU, ascending=False)

        fig = px.bar(
            create_pivot_table(),
            # x=DataSchema.CATEGORY,
            x='Shoes',
            y=DataSchema.SKU,
            # color=DataSchema.CATEGORY,
            color='Shoes',
            text="Shoes"
        )
        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)
        # fig = px.bar(filtered_data, x="medal", y="count", color="nation", text="nation")
        
    return html.Div(id=ids.BAR_CHART)