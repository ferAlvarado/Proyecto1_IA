"""
==========================================================================

Proyecto #1 ­ Simulador Votantes(red neuronal)

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
from keras.layers import Dense, Dropout, Activation
import numpy as np
import keras
import csv
import pandas as pd
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import adam, sgd
from main import *
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
# -----------------------------------------------------------------------

################################### 1 ##################################
"""
Funcion que genera la red neuronal para la primera ronda, con una
muestra pias.
"""
# -----------------------------------------------------------------------


def red_neuronal_primer_ronda_pais(cantidad_muestra):
    x1 = generar_muestra_pais(cantidad_muestra)
    y = dividir_entradas_salidas(x1)
    x1 = escribir_csv3(x1)
    from numpy import genfromtxt
    my_data = genfromtxt('testfile.csv', delimiter=',', encoding='cp1252')
    x = []
    y = []
    for i in my_data:
        x += [[i[-1], i[1], i[-3], i[-2], i[4], i[5], i[8], i[9]]]
        y += [[i[0]]]
    x = np.array(x)
    y = np.array(y)

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, random_state=0)
    y_train = keras.utils.to_categorical(y_train, num_classes=150)
    y_test = keras.utils.to_categorical(y_test, num_classes=150)

    model = Sequential()
    model.add(Dense(64, activation='softmax', input_dim=8))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='softmax'))
    model.add(Dropout(0.5))
    model.add(Dense(150, activation='softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    model.fit(x_train, y_train,
              epochs=1000,
              batch_size=128, verbose=0)
    score = model.evaluate(x_test, y_test, verbose=0, batch_size=128)
    print("Loss:", score[0], " Accuracy:", score[1])
    return
# -----------------------------------------------------------------------


################################### 2 ##################################
"""
Funcion que genera la red neuronal para la primera ronda, con una
muestra para provincia.
"""
# -----------------------------------------------------------------------


def red_neuronal_primer_ronda_provincia(cantidad_muestra, nombre_provincia):
    x1 = generar_muestra_provincia(cantidad_muestra, nombre_provincia)
    for i in x1:
        i.insert(0, nombre_provincia)
    y = dividir_entradas_salidas(x1)
    x1 = escribir_csv3(x1)
    from numpy import genfromtxt
    my_data = genfromtxt('testfile.csv', delimiter=',', encoding='cp1252')
    x = []
    y = []
    for i in my_data:
        x += [[i[-1], i[1], i[-3], i[-2], i[4], i[5], i[8], i[9]]]
        y += [[i[0]]]
    x = np.array(x)
    y = np.array(y)

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, random_state=0)
    y_train = keras.utils.to_categorical(y_train, num_classes=150)
    y_test = keras.utils.to_categorical(y_test, num_classes=150)

    model = Sequential()
    model.add(Dense(64, activation='softmax', input_dim=8))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='softmax'))
    model.add(Dropout(0.5))
    model.add(Dense(150, activation='softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    model.fit(x_train, y_train,
              epochs=1000,
              batch_size=128, verbose=0)
    score = model.evaluate(x_test, y_test, verbose=0, batch_size=128)
    print("Loss:", score[0], " Accuracy:", score[1])
    return
# -----------------------------------------------------------------------


################################### 3 ##################################
"""
Funcion que genera la red neuronal para la segunda ronda, con una
muestra pais.
"""
# -----------------------------------------------------------------------


def red_neuronal_segunda_ronda_pais(cantidad_muestra):
    x1 = generar_muestra_pais_con_segunda(cantidad_muestra)
    y = dividir_entradas_salidas2(x1)
    x1 = escribir_csv4(x1)
    from numpy import genfromtxt
    my_data = genfromtxt('testfile.csv', delimiter=',', encoding='cp1252')
    x = []
    y = []
    for i in my_data:
        x += [[i[-1], i[1], i[-4], i[-3], i[4], i[5], i[8], i[9]]]
        y += [[i[0]]]
    x = np.array(x)
    y = np.array(y)

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, random_state=0)
    y_train = keras.utils.to_categorical(y_train, num_classes=150)
    y_test = keras.utils.to_categorical(y_test, num_classes=150)

    model = Sequential()
    model.add(Dense(64, activation='softmax', input_dim=9))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='softmax'))
    model.add(Dropout(0.5))
    model.add(Dense(150, activation='softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    model.fit(x_train, y_train,
              epochs=1000,
              batch_size=128, verbose=0)
    score = model.evaluate(x_test, y_test, verbose=0, batch_size=128)
    print("Loss:", score[0], " Accuracy:", score[1])
    return
# -----------------------------------------------------------------------


################################### 4 ##################################
"""
Funcion que genera la red neuronal para la segunda ronda, con una
muestra para provincia.
"""
# -----------------------------------------------------------------------


def red_neuronal_segunda_ronda_provincia(cantidad_muestra, nombre_provincia):
    x1 = generar_muestra_provincia2(cantidad_muestra, nombre_provincia)
    for i in x1:
        i.insert(0, nombre_provincia)
    y = dividir_entradas_salidas2(x1)
    x1 = escribir_csv4(x1)
    from numpy import genfromtxt
    my_data = genfromtxt('testfile.csv', delimiter=',', encoding='cp1252')
    x = []
    y = []
    for i in my_data:
        x += [[i[-1], i[1], i[-4], i[-3], i[4], i[5], i[8], i[9]]]
        y += [[i[0]]]
    x = np.array(x)
    y = np.array(y)

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, random_state=0)
    y_train = keras.utils.to_categorical(y_train, num_classes=150)
    y_test = keras.utils.to_categorical(y_test, num_classes=150)

    model = Sequential()
    model.add(Dense(64, activation='softmax', input_dim=9))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='softmax'))
    model.add(Dropout(0.5))
    model.add(Dense(150, activation='softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    model.fit(x_train, y_train,
              epochs=1000,
              batch_size=128, verbose=0)
    score = model.evaluate(x_test, y_test, verbose=0, batch_size=128)
    print("Loss:", score[0], " Accuracy:", score[1])
    return
# -----------------------------------------------------------------------

################################### 5 ##################################
"""
Funcion que genera la red neuronal para la segunda ronda, con una
muestra para provincia pero tomando encuenta el voto de la primer ronda.
"""
# -----------------------------------------------------------------------


def red_neuronal_segunda_y_primera_provincia(
        cantidad_muestra, nombre_provincia):
    x1 = generar_muestra_provincia2(cantidad_muestra, nombre_provincia)
    for i in x1:
        i.insert(0, nombre_provincia)
    y = dividir_entradas_salidas2(x1)
    x1 = escribir_csv4(x1)
    from numpy import genfromtxt
    my_data = genfromtxt('testfile.csv', delimiter=',', encoding='cp1252')
    x = []
    y = []
    for i in my_data:
        x += [[i[-1], i[1], i[-2], i[-4], i[-3], i[4], i[5], i[8], i[9]]]
        y += [[i[0]]]
    x = np.array(x)
    y = np.array(y)

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, random_state=0)
    y_train = keras.utils.to_categorical(y_train, num_classes=150)
    y_test = keras.utils.to_categorical(y_test, num_classes=150)

    model = Sequential()
    model.add(Dense(64, activation='softmax', input_dim=9))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='softmax'))
    model.add(Dropout(0.5))
    model.add(Dense(150, activation='softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    model.fit(x_train, y_train,
              epochs=1000,
              batch_size=128, verbose=0)
    score = model.evaluate(x_test, y_test, verbose=0, batch_size=128)
    print("Loss:", score[0], " Accuracy:", score[1])
    return
# -----------------------------------------------------------------------

################################### 6 ##################################
"""
Funcion que genera la red neuronal para la segunda ronda, con una
muestra pais pero tomando encuenta el voto de la primer ronda.
"""
# -----------------------------------------------------------------------


def red_neuronal_segunda_y_primera_pais(cantidad_muestra):
    x1 = generar_muestra_pais_con_segunda(cantidad_muestra)
    y = dividir_entradas_salidas2(x1)
    x1 = escribir_csv4(x1)
    from numpy import genfromtxt
    my_data = genfromtxt('testfile.csv', delimiter=',', encoding='cp1252')
    x = []
    y = []
    for i in my_data:
        x += [[i[-1], i[1], i[-2], i[-4], i[-3], i[4], i[5], i[8], i[9]]]
        y += [[i[0]]]
    x = np.array(x)
    y = np.array(y)

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, random_state=0)
    y_train = keras.utils.to_categorical(y_train, num_classes=150)
    y_test = keras.utils.to_categorical(y_test, num_classes=150)

    model = Sequential()
    model.add(Dense(64, activation='softmax', input_dim=9))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='softmax'))
    model.add(Dropout(0.5))
    model.add(Dense(150, activation='softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    model.fit(x_train, y_train,
              epochs=1000,
              batch_size=128, verbose=0)
    score = model.evaluate(x_test, y_test, verbose=0, batch_size=128)
    print("Loss:", score[0], " Accuracy:", score[1])
    return

#red_neuronal_primer_ronda_pais(1000)
#red_neuronal_primer_ronda_provincia(1000,'SAN JOSE')
#red_neuronal_segunda_ronda_pais(1000)
#red_neuronal_segunda_ronda_provincia(1000,'CARTAGO')
#red_neuronal_segunda_y_primera_provincia(1000,'CARTAGO')
#red_neuronal_segunda_y_primera_pais(1000)
