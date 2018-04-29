import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt 
plt.rc("font", size = 14)
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

import os
import sys
import csv
import random
import unittest
import numpy as np
from main import *
os . system('ls -lah')

def regresion_logistica_primer_ronda_pais(loss,cantidad_muestra):
    x1 = generar_muestra_pais(cantidad_muestra)
    y = dividir_entradas_salidas(x1)
    x1 = escribir_csv(x1)

    data = pd.read_csv('testfile.csv', encoding='cp1252')
    data = data.dropna()
    #print(data.shape)
    #print(list(data.columns))

    #sns.countplot(x='Edad',data=data, palette='hls')
    #plt.show()
    #sns.countplot(y='Sexo', data=data)
    #plt.show()

    #sns.countplot(y="Voto", data=data)
    #plt.show()

    #data2 = pd.get_dummies(data, columns =['PROVINCIA', 'CANTON', 'Poblacion_total', 'Superficie (km2)', 'Densidad de población','Porcentaje de alfabetismo', 'Escolaridad promedio' 'Hombres', 'Mujeres', 'Porcentaje de población ocupada no asegurada', 'Porcentaje de población nacida en el extranjero', 'Porcentaje de población con discapacidad', 'Porcentaje de población no asegurada', 'Porcentaje de hogares con jefatura femenina', 'Porcentaje de hogares con jefatura compartida','Sexo','Edad','Voto'])
    #data2.drop(data2.columns[[1,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]], axis=1, inplace=True)
    data2 = pd.get_dummies(data, columns =['CANTON', 'Poblacion_total', 'Superficie (km2)', 'Densidad de población','Porcentaje de alfabetismo', 'Porcentaje de población ocupada no asegurada', 'Porcentaje de población nacida en el extranjero', 'Porcentaje de población con discapacidad', 'Porcentaje de población no asegurada', 'Porcentaje de hogares con jefatura femenina', 'Porcentaje de hogares con jefatura compartida','Sexo','Edad','PROVINCIA'])
    #data2.drop(data2.columns[[0]], axis=1, inplace=True)
    data2.columns

    #sns.heatmap(data2.corr())
    #plt.show()

    X = data2.iloc[:,1:]
    y = data2.iloc[:,0]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    classifier = LogisticRegression(loss)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    print(y_pred,len(X_test))
    from sklearn.metrics import confusion_matrix

    confusion_matrix = confusion_matrix(y_test, y_pred)
    print(confusion_matrix)
    print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(classifier.score(X_test, y_test)))

    

def regresion_logistica_primer_ronda_provincia(loss,cantidad_muestra,nombre_provincia):
    x1 = generar_muestra_provincia(cantidad_muestra,nombre_provincia)
    for i in x1:
        i.insert(0, nombre_provincia)
    y = dividir_entradas_salidas(x1)
    x1 = escribir_csv(x1)

    data = pd.read_csv('testfile.csv', encoding='cp1252')
    data = data.dropna()
    data2 = pd.get_dummies(data, columns =['CANTON', 'Poblacion_total', 'Superficie (km2)', 'Densidad de población','Porcentaje de alfabetismo', 'Porcentaje de población ocupada no asegurada', 'Porcentaje de población nacida en el extranjero', 'Porcentaje de población con discapacidad', 'Porcentaje de población no asegurada', 'Porcentaje de hogares con jefatura femenina', 'Porcentaje de hogares con jefatura compartida','Sexo','Edad','PROVINCIA'])
    data2.columns

    X = data2.iloc[:,1:]
    y = data2.iloc[:,0]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    classifier = LogisticRegression(loss)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    from sklearn.metrics import confusion_matrix

    confusion_matrix = confusion_matrix(y_test, y_pred)
    print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(classifier.score(X_test, y_test)))

def regresion_logistica_primer_ronda_provincia(loss,cantidad_muestra,nombre_provincia):
    x1 = generar_muestra_provincia(cantidad_muestra,nombre_provincia)
    for i in x1:
        i.insert(0, nombre_provincia)
    y = dividir_entradas_salidas(x1)
    x1 = escribir_csv(x1)

    data = pd.read_csv('testfile.csv', encoding='cp1252')
    data = data.dropna()
    data2 = pd.get_dummies(data, columns =['CANTON', 'Poblacion_total', 'Superficie (km2)', 'Densidad de población','Porcentaje de alfabetismo', 'Porcentaje de población ocupada no asegurada', 'Porcentaje de población nacida en el extranjero', 'Porcentaje de población con discapacidad', 'Porcentaje de población no asegurada', 'Porcentaje de hogares con jefatura femenina', 'Porcentaje de hogares con jefatura compartida','Sexo','Edad','PROVINCIA'])
    data2.columns

    X = data2.iloc[:,1:]
    y = data2.iloc[:,0]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    classifier = LogisticRegression(loss)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    from sklearn.metrics import confusion_matrix

    confusion_matrix = confusion_matrix(y_test, y_pred)
    print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(classifier.score(X_test, y_test)))

