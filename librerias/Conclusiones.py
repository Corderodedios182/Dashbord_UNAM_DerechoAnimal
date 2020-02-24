#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 23:47:18 2020

@author: carlos
"""
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
#import plotly.offline as pyo

from utilsv0 import Header

import pandas as pd

####################
#2 Importando datos#
####################

encuestas = pd.read_csv('https://raw.githubusercontent.com/Corderodedios182/Dashbord_UNAM_DerechoAnimal/master/datos/encuestas.csv')

Preguntas = []

for i in range(13):
    tmp = encuestas.loc[(encuestas.Pregunta == i), ['Pregunta_texto', 'Respuesta_texto', 'Opción']].groupby(['Pregunta_texto','Respuesta_texto'], as_index = False).count()
    tmp['Porcentaje'] = round(tmp.loc[:,'Opción'] / tmp.loc[:,'Opción'].sum(), 2)
    tmp['Porcentaje'] = tmp.Porcentaje.apply(lambda x: "{:.0%}".format(x))
    tmp['Pregunta'] = i
    tmp = tmp.rename(columns = {'Opción':'Personas'})
    tmp = tmp.loc[:, ['Pregunta','Pregunta_texto','Respuesta_texto','Personas','Porcentaje']]
    Preguntas.append(tmp)

Preguntas = pd.concat(Preguntas)

trace_0 = go.Table(
    header=dict(values=list(Preguntas.columns),
                fill_color='paleturquoise',
                align='center'),
    cells=dict(values=[Preguntas.Pregunta,Preguntas.Pregunta_texto, Preguntas.Respuesta_texto, Preguntas.Personas, Preguntas.Porcentaje],
               fill_color='lavender',
               align='center'))

layout_0 = go.Layout(legend = {"x":.9,"y":.5},  margin=dict(l=20, r=20, t=20, b=20),
                     height = 4400,
                     showlegend = False,
                    paper_bgcolor='rgb(243, 243, 243)',
                    template = 'ggplot2',
                    plot_bgcolor='rgb(243, 243, 243)')

fig = go.Figure(data = [trace_0], layout = layout_0)


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
                            ),
                                    html.Div([
                                    html.H6("Tabla resumen resultados por pregunta", className="subtitle padded"),
                                    dcc.Graph(id='plot_1',figure = fig)
                                            ])
                        ],
                        className="row",
                        ),
                        ], className="sub_page"
                    ),
                ], className="page",)
        
        