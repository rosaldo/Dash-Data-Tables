#!/usr/bin/env python3
# coding: utf-8

import os

import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, dcc, html, page_container
from flask import Flask

server = Flask(__name__)

app = Dash(
    __name__,
    server=server,
    title="Dash Data Tables",
    update_title="Refreshing Dash Data Tables ...",
    use_pages=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.SKETCHY],
    meta_tags=[
        {"charset": "utf-8"},
        {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=no"},
    ],
)

brand_bar = dbc.Col(
    children=[
        dbc.Row(
            html.H1(
                children=[
                    dcc.Link(
                        children="Dash Data Tables",
                        href="/home",
                        style={"text-decoration": "none"},
                    )
                ],
                style={"text-align": "center", "height": "50px"},
            ),
        ),
    ],
    class_name="d-grid gap-2 col-6 mx-auto",
)

nav_bar = dbc.NavbarSimple(
    id="main_menu",
    fluid=True,
    links_left=True,
    style={"height": "50px"},
    children=[
        dbc.NavItem(dbc.NavLink("Table", href="/table")),
        dbc.NavItem(dbc.NavLink("Datatable", href="/datatable")),
        dbc.NavItem(dbc.NavLink("Tabulator", href="/tabulator")),
        dbc.NavItem(dbc.NavLink("AG-Grid", href="/aggrid")),
    ],
)

app.layout = dbc.Container(
    children=[
        brand_bar,
        nav_bar,
        page_container,
    ],
    id="main_root",
    fluid=True,
    style={"margin": "0px", "padding": "0px", "height": "100vh", "width": "100hw"},
)

self_name = os.path.basename(__file__)[:-3]
if len(os.sys.argv) == 1:
    app.run(host="127.0.0.1", port="8888", debug=True)
elif len(os.sys.argv) == 2:
    host = os.sys.argv[1]
    os.system(f"gunicorn {self_name}:server -b {host}:8888 --reload --timeout 120")
elif len(os.sys.argv) == 3:
    host = os.sys.argv[1]
    port = int(os.sys.argv[2])
    os.system(f"gunicorn {self_name}:server -b {host}:{port} --reload --timeout 120")
