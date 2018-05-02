"""
==========================================================================
Proyecto #1 ­ Simulador Votantes(Regresion Logistica)

==========================================================================
:Institucion: Instituto Tecnologico de Costa Rica
:Curso: Inteligencia Artificial
:Grupo: 1
:Semestre: I Semestre 2018
:Autores: Fernanda Alvarado Vargas,fernadaalvarado95@gmail.com /
          Minor Sancho Valverde,tivin.minor10@gmail.com /
          Freyser Jimenez Mena, fjimenez577@gmail.com /
:Fecha: 25/04/2018

Dependencias con archivos de entrada:
- datos.csv
"""
# -----------------------------------------------------------------------
import os
import sys
import csv
import random
import unittest
import numpy as np
from main import *
os . system('ls -lah')
import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

# -----------------------------------------------------------------------

################################### 1 ##################################
"""
Funcion que genera la regresion logistica pra la primera ronda, con una
muestra pias.
"""
# -----------------------------------------------------------------------


def regresion_logistica_primer_ronda_pais(loss, cantidad_muestra):
    x1 = generar_muestra_pais(cantidad_muestra)
    y = dividir_entradas_salidas(x1)
    x1 = escribir_csv(x1)

    data = pd.read_csv('testfile.csv', encoding='cp1252')
    data = data.dropna()
    data2 = pd.get_dummies(
        data,
        columns=[
            'CANTON',
            'Poblacion_total',
            'Superficie (km2)',
            'Densidad de población',
            'Porcentaje de alfabetismo',
            'Porcentaje de población ocupada no asegurada',
            'Porcentaje de población nacida en el extranjero',
            'Porcentaje de población con discapacidad',
            'Porcentaje de población no asegurada',
            'Porcentaje de hogares con jefatura femenina',
            'Porcentaje de hogares con jefatura compartida',
            'Sexo',
            'Edad',
            'PROVINCIA'])
    data2.columns

    X = data2.iloc[:, 1:]
    y = data2.iloc[:, 0]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    classifier = LogisticRegression(loss)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    from sklearn.metrics import confusion_matrix

    confusion_matrix = confusion_matrix(y_test, y_pred)
    print('Accuracy: {:.2f}'.format(classifier.score(X_test, y_test)))
    return 0
# -----------------------------------------------------------------------


################################### 2 ##################################
"""
Funcion que genera la regresion logistica pra la primera ronda, con una
muestra para provincia.
"""
# -----------------------------------------------------------------------


def regresion_logistica_primer_ronda_provincia(
        loss, cantidad_muestra, nombre_provincia):
    x1 = generar_muestra_provincia(cantidad_muestra, nombre_provincia)
    for i in x1:
        i.insert(0, nombre_provincia)
    y = dividir_entradas_salidas(x1)
    x1 = escribir_csv(x1)

    data = pd.read_csv('testfile.csv', encoding='cp1252')
    data = data.dropna()
    data2 = pd.get_dummies(
        data,
        columns=[
            'CANTON',
            'Poblacion_total',
            'Superficie (km2)',
            'Densidad de población',
            'Porcentaje de alfabetismo',
            'Porcentaje de población ocupada no asegurada',
            'Porcentaje de población nacida en el extranjero',
            'Porcentaje de población con discapacidad',
            'Porcentaje de población no asegurada',
            'Porcentaje de hogares con jefatura femenina',
            'Porcentaje de hogares con jefatura compartida',
            'Sexo',
            'Edad',
            'PROVINCIA'])
    data2.columns

    X = data2.iloc[:, 1:]
    y = data2.iloc[:, 0]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    classifier = LogisticRegression(loss)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    from sklearn.metrics import confusion_matrix

    confusion_matrix = confusion_matrix(y_test, y_pred)
    print('Accuracy: {:.2f}'.format(classifier.score(X_test, y_test)))
    return 0
# -----------------------------------------------------------------------


################################### 3 ##################################
"""
Funcion que genera la regresion logistica para la segunda ronda, con una
muestra para provincia.
"""
# -----------------------------------------------------------------------


def regresion_logistica_segunda_ronda_provincia(
        loss, cantidad_muestra, nombre_provincia):
    x1 = generar_muestra_provincia2(cantidad_muestra, nombre_provincia)
    for i in x1:
        i.insert(0, nombre_provincia)
    y = dividir_entradas_salidas2(x1)
    x1 = escribir_csv2(x1)

    data = pd.read_csv('testfile.csv', encoding='cp1252')
    data = data.dropna()
    data2 = pd.get_dummies(
        data,
        columns=[
            'CANTON',
            'Poblacion_total',
            'Superficie (km2)',
            'Densidad de población',
            'Porcentaje de alfabetismo',
            'Porcentaje de población ocupada no asegurada',
            'Porcentaje de población nacida en el extranjero',
            'Porcentaje de población con discapacidad',
            'Porcentaje de población no asegurada',
            'Porcentaje de hogares con jefatura femenina',
            'Porcentaje de hogares con jefatura compartida',
            'Sexo',
            'Edad',
            'PROVINCIA'])
    data2.columns

    X = data2.iloc[:, 1:]
    y = data2.iloc[:, 0]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    classifier = LogisticRegression(loss)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    from sklearn.metrics import confusion_matrix

    confusion_matrix = confusion_matrix(y_test, y_pred)
    print('Accuracy: {:.2f}'.format(classifier.score(X_test, y_test)))
    return 0
