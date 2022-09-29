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
            layout=dict(
                margin={"l": 1, "r": 1, "t": 1, "b": 1},
            ),
            data=[
                go.Table(
                    header=dict(
                        values=df.columns,
                        fill_color="#000",
                        line_color="#000",
                        align="center",
                        font=dict(color="#fff", size=16),
                        height=30,
                    ),
                    cells=dict(
                        values=df.transpose().values,
                        fill_color=[["#eee", "#aaa"] * (len(df.transpose().values) - 1)],
                        line_color="#000",
                        font=dict(color="#000", size=14),
                        height=30,
                    ),
                )
            ],
        )
    )
