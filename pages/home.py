#!/usr/bin/env python3
# coding: utf-8


import dash
from dash import html

dash.register_page(__name__, path_template="/", title="Home")


def layout():
    return html.Div(
        children=html.H1("Escolha uma das opções acima"),
        style={
            "height": "calc(100vh - 110px)",
            "width": "100hw",
            "text-align": "center",
            "padding-top": "calc(50vh - 110px)",
        },
    )
