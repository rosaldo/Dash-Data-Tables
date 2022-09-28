#!/usr/bin/env python3
# coding: utf-8


import dash
import pandas as pd
import plotly.graph_objs as go
from dash import dcc

dash.register_page(__name__, path_template="/gotable", title="Dash Graph Objects Table")


def layout():
    df = pd.read_csv("https://git.io/Juf1t")
    return dcc.Graph(
        figure=go.Figure(
            data=[
                go.Table(
                    header=dict(values=["A Scores", "B Scores"]),
                    cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]]),
                )
            ]
        )
    )
