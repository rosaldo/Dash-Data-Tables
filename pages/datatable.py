#!/usr/bin/env python3
# coding: utf-8


import dash
import pandas as pd
from dash.dash_table import DataTable

dash.register_page(__name__, path_template="/datatable", title="Dash Datatable")


def layout():
    df = pd.read_csv("https://git.io/Juf1t")
    return DataTable(
        data=df.to_dict("records"),
        columns=[{"name": col, "id": col} for col in df.columns],
        style_header={
            "color": "#fff",
            "backgroundColor": "#000",
            "fontWeight": "bold",
        },
        style_data={
            "color": "#000",
            "backgroundColor": "#eee",
        },
        style_data_conditional=[
            {
                "if": {"row_index": "odd"},
                "backgroundColor": "#aaa",
            }
        ],
    )