# -----------------------------------------------------------------------


################################### 4 ##################################
"""
Funcion que genera la regresion logistica para la segunda ronda, con una
muestra pais.
"""
# -----------------------------------------------------------------------


def regresion_logistica_segunda_ronda_pais(loss, cantidad_muestra):
    x1 = generar_muestra_pais_con_segunda(cantidad_muestra)
    y = dividir_entradas_salidas2(x1)
    x1 = escribir_csv2(x1)

    data = pd.read_csv('testfile.csv', encoding='cp1252')
    data = data.dropna()
    data2 = pd.get_dummies(
        data,
        columns=[
            'CANTON',
            'Poblacion_total',
            'Superficie (km2)',
            'Densidad de población',
            'Porcentaje de alfabetismo',
            'Porcentaje de población ocupada no asegurada',
            'Porcentaje de población nacida en el extranjero',
            'Porcentaje de población con discapacidad',
            'Porcentaje de población no asegurada',
            'Porcentaje de hogares con jefatura femenina',
            'Porcentaje de hogares con jefatura compartida',
            'Sexo',
            'Edad',
            'Voto primera',
            'PROVINCIA'])
    data2.columns

    X = data2.iloc[:, 1:]
    y = data2.iloc[:, 0]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    classifier = LogisticRegression(loss)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    from sklearn.metrics import confusion_matrix

    confusion_matrix = confusion_matrix(y_test, y_pred)
    print('Accuracy: {:.2f}'.format(classifier.score(X_test, y_test)))
    return 0
# -----------------------------------------------------------------------


################################### 5 ##################################
"""
Funcion que genera la regresion logistica para la segunda ronda, con una
muestra para provincia pero tomando encuenta el voto de la primer ronda.
"""
# -----------------------------------------------------------------------


def regresion_logistica_segunda_y_primera_provincia(
        loss, cantidad_muestra, nombre_provincia):
    x1 = generar_muestra_provincia2(cantidad_muestra, nombre_provincia)
    for i in x1:
        i.insert(0, nombre_provincia)
    y = dividir_entradas_salidas2(x1)
    x1 = escribir_csv2(x1)

    data = pd.read_csv('testfile.csv', encoding='cp1252')
    data = data.dropna()
    data2 = pd.get_dummies(
        data,
        columns=[
            'CANTON',
            'Poblacion_total',
            'Superficie (km2)',
            'Densidad de población',
            'Porcentaje de alfabetismo',
            'Porcentaje de población ocupada no asegurada',
            'Porcentaje de población nacida en el extranjero',
            'Porcentaje de población con discapacidad',
            'Porcentaje de población no asegurada',
            'Porcentaje de hogares con jefatura femenina',
            'Porcentaje de hogares con jefatura compartida',
            'Sexo',
            'Edad',
            'Voto primera',
            'PROVINCIA'])
    data2.columns

    X = data2.iloc[:, 1:]
    y = data2.iloc[:, 0]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    classifier = LogisticRegression(loss)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    from sklearn.metrics import confusion_matrix

    confusion_matrix = confusion_matrix(y_test, y_pred)
    print('Accuracy: {:.2f}'.format(classifier.score(X_test, y_test)))
    return 0
# -----------------------------------------------------------------------


################################### 6 ##################################
"""
Funcion que genera la regresion logistica para la segunda ronda, con una
muestra pais pero tomando encuenta el voto de la primer ronda.
"""
# -----------------------------------------------------------------------


def regresion_logistica_segunda_y_primera_pais(loss, cantidad_muestra):
    x1 = generar_muestra_pais_con_segunda(cantidad_muestra)
    y = dividir_entradas_salidas2(x1)
    x1 = escribir_csv2(x1)

    data = pd.read_csv('testfile.csv', encoding='cp1252')
    data = data.dropna()
    data2 = pd.get_dummies(
        data,
        columns=[
            'CANTON',
            'Poblacion_total',
            'Superficie (km2)',
            'Densidad de población',
            'Porcentaje de alfabetismo',
            'Porcentaje de población ocupada no asegurada',
            'Porcentaje de población nacida en el extranjero',
            'Porcentaje de población con discapacidad',
            'Porcentaje de población no asegurada',
            'Porcentaje de hogares con jefatura femenina',
            'Porcentaje de hogares con jefatura compartida',
            'Sexo',
            'Edad',
            'Voto primera',
            'PROVINCIA'])
    data2.columns

    X = data2.iloc[:, 1:]
    y = data2.iloc[:, 0]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    classifier = LogisticRegression(loss)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    from sklearn.metrics import confusion_matrix

    confusion_matrix = confusion_matrix(y_test, y_pred)
    print('Accuracy: {:.2f}'.format(classifier.score(X_test, y_test)))
    return 0


# regresion_logistica_segunda_ronda_pais('l1',10000)
# regresion_logistica_primer_ronda_pais('l1',10000)
#regresion_logistica_segunda_ronda_provincia('l1',1000,'SAN JOSE')
#regresion_logistica_primer_ronda_provincia('l2',1000,'SAN JOSE')
#regresion_logistica_segunda_y_primera_provincia('l1',10000,'SAN JOSE')
regresion_logistica_segunda_y_primera_pais('l1', 10000)
