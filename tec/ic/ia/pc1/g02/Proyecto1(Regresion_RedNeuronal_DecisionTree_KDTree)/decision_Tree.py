"""
==========================================================================

Proyecto #1 ­ Simulador Votantes(Arbol de desicion)

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
from random import randrange
# -----------------------------------------------------------------------

################################### 1 ##################################
"""
Funcion que emplea el metodo cross validation para obtener las divisiones
correspondientes de los datos de entrada.
"""
# -----------------------------------------------------------------------


def divisiones_cross_validation(dataset, cortes):
    dataset_split = []
    copia_dataset = list(dataset)
    tamano_corte = int(len(dataset) / cortes)
    for i in range(cortes):
        corte = []
        while len(corte) < tamano_corte:
            indice = randrange(len(copia_dataset))
            corte.append(copia_dataset.pop(indice))
        dataset_split.append(corte)
    return dataset_split
# -----------------------------------------------------------------------


################################### 2 ##################################
"""
Funcion que no permite calcular el accuracy de los datos.
"""
# -----------------------------------------------------------------------


def exactitud(actual, predicted):
    correctos = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correctos += 1
    return correctos / float(len(actual)) * 100.0
# -----------------------------------------------------------------------


################################### 3 ##################################
"""
Funcion que nos devuelve dos conjuntos de datos para la prueba.
"""
# -----------------------------------------------------------------------
def prueba_particion(indice, valor, dataset):
    izq, der = [], []
    for i in dataset:
        if i[indice] < valor:
            izq.append(i)
        else:
            der.append(i)
    return izq, der
# -----------------------------------------------------------------------


################################### 4 ##################################
"""
Funcion que nos permite calcular la ganancia que se obtine de cada dato.
"""
# -----------------------------------------------------------------------


def ganancia(grupos, tipos):
    cortes = float(sum([len(subgrupo) for subgrupo in grupos]))
    result = 0.0
    for subgrupo in grupos:
        largo = float(len(subgrupo))
        if largo == 0:
            continue
        puntuacion = 0.0
        for i in tipos:
            puntos = [j[-1] for j in subgrupo].count(i) / largo
            puntuacion += puntos * puntos
        result += (1.0 - puntuacion) * (largo / cortes)
    return result
# -----------------------------------------------------------------------


################################### 5 ##################################
"""
Funcion que selecciona el mejor punto de corte en los datos y nos genera
un diccionario con los datos respectivos.
"""
# -----------------------------------------------------------------------


def hacer_corte(dataset):
    valor_tipo = list(set(i[-1] for i in dataset))
    indice, valor, puntuacion, grupo = 999, 999, 999, None
    for i in range(len(dataset[0]) - 1):
        for j in dataset:
            grupos = prueba_particion(i, j[i], dataset)
            ganado = ganancia(grupos, valor_tipo)
            if ganado < puntuacion:
                indice, valor, puntuacion, grupo = i, j[i], ganado, grupos
    return {'i': indice, 'valor': valor, 'grupos': grupo}
# -----------------------------------------------------------------------


################################### 6 ##################################
"""
Funcion que selecciona la salida mas comun una sublista.
"""
# -----------------------------------------------------------------------


def valorfinal_nodo(grupo):
    salidas = [i[-1] for i in grupo]
    return max(set(salidas), key=salidas.count)
# -----------------------------------------------------------------------


################################### 7 ##################################
"""
Funcion que va diviediendo los nodos y separandolos en etiquetas formando
un conjunto de nodos.
"""
# -----------------------------------------------------------------------


def dividir(nodo, max_profun, tamano, profundidad):
    izq, der = nodo['grupos']
    del(nodo['grupos'])

    if not izq or not der:
        nodo['izq'] = nodo['der'] = valorfinal_nodo(izq + der)
        return

    if profundidad >= max_profun:
        nodo['izq'], nodo['der'] = valorfinal_nodo(izq), valorfinal_nodo(der)
        return

    if len(izq) <= tamano:
        nodo['izq'] = valorfinal_nodo(izq)
    else:
        nodo['izq'] = hacer_corte(izq)
        dividir(nodo['izq'], max_profun, tamano, profundidad + 1)

    if len(der) <= tamano:
        nodo['der'] = valorfinal_nodo(der)
    else:
        nodo['der'] = hacer_corte(der)
        dividir(nodo['der'], max_profun, tamano, profundidad + 1)
# -----------------------------------------------------------------------


################################### 8 ##################################
"""
Funcion que nos construye el arbol de decision.
"""
# -----------------------------------------------------------------------


def creaar_arbol(entrenamineto, max_profun, tamano):
    raiz = hacer_corte(entrenamineto)
    dividir(raiz, max_profun, tamano, 1)
    return raiz
# -----------------------------------------------------------------------


################################### 9 ##################################
"""
Funcion que nos predice los datos apartir del arbol de decision.
"""
# -----------------------------------------------------------------------


def predecir(nodo, fila):
    if fila[nodo['i']] < nodo['valor']:
        if isinstance(nodo['izq'], dict):
            return predecir(nodo['izq'], fila)
        else:
            return nodo['izq']
    else:
        if isinstance(nodo['der'], dict):
            return predecir(nodo['der'], fila)
        else:
            return nodo['der']
 # -----------------------------------------------------------------------


################################### 10 ##################################
"""
Funcion que nos genera arbol con preddiones.
"""
# -----------------------------------------------------------------------


def arbol_decision(train, test, max_profun, tamano):
    arbol = creaar_arbol(train, max_profun, tamano)
    predicciones = []
    for i in test:
        prediccion = predecir(arbol, i)
        predicciones.append(prediccion)
    return(predicciones)
# -----------------------------------------------------------------------


################################### 11 ##################################
"""
Funcion que nos permite conocer cuales son los puntaciones de los datos
generados.
"""
# -----------------------------------------------------------------------


def general(dataset, algorithm, cortes, *args):
    tempo = divisiones_cross_validation(dataset, cortes)
    puntuaciones = []
    for i in tempo:
        train_set = list(tempo)
        train_set.remove(i)
        train_set = sum(train_set, [])
        test_set = []
        for j in i:
            j_copy = list(j)
            test_set.append(j_copy)
            j_copy[-1] = None
        predicted = algorithm(train_set, test_set, *args)
        actual = [j[-1] for j in i]
        exact = exactitud(actual, predicted)
        puntuaciones.append(exact)
    return puntuaciones
# -----------------------------------------------------------------------


################################### 12 ##################################
"""
Funcion que genera la arbol de decision para la segunda ronda, con una
muestra pais pero tomando encuenta el voto de la primer ronda.
"""
# -----------------------------------------------------------------------


def decision_tree_segunda_y_primer_pais(cantidad_muestra):
    x1 = generar_muestra_pais_con_segunda(cantidad_muestra)
    y = dividir_entradas_salidas2(x1)
    x1 = escribir_csv2(x1)
    dataset = leerArchivoCSV_with_header2('testfile.csv')
    dataset = dataset[1:]
    data = []
    for i in dataset:
        data += [[i[-1], i[1], i[-4], i[-2], i[0]]]
    dataset = []
    acum = []
    for i in data:
        for j in i:
            j = int(j)
            acum += [j]
        dataset += [acum]
        acum = []
    n_folds = 5
    max_depth = 10
    min_size = 10
    scores = general(dataset, arbol_decision, n_folds, max_depth, min_size)
    print('Scores: %s' % scores)
    print('Mean Accuracy: %.3f%%' % (sum(scores) / float(len(scores))))
    return 0
# -----------------------------------------------------------------------


################################### 13 ##################################
"""
Funcion que genera el arbol de desicion para la segunda ronda, con una
muestra para provincia pero tomando encuenta el voto de la primer ronda.
"""
# -----------------------------------------------------------------------


def decision_tree_segunda_y_primer_provincia(
        cantidad_muestra, nombre_provincia):
    x1 = generar_muestra_provincia2(cantidad_muestra, nombre_provincia)
    for i in x1:
        i.insert(0, nombre_provincia)
    y = dividir_entradas_salidas2(x1)
    x1 = escribir_csv2(x1)
    dataset = leerArchivoCSV_with_header2('testfile.csv')
    dataset = dataset[1:]
    data = []
    for i in dataset:
        data += [[i[-1], i[1], i[-4], i[-2], i[0]]]
    dataset = []
    acum = []
    for i in data:
        for j in i:
            j = int(j)
            acum += [j]
        dataset += [acum]
        acum = []
    n_folds = 5
    max_depth = 10
    min_size = 10
    scores = general(dataset, arbol_decision, n_folds, max_depth, min_size)
    print('Scores: %s' % scores)
    print('Mean Accuracy: %.3f%%' % (sum(scores) / float(len(scores))))
    return 0
# -----------------------------------------------------------------------


################################### 13 ##################################
"""
Funcion que genera el arbol desicion para la primera ronda, con una
muestra para provincia.
"""
# -----------------------------------------------------------------------


def decision_tree_primera_provincia(cantidad_muestra, nombre_provincia):
    x1 = generar_muestra_provincia(cantidad_muestra, nombre_provincia)
    for i in x1:
        i.insert(0, nombre_provincia)
    y = dividir_entradas_salidas(x1)
    x1 = escribir_csv(x1)
    dataset = leerArchivoCSV_with_header2('testfile.csv')
    dataset = dataset[1:]
    data = []
    for i in dataset:
        data += [[i[-1], i[1], i[-3], i[-2], i[0]]]
    dataset = []
    acum = []
    for i in data:
        for j in i:
            j = int(j)
            acum += [j]
        dataset += [acum]
        acum = []
    n_folds = 5
    max_depth = 10
    min_size = 10
    scores = general(dataset, arbol_decision, n_folds, max_depth, min_size)
    print('Scores: %s' % scores)
    print('Mean Accuracy: %.3f%%' % (sum(scores) / float(len(scores))))
    return 0
# -----------------------------------------------------------------------


################################### 14 ##################################
"""
Funcion que genera el arbol de decision para la primera ronda, con una
muestra pias.
"""
# -----------------------------------------------------------------------


def decision_tree_primera_pais(cantidad_muestra):
    x1 = generar_muestra_pais(cantidad_muestra)
    y = dividir_entradas_salidas(x1)
    x1 = escribir_csv(x1)
    dataset = leerArchivoCSV_with_header2('testfile.csv')
    dataset = dataset[1:]
    data = []
    for i in dataset:
        data += [[i[-1], i[1], i[-3], i[-2], i[0]]]
    dataset = []
    acum = []
    for i in data:
        for j in i:
            j = int(j)
            acum += [j]
        dataset += [acum]
        acum = []
    n_folds = 5
    max_depth = 10
    min_size = 10
    scores = general(dataset, arbol_decision, n_folds, max_depth, min_size)
    print('Scores: %s' % scores)
    print('Mean Accuracy: %.3f%%' % (sum(scores) / float(len(scores))))
    return 0
# -----------------------------------------------------------------------


################################### 15 ##################################
"""
Funcion que genera el arbol de desicion para la segunda ronda, con una
muestra pais.
"""
# -----------------------------------------------------------------------


def decision_tree_segunda_pais(cantidad_muestra):
    x1 = generar_muestra_pais_con_segunda(cantidad_muestra)
    y = dividir_entradas_salidas2(x1)
    x1 = escribir_csv2(x1)
    dataset = leerArchivoCSV_with_header2('testfile.csv')
    dataset = dataset[1:]
    data = []
    for i in dataset:
        data += [[i[-1], i[1], i[-3], i[-2], i[0]]]
    dataset = []
    acum = []
    for i in data:
        for j in i:
            j = int(j)
            acum += [j]
        dataset += [acum]
        acum = []
    n_folds = 5
    max_depth = 10
    min_size = 10
    scores = general(dataset, arbol_decision, n_folds, max_depth, min_size)
    print('Scores: %s' % scores)
    print('Mean Accuracy: %.3f%%' % (sum(scores) / float(len(scores))))
    return 0
# -----------------------------------------------------------------------


################################### 16 ##################################
"""
Funcion que genera el arbol de desicion para la segunda ronda, con una
muestra para provincia.
"""
# -----------------------------------------------------------------------


def decision_tree_segunda_provincia(cantidad_muestra, nombre_provincia):
    x1 = generar_muestra_provincia2(cantidad_muestra, nombre_provincia)
    for i in x1:
        i.insert(0, nombre_provincia)
    y = dividir_entradas_salidas2(x1)
    x1 = escribir_csv2(x1)
    dataset = leerArchivoCSV_with_header2('testfile.csv')
    dataset = dataset[1:]
    data = []
    for i in dataset:
        data += [[i[-1], i[1], i[-3], i[-2], i[0]]]
    dataset = []
    acum = []
    for i in data:
        for j in i:
            j = int(j)
            acum += [j]
        dataset += [acum]
        acum = []
    n_folds = 5
    max_depth = 10
    min_size = 10
    scores = general(dataset, arbol_decision, n_folds, max_depth, min_size)
    print('Scores: %s' % scores)
    print('Mean Accuracy: %.3f%%' % (sum(scores) / float(len(scores))))
    return 0


# print(decision_tree_segunda_y_primer_pais(1000))
# print(decision_tree_segunda_y_primer_provincia(1000,"CARTAGO"))
# print(decision_tree_primera_provincia(1000,"CARTAGO"))
# print(decision_tree_primera_pais(1000))
# print(decision_tree_segunda_pais(1000))
print(decision_tree_segunda_provincia(1000, "CARTAGO"))
