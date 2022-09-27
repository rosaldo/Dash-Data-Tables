#!/usr/bin/env python3
# coding: utf-8

import dash
from dash import dcc

dash.register_page(__name__)


def layout():
    return dcc.Location(id="404_logout_location", href="/", refresh=True)
