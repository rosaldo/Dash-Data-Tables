#!/usr/bin/env python3
# coding: utf-8


import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

dash.register_page(__name__, path_template="/aggrid", title="AG Grid")


def layout():
    return html.Div(
        id="ag_grid",
        className="ag-theme-alpine",
        style={
            "height": "200px",
            "width": "620px",
        },
    )
