import pandas as pd
from dash import Dash, html, dcc, dash_table
import plotly.express as px


# Plotly dashboard
app = Dash(__name__)


def generate_gui() -> None:
    """
    Draw a table and graph with the collected data.
    """

    df = pd.read_csv("comparator/output.csv")

    app.layout = html.Div(
        [
            html.H1(children="Stablecoin analysis tool", style={"textAlign": "center"}),
            dash_table.DataTable(data=df.to_dict("records"), page_size=10),
            dcc.Graph(figure=px.histogram(df, x="blockchain", y="total_supply")),
        ]
    )
    app.run_server(debug=True)
