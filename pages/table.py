#!/usr/bin/env python3
# coding: utf-8


import dash
import pandas as pd
from dash import html

dash.register_page(__name__, path_template="/table", title="Dash Table")


def df2table(df):
    data = []
    data_head = html.Tr([html.Th(col, style={"border": "solid #000 1px"}) for col in df.columns])
    data_body = [
        html.Tr([html.Td(cel, style={"border": "solid #000 1px"}) for cel in df.values[row]])
        for row in range(len(df.values))
    ]
    data.append(data_head)
    data.extend(data_body)
    return html.Table(
        data, style={"width": "100%", "border": "solid #000 1px", "text-align": "center"}
    )


def layout():
    df = pd.read_csv("https://git.io/Juf1t")
    return df2table(df)
