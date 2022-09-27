#!/usr/bin/env python3
# coding: utf-8


import dash
from dash import html

dash.register_page(__name__, path_template="/table", title="Dash Table")


def layout():
    return html.Table(
        id="data_tables",
        className="display",
        style={
            "height": "200px",
            "width": "620px",
        },
        children=[
            html.Tr(
                [
                    html.Th("make"),
                    html.Th("model"),
                    html.Th("price"),
                ]
            ),
            html.Tr(
                [
                    html.Td("Toyota"),
                    html.Td("Celica"),
                    html.Td("35000"),
                ]
            ),
            html.Tr(
                [
                    html.Td("Ford"),
                    html.Td("Mondeo"),
                    html.Td("32000"),
                ]
            ),
            html.Tr(
                [
                    html.Td("Porsche"),
                    html.Td("Boxster"),
                    html.Td("72000"),
                ]
            ),
        ],
    )
