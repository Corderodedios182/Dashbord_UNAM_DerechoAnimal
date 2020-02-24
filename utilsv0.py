#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 23:42:54 2020
@author: carlos
"""

import dash_html_components as html
import dash_core_components as dcc

def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div([
                html.Div([
                    html.Div(
                        [html.H5("Derecho Animal ",style={'text-align': 'center'}),
                         html.H6("¿Qué opinan los alumnos de la UNAM?",style={'text-align': 'center'})
                         ]),
                    html.Div([
                        html.Img(
                        src=app.get_asset_url("unam.png"),
                        style={'height':'90%', 'width':'90%', 'display': 'inline-block'},
                        className = "logo")
                            ],
                        className="five columns")],
                className="twelve columns",
                )
                ])
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Muestra",
                href="/Dash_Encuestas/Muestra",
                className="tab first",
            ),
            dcc.Link(
                "Resultados",
                href="/Dash_Encuestas/Resultados",
                className="tab",
            ),
            dcc.Link(
                "Conclusiones",
                href="/Dash_Encuestas/Conclusiones",
                className="tab",
            ),
            dcc.Link(
                "¿Qué sigue?", href="/Dash_Encuestas/Que_sigue", className="tab"
            ),
        ],
        className="row all-tabs",
    )
    return menu
