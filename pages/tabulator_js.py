#!/usr/bin/env python3
# coding: utf-8


import dash
import dash_bootstrap_components as dbc
from dash import html

dash.register_page(__name__, path_template="/tabulator_js", title="Tabulator JS")


def layout():
    return dbc.Container(
        [
            html.Div(
                [
                    dbc.Button("Download CSV", id="download-csv"),
                    dbc.Button("Download JSON", id="download-json"),
                    dbc.Button("Download XLSX", id="download-xlsx"),
                    dbc.Button("Download PDF", id="download-pdf"),
                    dbc.Button("Download HTML", id="download-html"),
                ]
            ),
            html.Div(id="tabulator_js"),
        ]
    )
