#!/usr/bin/env python3
# coding: utf-8


import dash

from dash_tabulator import DashTabulator

dash.register_page(__name__, path_template="/dash_tabulator", title="Dash Tabulator")


def layout():
    columns = [
        {"title": "Name", "field": "name", "width": 150, "headerFilter": True, "editor": "input"},
        {"title": "Age", "field": "age", "hozAlign": "left", "formatter": "progress"},
        {"title": "Favourite Color", "field": "col", "headerFilter": True},
        {"title": "Date Of Birth", "field": "dob", "hozAlign": "center"},
        {"title": "Rating", "field": "rating", "hozAlign": "center", "formatter": "star"},
        {"title": "Passed?", "field": "passed", "hozAlign": "center", "formatter": "tickCross"},
    ]
    data = [
        {"id": 1, "name": "Oli Bob", "age": "12", "col": "red", "dob": ""},
        {"id": 2, "name": "Mary May", "age": "1", "col": "blue", "dob": "14/05/1982"},
        {"id": 3, "name": "Christine Lobowski", "age": "42", "col": "green", "dob": "22/05/1982"},
        {"id": 4, "name": "Brendon Philips", "age": "125", "col": "orange", "dob": "01/08/1980"},
        {"id": 5, "name": "Margret Marmajuke", "age": "16", "col": "yellow", "dob": "31/01/1999"},
        {
            "id": 6,
            "name": "Fred Savage",
            "age": "16",
            "col": "yellow",
            "rating": "1",
            "dob": "31/01/1999",
        },
        {
            "id": 6,
            "name": "Brie Larson",
            "age": "30",
            "col": "blue",
            "rating": "1",
            "dob": "31/01/1999",
        },
    ]
    options = {"groupBy": "col", "selectable": 1}
    downloadButtonType = {"css": "btn btn-primary", "text": "Export to xlsx", "type": "xlsx"}
    clearFilterButtonType = {"css": "btn btn-outline-dark", "text": "Clear Filters"}
    return DashTabulator(
        id="tabulator",
        columns=columns,
        data=data,
        options=options,
        downloadButtonType=downloadButtonType,
        clearFilterButtonType=clearFilterButtonType,
    )
