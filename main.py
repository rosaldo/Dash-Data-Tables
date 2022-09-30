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
        "assets/tabulator.min.css",
    ],
    external_scripts=[
        "assets/datatables.min.js",
        "assets/tabulator.min.js",
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
                "Tabulator JS",
                id="main_menu_tabulator_js",
                href="/tabulator_js",
                active=True,
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                "Dash Tabulator",
                id="main_menu_dash_tabulator",
                href="/dash_tabulator",
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
        function tabulator_show(loading_state, bt_csv, bt_json, bt_xlsx, bt_pdf, bt_html) {
            var table = new Tabulator(document.querySelector("#tabulator_js"), {
                pagination: "local",
                paginationSize: 7,
                paginationSizeSelector: [3, 5, 7, 9, 11, true],
                resizableColumns: "header",
                groupBy: "col",
                selectable: 1,
                downloadButtonType: {"css": "btn btn-primary", "text": "Export to xlsx", "type": "xlsx"},
                clearFilterButtonType: {"css": "btn btn-outline-dark", "text": "Clear Filters"},
                columns: [
                    {"title": "Name", "field": "name", "width": 150, "headerFilter": true, "editor": "input"},
                    {"title": "Age", "field": "age", "hozAlign": "left", "formatter": "progress"},
                    {"title": "Favourite Color", "field": "col", "headerFilter": true},
                    {"title": "Date Of Birth", "field": "dob", "hozAlign": "center"},
                    {"title": "Rating", "field": "rating", "hozAlign": "center", "formatter": "star"},
                    {"title": "Passed?", "field": "passed", "hozAlign": "center", "formatter": "tickCross"},
                ],
                data: [
                    {"id": 1, "name": "Oli Bob", "age": "12", "col": "red", "dob": ""},
                    {"id": 2, "name": "Mary May", "age": "1", "col": "blue", "dob": "14/05/1982"},
                    {"id": 3, "name": "Christine Lobowski", "age": "42", "col": "green", "dob": "22/05/1982"},
                    {"id": 4, "name": "Brendon Philips", "age": "125", "col": "orange", "dob": "01/08/1980"},
                    {"id": 5, "name": "Margret Marmajuke", "age": "16", "col": "yellow", "dob": "31/01/1999"},
                    {"id": 6, "name": "Fred Savage", "age": "16", "col": "yellow", "rating": "1", "dob": "31/01/1999"},
                    {"id": 6,"name": "Brie Larson","age": "30","col": "blue","rating": "1","dob": "31/01/1999"},
                ],
            });
            
            //trigger download of data.csv file
            if (bt_csv == 1) {
                table.download("csv", "data.csv");
            };
            
            
            //trigger download of data.json file
            if (bt_json == 1) {
                table.download("json", "data.json");
            };

            //trigger download of data.xlsx file
            if (bt_xlsx == 1) {
                table.download("xlsx", "data.xlsx", {sheetName:"My Data"});
            };

            //trigger download of data.pdf file
            if (bt_pdf == 1) {
                table.download("pdf", "data.pdf", {
                    orientation:"portrait", //set page orientation to portrait
                    title:"Example Report", //add title to report
                });
            };

            //trigger download of data.html file
            if (bt_html == 1) {
                table.download("html", "data.html", {style:true});
            };
            
            return ([0, 0, 0, 0, 0, 0]);
        }
    """,
    [
        Output("tabulator_js", "n_clicks"),
        Output("download-csv", "n_clicks"),
        Output("download-json", "n_clicks"),
        Output("download-xlsx", "n_clicks"),
        Output("download-pdf", "n_clicks"),
        Output("download-html", "n_clicks"),
    ],
    [
        Input("tabulator_js", "loading_state"),
        Input("download-csv", "n_clicks"),
        Input("download-json", "n_clicks"),
        Input("download-xlsx", "n_clicks"),
        Input("download-pdf", "n_clicks"),
        Input("download-html", "n_clicks"),
    ],
)


app.clientside_callback(
    """
        function aggrid_show(loading_state, n_clicks) {
            const gridOptions = {
                enableRangeSelection: true,
                rowSelection: 'multiple',
                defaultColDef: {
                    flex: 1,
                    minWidth: 100,
                    filter: true,
                    resizable: true,
                },
                columnDefs: [
                    { field: "make", filter: 'agTextColumnFilter' },
                    { field: "model", filter: 'agTextColumnFilter' },
                    { field: "price", filter: 'agNumberColumnFilter'}
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
