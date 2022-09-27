#!/usr/bin/env python3
# coding: utf-8


import dash
import pandas as pd
from dash import dash_table

dash.register_page(__name__, path_template="/datatable", title="Dash Datatable")


def layout():
    df = pd.read_csv("https://git.io/Juf1t")
    return dash_table.DataTable(
        data=df.to_dict("records"),
        columns=[{"name": i, "id": i} for i in df.columns],
    )
