#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 23:47:18 2020

@author: carlos
"""

import dash_html_components as html

from utilsv0 import Header
#######################
# Creacion Dash Layout#
#######################

def create_layout(app):
    
    return html.Div(
        [
        
        html.Div([Header(app)]),
            #page 1
            html.Div([
                    
                # Row 3
                html.Div(
                        [
                            html.Div(
                                [
                                      html.P(
                                            "El fundamento para determinar si los animales son portadores de derechos no depende de que se les otorgue el estatus de personas jurídicas, \
                                            sino que son sujetos de derechos porque cuentan con la condición de ser seres sintientes." ),
                                      html.P(
                                            "De-cosificar a los animales es el primer paso, mediante la reforma al Código Civil Federal, cuya inclusión del bienestar animal es necesaria, \
                                            ya que las problemáticas y situaciones en las que se enfrentan los animales no son finitas, pues de ciertas prácticas se derivan otras cada vez \
                                            más crueles e injustificadas." ),
                                    html.Br([]),
                                    html.P(
                                        "",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                        ),
                        ], className="sub_page"
                    ),
                ], className="page",)
        
        