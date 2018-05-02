"""
==========================================================================

Proyecto #1 ­ Simulador Votantes(Arbol KD)

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
import math
import operator
import os
import sys
import csv
import random
import unittest
import numpy as np
from main import *
os . system('ls -lah')
from random import randrange
# -----------------------------------------------------------------------

################################### 1 ##################################
"""
Funcion que nos obtiene los datos y los lee para la primera ronda, admas
nos genera una salida con datos de training y test.
"""
# -----------------------------------------------------------------------


def leerArchivoCSV_with_header3(nombre, corte, trainingSet, testeo):
    result = []
    with open(nombre) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            result += [row]
    result = result[1:]

    resultado = []
    for i in result:
        tempo = [int(i[-1]), int(i[1]), int(i[-3]), int(i[-2]), int(i[0])]
        resultado += [tempo]
    for x in range(len(resultado)):
        if random.random() < corte:
            trainingSet.append(resultado[x])
        else:
            testeo.append(resultado[x])
    return resultado
# -----------------------------------------------------------------------


################################### 2 ##################################
"""
Funcion que nos obtiene los datos y los lee para la segunda ronnda, y
la segunda mas la primera, ademas nos genera una salida con datos de
training y test.
"""
# -----------------------------------------------------------------------


def leerArchivoCSV_with_header4(nombre, corte, trainingSet, testeo):
    result = []
    with open(nombre) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            result += [row]
    result = result[1:]

    resultado = []

    for i in result:
        tempo = [int(i[-1]), int(i[1]), int(i[-4]), int(i[-2]), int(i[0])]
        resultado += [tempo]
    for x in range(len(resultado)):
        if random.random() < corte:
            trainingSet.append(resultado[x])
        else:
            testeo.append(resultado[x])
    return resultado
# -----------------------------------------------------------------------


################################### 3 ##################################
"""
Funcion que nos obtiene la distancia euclideana para los puntos.
"""
# -----------------------------------------------------------------------


def distanciaEuclideana(x1, x2, largo):
    distancia = 0
    for i in range(largo):
        distancia += pow((x1[i] - x2[i]), 2)
    return math.sqrt(distancia)
# -----------------------------------------------------------------------


################################### 4 ##################################
"""
Funcion que nos obtiene los vecinos par los datos de training y test.
"""
# -----------------------------------------------------------------------


def obtenerVecinos(entrenamiento, testeo, k):
    distancias = []
    largo = len(testeo) - 1
    for x in range(len(entrenamiento)):
        dist = distanciaEuclideana(testeo, entrenamiento[x], largo)
        distancias.append((entrenamiento[x], dist))
    distancias.sort(key=operator.itemgetter(1))
    vecinos = []
    for x in range(k):
        vecinos.append(distancias[x][0])
    return vecinos
# -----------------------------------------------------------------------


################################### 5 ##################################
"""
Funcion que nos permite obtener el conjunto de datos con vecinos asignados
y tenerlos ordenados.
"""
# -----------------------------------------------------------------------


def obtenerRespuesta(vecinos):
    votos = {}
    for x in range(len(vecinos)):
        respuesta = vecinos[x][-1]
        if respuesta in votos:
            votos[respuesta] += 1
        else:
            votos[respuesta] = 1
    votosOrdenados = sorted(
        votos.items(),
        key=operator.itemgetter(1),
        reverse=True)
    return votosOrdenados[0][0]
# -----------------------------------------------------------------------


################################### 6 ##################################
"""
Funcion que nos permite calcula el accuracy para los datos.
"""
# -----------------------------------------------------------------------


def obtenerExactitud(testeo, predicciones):
    correctos = 0
    for x in range(len(testeo)):
        if testeo[x][-1] == predicciones[x]:
            correctos += 1
    return (correctos / float(len(testeo))) * 100.0
# -----------------------------------------------------------------------


################################### 7 ##################################
"""
Funcion que genera la kd-tree para la segunda ronda, con una
muestra pais pero tomando encuenta el voto de la primer ronda.
"""
# -----------------------------------------------------------------------


def kd_tree_segunda_y_primer_pais(cantidad_muestra):
    x1 = generar_muestra_pais_con_segunda(cantidad_muestra)
    y = dividir_entradas_salidas2(x1)
    x1 = escribir_csv2(x1)
    entrenamiento = []
    testeo = []
    corte = 0.67
    leerArchivoCSV_with_header3('testfile.csv', corte, entrenamiento, testeo)
    predicciones = []
    k = 7
    for x in range(len(testeo)):
        neighbors = obtenerVecinos(entrenamiento, testeo[x], k)
        result = obtenerRespuesta(neighbors)
        predicciones.append(result)
    accuracy = obtenerExactitud(testeo, predicciones)
    print('Accuracy: ' + repr(accuracy) + '%')
# -----------------------------------------------------------------------


################################### 8 ##################################
"""
Funcion que genera el kd-tree para la segunda ronda, con una
muestra para provincia pero tomando encuenta el voto de la primer ronda.
"""
# -----------------------------------------------------------------------


def kd_tree_segunda_y_primer_provincia(cantidad_muestra, nombre_provincia):
    x1 = generar_muestra_provincia2(cantidad_muestra, nombre_provincia)
    for i in x1:
        i.insert(0, nombre_provincia)
    y = dividir_entradas_salidas2(x1)
    x1 = escribir_csv2(x1)
    entrenamiento = []
    testeo = []
    corte = 0.67
    leerArchivoCSV_with_header3('testfile.csv', corte, entrenamiento, testeo)
    predicciones = []
    k = 7
    for x in range(len(testeo)):
        neighbors = obtenerVecinos(entrenamiento, testeo[x], k)
        result = obtenerRespuesta(neighbors)
        predicciones.append(result)
    accuracy = obtenerExactitud(testeo, predicciones)
    print('Accuracy: ' + repr(accuracy) + '%')

# -----------------------------------------------------------------------


################################### 9 ##################################
"""
Funcion que genera el kd-tree para la primera ronda, con una
muestra para provincia.
"""
# -----------------------------------------------------------------------


def kd_tree_primera_provincia(cantidad_muestra, nombre_provincia):
    x1 = generar_muestra_provincia(cantidad_muestra, nombre_provincia)
    for i in x1:
        i.insert(0, nombre_provincia)
    y = dividir_entradas_salidas(x1)
    x1 = escribir_csv(x1)
    entrenamiento = []
    testeo = []
    corte = 0.67
    leerArchivoCSV_with_header3('testfile.csv', corte, entrenamiento, testeo)
    predicciones = []
    k = 7
    for x in range(len(testeo)):
        neighbors = obtenerVecinos(entrenamiento, testeo[x], k)
        result = obtenerRespuesta(neighbors)
        predicciones.append(result)
    accuracy = obtenerExactitud(testeo, predicciones)
    print('Accuracy: ' + repr(accuracy) + '%')
# -----------------------------------------------------------------------


################################### 10 ##################################
"""
Funcion que genera el kd-tree para la primera ronda, con una
muestra pias.
"""
# -----------------------------------------------------------------------


def kd_tree_primera_pais(cantidad_muestra):
    x1 = generar_muestra_pais(cantidad_muestra)
    y = dividir_entradas_salidas(x1)
    x1 = escribir_csv(x1)
    entrenamiento = []
    testeo = []
    corte = 0.67
    leerArchivoCSV_with_header3('testfile.csv', corte, entrenamiento, testeo)
    predicciones = []
    k = 7
    for x in range(len(testeo)):
        neighbors = obtenerVecinos(entrenamiento, testeo[x], k)
        result = obtenerRespuesta(neighbors)
        predicciones.append(result)
    accuracy = obtenerExactitud(testeo, predicciones)
    print('Accuracy: ' + repr(accuracy) + '%')
# -----------------------------------------------------------------------


################################### 11 ##################################
"""
Funcion que genera el kd-tree para la segunda ronda, con una
muestra pais.
"""
# -----------------------------------------------------------------------


def kd_tree_segunda_pais(cantidad_muestra):
    x1 = generar_muestra_pais_con_segunda(cantidad_muestra)
    y = dividir_entradas_salidas2(x1)
    x1 = escribir_csv2(x1)
    entrenamiento = []
    testeo = []
    corte = 0.67
    leerArchivoCSV_with_header3('testfile.csv', corte, entrenamiento, testeo)
    predicciones = []
    k = 7
    for x in range(len(testeo)):
        neighbors = obtenerVecinos(entrenamiento, testeo[x], k)
        result = obtenerRespuesta(neighbors)
        predicciones.append(result)
    accuracy = obtenerExactitud(testeo, predicciones)
    print('Accuracy: ' + repr(accuracy) + '%')
# -----------------------------------------------------------------------


################################### 12 ##################################
"""
Funcion que genera el kd-tree para la segunda ronda, con una
muestra para provincia.
"""
# -----------------------------------------------------------------------


def kd_tree_segunda_provincia(cantidad_muestra, nombre_provincia):
    x1 = generar_muestra_provincia2(cantidad_muestra, nombre_provincia)
    for i in x1:
        i.insert(0, nombre_provincia)
    y = dividir_entradas_salidas2(x1)
    x1 = escribir_csv2(x1)
    entrenamiento = []
    testeo = []
    corte = 0.67
    leerArchivoCSV_with_header4('testfile.csv', corte, entrenamiento, testeo)
    predicciones = []
    k = 7
    for x in range(len(testeo)):
        neighbors = obtenerVecinos(entrenamiento, testeo[x], k)
        result = obtenerRespuesta(neighbors)
        predicciones.append(result)
    accuracy = obtenerExactitud(testeo, predicciones)
    print('Accuracy: ' + repr(accuracy) + '%')

# kd_tree_segunda_provincia(1000,"CARTAGO")
# kd_tree_segunda_pais(1000)
# kd_tree_primera_provincia(1000,"CARTAGO")
# kd_tree_primera_pais(1000)
# kd_tree_segunda_y_primer_provincia(1000,"CARTAGO")
# kd_tree_segunda_y_primer_pais(1000)
