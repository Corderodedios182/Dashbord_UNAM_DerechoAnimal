#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 23:47:18 2020

@author: carlos
"""

import dash_html_components as html

from utilsv0 import Header

######################
#Creacion Dash Layout#
######################

def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 6
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("¿Qué se necesita para una protección animal a nivel federal más amplia?", className="subtitle padded"),
                                    html.Br([]),
                                ],
                                className="row",
                            ),
                            html.Div(
                                [
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.Li("La investigación se basa en el análisis jurídico-lingüístico del Libro segundo: De los bienes. Títulos primero y segundo \
                                                    (Clasificación de los bienes), capítulos I, II, III, IV, V; títulos tercero y cuarto (De la propiedad), capítulos I, II \
                                                    (De la apropiación de los animales) y IV, del Código Civil Federal (CCF) mexicano."),
                                            html.Li(
                                                "Por lo que se requiere un manejo de información a partir de la interpretación jurídica, del campo de la lingüística aplicada y de la biología."
                                            ),
                                            html.Li(
                                                "Se llevará a cabo un estudio comparado de los códigos civiles de Alemania, Austria, Suiza y Francia, en cuyas legislaciones los animales han dejado de ser cosas."
                                            ),
                                            html.Li(
                                                "Se realizará el análisis lingüístico-biológico del concepto de animal."
                                            ),
                                            html.Li(
                                                "En cuanto hace al reconocimiento de derechos se pretende un análisis categórico de éstos (con ciertas excepciones de acuerdo a la especie), \
                                                pues si bien el sector universitario opinó que todos los animales poseen derechos, es cierto que tales derechos deben ser estudiados a profundidad."
                                            ),
                                            html.Li(
                                                "Tratándose del bienestar animal, durante el sacrificio (ley de sanidad y normas oficiales mexicanas) o en la vida libre de los animales, éste representa un avance en la materia."
                                            ),
                                            html.Li(
                                                "No obstante, sin olvidar que la crueldad hacia ellos y su sufrimiento sigue estando presente en la industria cárnica y farmacéutica, y en los hogares mexicanos, \
                                                se estudiarán las implicaciones legales (obligaciones de hacer o no hacer) sobre la muerte del animal con aturdimiento y la diferencia que existe entre este método \
                                                y la eutanasia (cuando ya no es posible mantener con vida a un animal)."
                                            )
                                        ],
                                        id="reviews-bullet-pts",
                                    ),
                                ],
                                className="row",
                            ),
                        ],
                        className="row ",
                    )
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )