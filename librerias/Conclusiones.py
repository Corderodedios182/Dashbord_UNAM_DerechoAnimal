#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 23:47:18 2020

@author: carlos
"""
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

from utilsv0 import Header

import pandas as pd

####################
#2 Importando datos#
####################

encuestas = pd.read_csv('https://raw.githubusercontent.com/Corderodedios182/Dashbord_UNAM_DerechoAnimal/master/datos/encuestas.csv')

Pregunta_1 = encuestas.loc[(encuestas.Pregunta == 1), ['Pregunta_texto', 'Respuesta_texto', 'Opción']].groupby(['Pregunta_texto','Respuesta_texto'], as_index = False).count()
Pregunta_1['Porcentaje'] = round(Pregunta_1.loc[:,'Opción'] / Pregunta_1.loc[:,'Opción'].sum(), 2)
Pregunta_1['Pregunta'] = "1"
Pregunta_1 = Pregunta_1.rename(columns = {'Opción':'Personas'})
Pregunta_1 = Pregunta_1.loc[:, ['Pregunta','Pregunta_texto','Respuesta_texto','Personas','Porcentaje']]

Pregunta_2 = encuestas.loc[(encuestas.Pregunta == 2), ['Pregunta_texto', 'Respuesta_texto', 'Opción']].groupby(['Pregunta_texto','Respuesta_texto'], as_index = False).count()
Pregunta_2['Porcentaje'] = round(Pregunta_2.loc[:,'Opción'] / Pregunta_2.loc[:,'Opción'].sum(), 2)
Pregunta_2['Pregunta'] = "2"
Pregunta_2 = Pregunta_2.rename(columns = {'Opción':'Personas'})
Pregunta_2 = Pregunta_2.loc[:, ['Pregunta','Pregunta_texto','Respuesta_texto','Personas','Porcentaje']]

Preguntas = pd.concat([Pregunta_1, Pregunta_2])

trace_0 = go.Table(
    header=dict(values=list(Preguntas.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[Preguntas.Pregunta,Preguntas.Pregunta_texto, Preguntas.Respuesta_texto, Preguntas.Personas, Preguntas.Porcentaje],
               fill_color='lavender',
               align='left'))

layout_0 = go.Layout(legend = {"x":.9,"y":.5},  margin=dict(l=40,r=30,b=80,t=100,),
                     title = 'Tabla Resumen Resultados por Pregunta',
                     annotations = [dict(xref='paper',
                                        yref='paper',
                                        x=0.5, y=-0.25,
                                        showarrow=False,
                                        text ='Con mayor participación de Veterinaria, Química, Ciencias, Derecho')],
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
                                    html.H6("Colocar algo de texto aquí", className="subtitle padded"),
                                    dcc.Graph(id='plot_1',figure = fig)
                                            ])
                        ],
                        className="row",
                        ),
                        ], className="sub_page"
                    ),
                ], className="page",)
        
        