def regresion_logistica_segunda_ronda_pais(loss,cantidad_muestra):
    x1 = generar_muestra_pais_con_segunda(cantidad_muestra)
    y = dividir_entradas_salidas2(x1)
    x1 = escribir_csv2(x1)

    data = pd.read_csv('testfile.csv', encoding='cp1252')
    data = data.dropna()
    data2 = pd.get_dummies(data, columns =['CANTON', 'Poblacion_total', 'Superficie (km2)', 'Densidad de población','Porcentaje de alfabetismo', 'Porcentaje de población ocupada no asegurada', 'Porcentaje de población nacida en el extranjero', 'Porcentaje de población con discapacidad', 'Porcentaje de población no asegurada', 'Porcentaje de hogares con jefatura femenina', 'Porcentaje de hogares con jefatura compartida','Sexo','Edad','Voto primera','PROVINCIA'])
    data2.columns

    X = data2.iloc[:,1:]
    y = data2.iloc[:,0]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    classifier = LogisticRegression(loss)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    from sklearn.metrics import confusion_matrix

    confusion_matrix = confusion_matrix(y_test, y_pred)
    print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(classifier.score(X_test, y_test)))

def regresion_logistica_segunda_ronda_provincia(loss,cantidad_muestra,nombre_provincia):
    x1 = generar_muestra_provincia2(cantidad_muestra,nombre_provincia)
    for i in x1:
        i.insert(0, nombre_provincia)
    y = dividir_entradas_salidas2(x1)
    x1 = escribir_csv2(x1)

    data = pd.read_csv('testfile.csv', encoding='cp1252')
    data = data.dropna()
    data2 = pd.get_dummies(data, columns =['CANTON', 'Poblacion_total', 'Superficie (km2)', 'Densidad de población','Porcentaje de alfabetismo', 'Porcentaje de población ocupada no asegurada', 'Porcentaje de población nacida en el extranjero', 'Porcentaje de población con discapacidad', 'Porcentaje de población no asegurada', 'Porcentaje de hogares con jefatura femenina', 'Porcentaje de hogares con jefatura compartida','Sexo','Edad','PROVINCIA'])
    data2.columns

    X = data2.iloc[:,1:]
    y = data2.iloc[:,0]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    classifier = LogisticRegression(loss)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    from sklearn.metrics import confusion_matrix

    confusion_matrix = confusion_matrix(y_test, y_pred)
    print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(classifier.score(X_test, y_test)))

def regresion_logistica_segunda_y_primera_provincia(loss,cantidad_muestra,nombre_provincia):
    x1 = generar_muestra_provincia2(cantidad_muestra,nombre_provincia)
    for i in x1:
        i.insert(0, nombre_provincia)
    y = dividir_entradas_salidas2(x1)
    x1 = escribir_csv2(x1)

    data = pd.read_csv('testfile.csv', encoding='cp1252')
    data = data.dropna()
    data2 = pd.get_dummies(data, columns =['CANTON', 'Poblacion_total', 'Superficie (km2)', 'Densidad de población','Porcentaje de alfabetismo', 'Porcentaje de población ocupada no asegurada', 'Porcentaje de población nacida en el extranjero', 'Porcentaje de población con discapacidad', 'Porcentaje de población no asegurada', 'Porcentaje de hogares con jefatura femenina', 'Porcentaje de hogares con jefatura compartida','Sexo','Edad','Voto primera','PROVINCIA'])
    data2.columns

    X = data2.iloc[:,1:]
    y = data2.iloc[:,0]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    classifier = LogisticRegression(loss)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    from sklearn.metrics import confusion_matrix

    confusion_matrix = confusion_matrix(y_test, y_pred)
    print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(classifier.score(X_test, y_test)))

def regresion_logistica_segunda_y_primera_pais(loss,cantidad_muestra):
    x1 = generar_muestra_pais_con_segunda(cantidad_muestra)
    y = dividir_entradas_salidas2(x1)
    x1 = escribir_csv2(x1)

    data = pd.read_csv('testfile.csv', encoding='cp1252')
    data = data.dropna()
    data2 = pd.get_dummies(data, columns =['CANTON', 'Poblacion_total', 'Superficie (km2)', 'Densidad de población','Porcentaje de alfabetismo', 'Porcentaje de población ocupada no asegurada', 'Porcentaje de población nacida en el extranjero', 'Porcentaje de población con discapacidad', 'Porcentaje de población no asegurada', 'Porcentaje de hogares con jefatura femenina', 'Porcentaje de hogares con jefatura compartida','Sexo','Edad','Voto primera','PROVINCIA'])
    data2.columns

    X = data2.iloc[:,1:]
    y = data2.iloc[:,0]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    classifier = LogisticRegression(loss)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    from sklearn.metrics import confusion_matrix

    confusion_matrix = confusion_matrix(y_test, y_pred)
    print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(classifier.score(X_test, y_test)))

#print(regresion_logistica_segunda_ronda_pais('l1',10000))
#print(regresion_logistica_primer_ronda_pais('l1',10000))
#print(regresion_logistica_segunda_ronda_provincia('l1',10000,'SAN JOSE'))
#print(regresion_logistica_primer_ronda_provincia('l2',10000,'SAN JOSE'))
#print(regresion_logistica_segunda_y_primera_provincia('l1',10000,'SAN JOSE'))
#print(regresion_logistica_segunda_y_primera_pais('l1',10000))
