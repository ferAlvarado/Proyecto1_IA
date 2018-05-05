"""
=====================================
Proyecto Corto #1 ­ Simulador Votantes
        (Modulo unittest)
=====================================
:Institucion: Instituto Tecnologico de Costa Rica
:Curso: Inteligencia Artificial
:Grupo: 1
:Semestre: I Semestre 2018
:Autores: Fernanda Alvarado Vargas,fernadaalvarado95@gmail.com
          Minor Sancho Valverde,tivin.minor10@gmail.com
          Freyser Jimenez Mena, fjimenez577@gmail.com
:Fecha: 25/04/2018

Dependencias con archivos de entrada:
- datos.csv
"""
#-----------------------------------------------------------------------
import os
import sys
import csv
import random
import unittest
from kd_tree import *
from decision_Tree import *
os . system('ls -lah')
#-----------------------------------------------------------------------
######################  Clase de testeo  ##################################

class TestUM(unittest.TestCase):
   
    def setUp(self):
        pass
    
    ################################### 1 ##################################
    """
    Funcion de testeo para kd_tree_segunda_y_primer_pais que genera los votos pais.
    input: int
    output: int
    """
    def test_kd_tree_segunda_y_primer_pais(self):
        print("__________________________________________________________________\n")
        print("Test : test_kd_tree_segunda_y_primer_pais")
        resultado = 0.5
        num = 1000
        porcentaje = 20
        k = 7
        self.assertGreaterEqual(kd_tree_segunda_y_primer_pais(num,porcentaje,k), resultado)	
        print("Input:")
        print("Muestra: "+str(num) +" y %"+ str(porcentaje)+" y K: "+ str(k))
        print("Output:")
        print(resultado)
    ################################### 2 ##################################
    """
    Funcion de testeo para kd_tree_segunda_y_primer_provincia que genera los votos pais.
    input: int,string
    output: int
    """
    def test_kd_tree_segunda_y_primer_provincia(self):
        print("__________________________________________________________________\n")
        print("Test : test_kd_tree_segunda_y_primer_provincia")
        resultado = 0.6
        porcentaje = 20
        k = 7
        num = 1000
        pro = "CARTAGO"
        self.assertGreaterEqual(kd_tree_segunda_y_primer_provincia(num,pro,porcentaje,k), resultado)	
        print("Input:")
        print("Muestra: "+str(num) +" y Provincia: "+pro +" y %"+ str(porcentaje)+" y K: "+ str(k))
        print("Output:")
        print(">= ",resultado)
    ################################### 3 ##################################
    """
    Funcion de testeo para kd_tree_primera_provincia que genera los votos pais.
    input: int,string
    output: int
    """
    def test_kd_tree_primera_provincia(self):
        print("__________________________________________________________________\n")
        print("Test : test_kd_tree_primera_provincia")
        resultado = 0.2
        num = 1000
        porcentaje = 20
        k = 7
        pro = "CARTAGO"
        self.assertGreaterEqual(kd_tree_primera_provincia(num,pro,porcentaje,k), resultado)	
        print("Input:")
        print("Muestra: "+str(num) +" y Provincia: "+pro +" y %"+ str(porcentaje)+" y K: "+ str(k))
        print("Output:")
        print(">= ",resultado)
    ################################### 4 ##################################
    """
    Funcion de testeo para kd_tree_primera_pais que genera los votos pais.
    input: int
    output: int
    """
    def test_kd_tree_primera_pais(self):
        print("__________________________________________________________________\n")
        print("Test : test_kd_tree_primera_pais")
        resultado = 0.2
        num = 1000
        porcentaje = 20
        k = 7
        self.assertGreaterEqual(kd_tree_primera_pais(num,porcentaje,k), resultado)	
        print("Input:")
        print("Muestra: "+str(num) +" y %"+ str(porcentaje)+" y K: "+ str(k))
        print("Output:")
        print(">=",resultado)

    ################################### 5 ##################################
    """
    Funcion de testeo para kd_tree_segunda_pais que genera los votos pais.
    input: int
    output: int
    """
    def test_kd_tree_segunda_pais(self):
        print("__________________________________________________________________\n")
        print("Test : test_kd_tree_segunda_pais")
        resultado = 0.5
        num = 1000
        porcentaje = 20
        k = 7
        self.assertGreaterEqual(kd_tree_segunda_pais(num,porcentaje,k), resultado)	
        print("Input:")
        print("Muestra: "+str(num)+pro +" y %"+ str(porcentaje)+" y K: "+ str(k))
        print("Output:")
        print(">=",resultado)

    ################################### 6 ##################################
    """
    Funcion de testeo para kd_tree_segunda_provincia que genera los votos pais.
    input: int,string
    output: int
    """
    def test_kd_tree_segunda_provincia(self):
        print("__________________________________________________________________\n")
        print("Test : test_kd_tree_segunda_provincia")
        resultado = 0.65
        num = 1000
        porcentaje = 20
        k = 7
        pro = "CARTAGO"
        self.assertGreaterEqual(kd_tree_segunda_provincia(num,pro,porcentaje,k), resultado)	
        print("Input:")
        print("Muestra: "+str(num) +" y Provincia: "+pro +" y %"+ str(porcentaje)+" y K: "+ str(k))
        print("Output:")
        print(">= ",resultado)
    ################################### 7 ##################################
    """
    Funcion de testeo para decision_tree_segunda_y_primer_pais que genera los votos pais.
    input: int
    output: int
    """
    def test_decision_tree_segunda_y_primer_pais(self):
        print("__________________________________________________________________\n")
        print("Test : test_decision_tree_segunda_y_primer_pais")
        resultado = 0.57
        num = 100
        porcentaje = 20
        k = 7
        self.assertGreaterEqual(decision_tree_segunda_y_primer_pais(num,porcentaje,k), resultado)	
        print("Input:")
        print("Muestra: "+str(num)+" y %"+ str(porcentaje)+" y Umbral: "+ str(k))
        print("Output:")
        print(">=",resultado)
    ################################### 8 ##################################
    """
    Funcion de testeo para decision_tree_segunda_y_primer_provincia que genera los votos pais.
    input: int,string
    output: int
    """
    def test_decision_tree_segunda_y_primer_provincia(self):
        print("__________________________________________________________________\n")
        print("Test : test_decision_tree_segunda_y_primer_provincia")
        resultado = 0.7
        num = 100
        pro = "CARTAGO"
        porcentaje = 20
        k = 7
        self.assertGreaterEqual(decision_tree_segunda_y_primer_provincia(num,pro,porcentaje,k), resultado)	
        print("Input:")
        print("Muestra: "+str(num) +" y Provincia: "+pro +" y %"+ str(porcentaje)+" y Umbral: "+ str(k))
        print("Output:")
        print(">= ",resultado)
    ################################### 9 ##################################
    """
    Funcion de testeo para decision_tree_primera_provincia que genera los votos pais.
    input: int,string
    output: int
    """
    def test_decision_tree_primera_provincia(self):
        print("__________________________________________________________________\n")
        print("Test : test_decision_tree_primera_provincia")
        resultado = 0.18
        num = 100
        pro = "CARTAGO"
        porcentaje = 20
        k = 7
        self.assertGreaterEqual(decision_tree_primera_provincia(num,pro,porcentaje,k), resultado)	
        print("Input:")
        print("Muestra: "+str(num) +" y Provincia: "+pro +" y %"+ str(porcentaje)+" y Umbral: "+ str(k))
        print("Output:")
        print(">= ",resultado)
    ################################### 10 ##################################
    """
    Funcion de testeo para decision_tree_primera_pais que genera los votos pais.
    input: int
    output: int
    """
    def test_decision_tree_primera_pais(self):
        print("__________________________________________________________________\n")
        print("Test : test_decision_tree_primera_pais")
        resultado = 0.25
        num = 100
        porcentaje = 20
        k = 7
        self.assertGreaterEqual(decision_tree_primera_pais(num,porcentaje,k), resultado)	
        print("Input:")
        print("Muestra: "+str(num) +" y %"+ str(porcentaje)+" y Umbral: "+ str(k))
        print("Output:")
        print(">=",resultado)
    ################################### 11 ##################################
    """
    Funcion de testeo para decision_tree_segunda_pais que genera los votos pais.
    input: int
    output: int
    """
    def test_decision_tree_segunda_pais(self):
        print("__________________________________________________________________\n")
        print("Test : test_decision_tree_segunda_pais")
        resultado = 0.5
        num = 100
        porcentaje = 20
        k = 7
        self.assertGreaterEqual(decision_tree_segunda_pais(num,porcentaje,k), resultado)	
        print("Input:")
        print("Muestra: "+str(num) +" y %"+ str(porcentaje)+" y Umbral: "+ str(k))
        print("Output:")
        print(">=",resultado)
    ################################### 12 ##################################
    """
    Funcion de testeo para decision_tree_segunda_provincia que genera los votos pais.
    input: int,string
    output: int
    """
    def test_decision_tree_segunda_provincia(self):
        print("__________________________________________________________________\n")
        print("Test : test_decision_tree_segunda_provincia")
        resultado = 0.6
        num = 100
        pro = "CARTAGO"
        porcentaje = 20
        k = 7
        self.assertGreaterEqual(decision_tree_segunda_provincia(num,pro,porcentaje,k), resultado)	
        print("Input:")
        print("Muestra: "+str(num) +" y Provincia: "+pro +" y %"+ str(porcentaje)+" y Umbral: "+ str(k))
        print("Output:")
        print(">= ",resultado)
 
        
if __name__ == '__main__':
    unittest.main()
