#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 23:47:18 2020

@author: carlos
"""
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import plotly.graph_objects as go

from utilsv0 import Header
####################
#2 Importando datos#
####################
#encuestas = pd.read_csv('/home/carlos/Documentos/1_Dashbord_UNAM_DerechoAnimal/datos/encuestas.csv')
encuestas = pd.read_csv('https://raw.githubusercontent.com/Corderodedios182/Dashbord_UNAM_DerechoAnimal/master/datos/encuestas.csv')

#General
conteo = encuestas.Facultad.value_counts().reset_index()
conteo['encuestados'] = conteo.Facultad/12
conteo.columns = ['Facultad','Conteo','encuestados']

#Sexo
Masculino = encuestas[encuestas.Sexo == 'M'].Facultad.value_counts().reset_index()
Masculino['encuestados'] = Masculino.Facultad/12
Masculino.columns = ['Facultad','Conteo','encuestados']

Mujeres = encuestas[encuestas.Sexo == 'F'].Facultad.value_counts().reset_index()
Mujeres['encuestados'] = Mujeres.Facultad/12
Mujeres.columns = ['Facultad','Conteo','encuestados']

#Rango de Edades
tmp = encuestas.groupby(['Facultad','Edad'],  as_index = False).count().iloc[:,:3]
tmp.columns = ['Facultad','Edad','Conteo']
tmp.Conteo = tmp.Conteo/12

tmp.loc[tmp['Edad'] == 16]

######################
#3 Creando el grafico#
######################

#Facultades
trace_0 = go.Pie(labels=conteo.loc[:,'Facultad'], values=conteo.loc[:,'encuestados'])
layout_0 = go.Layout(legend = {"x":.9,"y":.5},  margin=dict(l=40,r=30,b=80,t=100,),
                     title = 'Se encuestaron a 2013 alumnos en 14 facultades',
                     annotations = [dict(xref='paper',
                                        yref='paper',
                                        x=0.5, y=-0.25,
                                        showarrow=False,
                                        text ='Con mayor participación de las facultades de Veterinaria, Química, Ciencias, Derecho')],
                    paper_bgcolor='rgb(243, 243, 243)',
                    template = 'ggplot2',
                    plot_bgcolor='rgb(243, 243, 243)')
fig_0 = go.Figure(data = [trace_0], layout = layout_0)

#Sexo
fig_1 = go.Figure()

fig_1.add_trace(go.Bar(
    x=Masculino['Facultad'],
    y=Masculino['encuestados'],
    name='Hombres',
    text = Masculino['encuestados'],
    textposition = 'auto',
    marker=dict(
        color='rgba(58, 71, 80, 0.6)',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
    )
))
fig_1.add_trace(go.Bar(
    x=Mujeres['Facultad'],
    y=Mujeres['encuestados'],
    name='Mujeres',
    text = Mujeres['encuestados'],
    textposition = 'auto',
    marker=dict(
        color='rgba(246, 78, 139, 0.6)',
        line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
        )
))

fig_1.update_layout(barmode='stack', title = '55% Mujeres y 45% Hombres', title_x = 0.50,
                    margin=dict(l=40,r=30,b=80,t=100,),
                    paper_bgcolor='rgb(243, 243, 243)',
                    plot_bgcolor='rgb(243, 243, 243)')

#Rango de Edades
fig_2 = go.Figure()

fig_2.add_trace(go.Box(
    y=tmp["Edad"],
    x=tmp["Facultad"],
    name='kale',
    boxpoints='all',
    jitter=0.5,
    whiskerwidth=0.2,
    marker_size=2,
    line_width=1)
    )

fig_2.update_layout(
    title = 'Rango de Edad entre 17-27 años',
    title_x = 0.50,
    yaxis_title='Rango de Edades',
    yaxis=dict(
        autorange=True,
        showgrid=True,
        zeroline=True,
        dtick=3,
        gridcolor='rgb(255, 255, 255)',
        gridwidth=1,
        zerolinecolor='rgb(255, 255, 255)',
        zerolinewidth=2,
    ),
    margin=dict(
        l=40,
        r=30,
        b=80,
        t=100,
    ),
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
    showlegend=False
)



########################
#4 Creacion Dash Layout#
########################

def create_layout(app):
    
    return html.Div(
        [
        html.Div([Header(app)]),
            #page 1
            html.Div([
                    
                # Row 3
                html.Div([
                         html.Div([
                                    html.P(
                                            "La presente encuesta se realizó a los alumnos de las facultades de la Universidad Nacional Autónoma de México (UNAM) con la finalidad de conocer las opiniones y conocimiento que tienen sobre el derecho animal y la importancia de éste para la defensa de los animales en México." ),
                                    html.P(        
                                            "La profesionalización y capacitación hacia la comunidad universitaria en temas de bienestar animal y derecho animal resulta necesaria para entender el trato y cuidado de los animales, las implicaciones jurídicas que se derivan de los actos civiles-mercantiles y las limitaciones que se tienen en materia civil."),
                                    
                                    ],
                         className="product")],
                        className="row"),
                #Row 4
                html.Div([
                    
                        html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("Porcentaje Muestra por Facultades UNAM", className="subtitle padded"),
                                    dcc.Graph(id='plot_0',figure = fig_0)
                                ]
                                    ),
                            ],
                          className = "row",
                        style = {"margin-bottom":"35px"})
                         ],
                                className = "row", style = {"margin-bottom":"35px"}),
                #Row 5
                    html.Div([
                        html.Div([
                                    html.H6("Proporción Mujeres y Hombres", className="subtitle padded"),
                                    dcc.Graph(id='plot_1',figure = fig_1)])]),
                #row 6
                    html.Div([
                        html.Div([
                                    html.H6("Rango de Edades Facultades", className="subtitle padded"),
                                    dcc.Graph(id='plot_2',figure = fig_2)])])
                    ], className="sub_page"),
                ], className="page",)
        
        