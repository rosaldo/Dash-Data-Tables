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
    external_stylesheets=[
        dbc.themes.SKETCHY,
        "assets/datatables.min.css",
    ],
    external_scripts=[
        "assets/datatables.min.js",
        "assets/ag-grid-community.min.js",
        "assets/xlsx.full.min.js",
        "assets/jspdf.min.js",
        "assets/jspdf.plugin.autotable.js",
    ],
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
        dbc.NavItem(
            dbc.NavLink(
                "Table",
                id="main_menu_table",
                href="/table",
                active=True,
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                "Datatable",
                id="main_menu_datatable",
                href="/datatable",
                active=True,
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                "GO Table",
                id="main_menu_gotable",
                href="/gotable",
                active=True,
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                "Tabulator",
                id="main_menu_tabulator",
                href="/tabulator",
                active=True,
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                "AG-Grid",
                id="main_menu_aggrid",
                href="/aggrid",
                active=True,
            )
        ),
    ],
)

app.layout = dbc.Container(
    children=[
        brand_bar,
        nav_bar,
        page_container,
    ],
)


app.clientside_callback(
    """
        $(document).ready(function () {
            $("#data_tables").DataTable();
        });
    """,
    [
        Output("data_tables", "n_clicks"),
    ],
    [
        Input("data_tables", "loading_state"),
    ],
    [
        State("data_tables", "n_clicks"),
    ],
)


app.clientside_callback(
    """
        function aggrid_show(loading_state, n_clicks) {
            const gridOptions = {
                columnDefs: [
                    { field: "make" },
                    { field: "model" },
                    { field: "price" }
                ],
                rowData: [
                    { make: "Toyota", model: "Celica", price: 35000 },
                    { make: "Ford", model: "Mondeo", price: 32000 },
                    { make: "Porsche", model: "Boxster", price: 72000 }
                ]
            };
            new agGrid.Grid(document.querySelector("#ag_grid"), gridOptions);
        }
    """,
    [
        Output("ag_grid", "n_clicks"),
    ],
    [
        Input("ag_grid", "loading_state"),
    ],
    [
        State("ag_grid", "n_clicks"),
    ],
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
