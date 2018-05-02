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
from main import *
os . system('ls -lah')
leerArchivoCSV("datos.csv")
lista_catones = cargar_datos_cantones("CARTAGO")
lista_votos_totales = calcular_cantidad_voto_por_canton(lista_catones)
lista_aleatorio = aleatorio(500,"CARTAGO")
votos_provincia = obtener_votos_cada_provincias()
promedio_votos_x_provincia = promedio_votos_por_provincia()
print()
#-----------------------------------------------------------------------

######################  Clase de testeo  ##################################

class TestUM(unittest.TestCase):
   
    def setUp(self):
        pass
    ################################### 1 ##################################
    """
    Funcion de testeo para leerArchivoCSV que lee el archivo y almacena los datos en variable global total
    input:
    output: bool
    """
    def test_leerArchivoCSV(self):
            print("__________________________________________________________________\n")
            print("Test : leerArchivoCSV()")
            print("__________________________________________________________________")
            self.assertTrue(leerArchivoCSV("datos.csv"))

    ################################### 2 ##################################
    """
    Funcion de testeo para sumar_todos_por_provincia que esta funcion suma todos los votos para cada partido en una provincia determinada
    input: string
    output: lista de sublistas
    """
    def test_sumar_todos_por_provincia(self):
            print("__________________________________________________________________\n")
            print("Test : sumar_todos_por_provincia(provincia)")
            resultado = ['CARTAGO', [1061, 72528, 5920, 527, 2097, 29839, 55344, 2814, 2361, 1955, 17464, 41211, 41337, 3401, 685], 278544]
            self.assertEqual(sumar_todos_por_provincia("CARTAGO"),resultado)
            print("Input:")
            print("CARTAGO")
            print("Output:")
            print(resultado)

    ################################### 3 ##################################
    """
    Funcion de testeo para test_cargar_datos_cantones que carga los datos referentes a los cantones para una provincia dada.
    input: string
    output: lista de sublistas 
    """
    def test_cargar_datos_cantones(self):
            print("__________________________________________________________________\n")
            print("Test : cargar_datos_cantones(nombre_provincia)")
            self.assertEqual(cargar_datos_cantones("CARTAGO"),[['CARTAGO', 'CARTAGO CENTRAL', 270, 24665, 3295, 174, 575, 9491, 19042, 951, 856, 613, 5269, 10318, 13872, 1108, 184, 147898, 287.8, 514, 88.7, 96.1, 43.9, 36618, 3.8, 74.1, 2.9, 98.4, 99.3, 97.9, 9, 9.8, 7.6, 34.3, 19.1, 89.4, 51.9, 9.2, 46.8, 53.2, 72.2, 35.3, 13.7, 3.9, 8.6, 13.9, 28.7, 6.4], ['CARTAGO', 'PARAISO', 212, 8478, 421, 69, 268, 6342, 5418, 316, 269, 282, 2872, 4613, 3900, 460, 89, 57743, 411.9, 140, 76.9, 95.9, 45.8, 14626, 3.94, 70.8, 4, 98, 99.3, 97.2, 7.5, 8.3, 6, 32.8, 17, 87, 42.9, 6.9, 48.5, 51.5, 74.2, 29.9, 13.9, 2.4, 8, 13.5, 26, 4.9], ['CARTAGO', 'LA UNION', 192, 11902, 397, 83, 378, 4145, 8441, 599, 468, 300, 2501, 10656, 8706, 369, 73, 99399, 44.8, 2217, 97, 93.2, 43.7, 26979, 3.67, 69.7, 4.7, 98.6, 99.4, 98.3, 9.5, 10.2, 8, 34.2, 18.5, 89.8, 47.6, 9.8, 40.7, 59.3, 75.4, 44.7, 12.9, 9.7, 9.4, 14.1, 31.5, 8.4], ['CARTAGO', 'JIMENEZ', 37, 2042, 128, 19, 94, 776, 2105, 72, 81, 46, 748, 1319, 781, 148, 32, 14669, 286.4, 51, 52.6, 98.9, 46.8, 4113, 3.56, 56.7, 2, 96.6, 99.1, 95.3, 6.6, 7.4, 5.2, 31.6, 15.7, 89.1, 44, 5.9, 52.9, 47.1, 70.3, 23.8, 12.7, 2.4, 10.9, 11, 25.6, 10], ['CARTAGO', 'TURRIALBA', 127, 10185, 461, 71, 337, 3022, 7631, 292, 186, 267, 2024, 7507, 5237, 506, 138, 69616, 1642.7, 42, 57.4, 97.8, 49.1, 20453, 3.4, 64.9, 3.4, 96.1, 98.8, 94.8, 7.4, 8.3, 6, 33, 18.8, 88.4, 49.1, 8.2, 52.5, 47.5, 67.7, 28.1, 14.9, 2.2, 11.7, 12.6, 26.5, 8.3], ['CARTAGO', 'ALVARADO', 33, 1938, 76, 19, 25, 735, 1562, 59, 96, 57, 705, 925, 964, 134, 32, 14312, 81.1, 177, 62.6, 100.3, 47.6, 3612, 3.95, 72.4, 3.1, 97.2, 98.8, 96.4, 6.6, 7.3, 5.2, 29.5, 16.4, 82.4, 35.7, 5.5, 47, 53, 79.7, 26.7, 18.1, 1.4, 8.9, 14.3, 19.5, 8.8], ['CARTAGO', 'OREAMUNO', 100, 7171, 602, 52, 285, 2779, 5452, 259, 189, 220, 1815, 2985, 3770, 396, 60, 45473, 201.3, 226, 87.5, 95.7, 45.5, 11232, 4.04, 76.7, 4, 97.7, 99.1, 97, 8.1, 8.8, 6.7, 33.9, 18.9, 88.3, 46.8, 7.8, 46.1, 53.9, 75.8, 33.5, 17.2, 1.4, 8.3, 15.7, 26, 7.2], ['CARTAGO', 'EL GUARCO', 90, 6147, 540, 40, 135, 2549, 5693, 266, 216, 170, 1530, 2888, 4107, 280, 77, 41793, 167.7, 249, 87.7, 101.5, 44.7, 10831, 3.83, 73.2, 2.5, 98.4, 99.5, 97.9, 8.3, 9.2, 6.5, 34.4, 17.7, 89.8, 44.8, 8.7, 44.9, 55.1, 75.5, 34.8, 12.9, 2.8, 8.1, 13, 23.7, 7.3]])
            print("Input:")
            print("CARTAGO")
            print("Output:")
            print([['CARTAGO', 'CARTAGO CENTRAL', 270, 24665, 3295, 174, 575, 9491, 19042, 951, 856, 613, 5269, 10318, 13872, 1108, 184, 147898, 287.8, 514, 88.7, 96.1, 43.9, 36618, 3.8, 74.1, 2.9, 98.4, 99.3, 97.9, 9, 9.8, 7.6, 34.3, 19.1, 89.4, 51.9, 9.2, 46.8, 53.2, 72.2, 35.3, 13.7, 3.9, 8.6, 13.9, 28.7, 6.4], ['CARTAGO', 'PARAISO', 212, 8478, 421, 69, 268, 6342, 5418, 316, 269, 282, 2872, 4613, 3900, 460, 89, 57743, 411.9, 140, 76.9, 95.9, 45.8, 14626, 3.94, 70.8, 4, 98, 99.3, 97.2, 7.5, 8.3, 6, 32.8, 17, 87, 42.9, 6.9, 48.5, 51.5, 74.2, 29.9, 13.9, 2.4, 8, 13.5, 26, 4.9], ['CARTAGO', 'LA UNION', 192, 11902, 397, 83, 378, 4145, 8441, 599, 468, 300, 2501, 10656, 8706, 369, 73, 99399, 44.8, 2217, 97, 93.2, 43.7, 26979, 3.67, 69.7, 4.7, 98.6, 99.4, 98.3, 9.5, 10.2, 8, 34.2, 18.5, 89.8, 47.6, 9.8, 40.7, 59.3, 75.4, 44.7, 12.9, 9.7, 9.4, 14.1, 31.5, 8.4], ['CARTAGO', 'JIMENEZ', 37, 2042, 128, 19, 94, 776, 2105, 72, 81, 46, 748, 1319, 781, 148, 32, 14669, 286.4, 51, 52.6, 98.9, 46.8, 4113, 3.56, 56.7, 2, 96.6, 99.1, 95.3, 6.6, 7.4, 5.2, 31.6, 15.7, 89.1, 44, 5.9, 52.9, 47.1, 70.3, 23.8, 12.7, 2.4, 10.9, 11, 25.6, 10], ['CARTAGO', 'TURRIALBA', 127, 10185, 461, 71, 337, 3022, 7631, 292, 186, 267, 2024, 7507, 5237, 506, 138, 69616, 1642.7, 42, 57.4, 97.8, 49.1, 20453, 3.4, 64.9, 3.4, 96.1, 98.8, 94.8, 7.4, 8.3, 6, 33, 18.8, 88.4, 49.1, 8.2, 52.5, 47.5, 67.7, 28.1, 14.9, 2.2, 11.7, 12.6, 26.5, 8.3], ['CARTAGO', 'ALVARADO', 33, 1938, 76, 19, 25, 735, 1562, 59, 96, 57, 705, 925, 964, 134, 32, 14312, 81.1, 177, 62.6, 100.3, 47.6, 3612, 3.95, 72.4, 3.1, 97.2, 98.8, 96.4, 6.6, 7.3, 5.2, 29.5, 16.4, 82.4, 35.7, 5.5, 47, 53, 79.7, 26.7, 18.1, 1.4, 8.9, 14.3, 19.5, 8.8], ['CARTAGO', 'OREAMUNO', 100, 7171, 602, 52, 285, 2779, 5452, 259, 189, 220, 1815, 2985, 3770, 396, 60, 45473, 201.3, 226, 87.5, 95.7, 45.5, 11232, 4.04, 76.7, 4, 97.7, 99.1, 97, 8.1, 8.8, 6.7, 33.9, 18.9, 88.3, 46.8, 7.8, 46.1, 53.9, 75.8, 33.5, 17.2, 1.4, 8.3, 15.7, 26, 7.2], ['CARTAGO', 'EL GUARCO', 90, 6147, 540, 40, 135, 2549, 5693, 266, 216, 170, 1530, 2888, 4107, 280, 77, 41793, 167.7, 249, 87.7, 101.5, 44.7, 10831, 3.83, 73.2, 2.5, 98.4, 99.5, 97.9, 8.3, 9.2, 6.5, 34.4, 17.7, 89.8, 44.8, 8.7, 44.9, 55.1, 75.5, 34.8, 12.9, 2.8, 8.1, 13, 23.7, 7.3]])

    ################################### 4 ##################################
    """
    Funcion de testeo para calcular_cantidad_voto_por_canton que retorna el total de votos para cada canton en especifico.
    input: lista
    output: lista 
    """
    def test_calcular_cantidad_voto_por_canton(self):
            global lista_catones
            print("__________________________________________________________________\n")
            print("Test : test_calcular_cantidad_voto_por_canton(lista_cantones)")
            resultado = [1061, 72528, 5920, 527, 2097, 29839, 55344, 2814, 2361, 1955, 17464, 41211, 41337, 3401, 685]
            self.assertEqual(calcular_cantidad_voto_por_canton(lista_catones),resultado)
            print("Input:")
            print(lista_catones)
            print("Output:")
            print(resultado)

    ################################### 5 ##################################
    """
    Funcion de testeo para calcular_probabilidad_voto_por_partido_canton que calcula la probabilidad de un voto para cada partido en un detreminado canton.
    input: lista , lista
    output: lista
    """
    def test_calcular_probabilidad_voto_por_partido_canton(self):
            global lista_catones,lista_votos_totales
            print("__________________________________________________________________\n")
            print("Test : calcular_probabilidad_voto_por_partido_canton(lista_cantones,votos_totales)")
            resultado = [['CARTAGO', 'CARTAGO CENTRAL', 0.2544769085768143, 0.3400755570262519, 0.5565878378378378, 0.3301707779886148, 0.27420123986647593, 0.31807366198599146, 0.34406620410523275, 0.337953091684435, 0.36255823803473103, 0.3135549872122762, 0.3017063673843335, 0.25037004683215647, 0.33558313375426374, 0.3257865333725375, 0.2686131386861314], ['CARTAGO', 'PARAISO', 0.1998114985862394, 0.11689278623428193, 0.07111486486486486, 0.13092979127134724, 0.12780162136385312, 0.2125406347397701, 0.09789679098005204, 0.1122956645344705, 0.11393477340110122, 0.1442455242966752, 0.16445258818140174, 0.1119361335565747, 0.09434646926482328, 0.13525433695971772, 0.12992700729927006], ['CARTAGO', 'LA UNION', 0.18096135721017909, 0.16410213986322525, 0.0670608108108108, 0.15749525616698293, 0.18025751072961374, 0.1389121619357217, 0.15251879155825382, 0.212864250177683, 0.19822109275730623, 0.1534526854219949, 0.14320888685295466, 0.2585717405547063, 0.2106103490819363, 0.10849750073507791, 0.10656934306569343], ['CARTAGO', 'JIMENEZ', 0.034872761545711596, 0.028154643723803222, 0.021621621621621623, 0.036053130929791274, 0.04482594182164998, 0.0260062334528637, 0.03803483665799364, 0.0255863539445629, 0.03430749682337993, 0.023529411764705882, 0.042830966559780116, 0.03200601781077868, 0.01889348525534025, 0.04351661276095266, 0.04671532846715328], ['CARTAGO', 'TURRIALBA', 0.11969839773798303, 0.14042852415618795, 0.07787162162162162, 0.1347248576850095, 0.16070577014783025, 0.10127685244143571, 0.13788305868748194, 0.10376687988628287, 0.07878017789072427, 0.13657289002557546, 0.11589555657352267, 0.18216010288515203, 0.12669037424099475, 0.1487797706556895, 0.20145985401459854], ['CARTAGO', 'ALVARADO', 0.03110273327049953, 0.02672071475843812, 0.012837837837837839, 0.036053130929791274, 0.011921793037672867, 0.02463219276785415, 0.028223474992772477, 0.020966595593461264, 0.04066073697585769, 0.029156010230179028, 0.040368758589097574, 0.022445463589818252, 0.023320511890074266, 0.03940017641870038, 0.04671532846715328], ['CARTAGO', 'OREAMUNO', 0.0942507068803016, 0.09887215971762629, 0.10168918918918919, 0.09867172675521822, 0.13590844062947066, 0.09313314789369617, 0.0985111303845042, 0.09203980099502487, 0.08005082592121983, 0.11253196930946291, 0.10392808062299588, 0.07243211763849458, 0.09120158695599584, 0.11643634225227874, 0.08759124087591241], ['CARTAGO', 'EL GUARCO', 0.08482563619227144, 0.0847534745201853, 0.09121621621621621, 0.07590132827324478, 0.06437768240343347, 0.08542511478266698, 0.10286571263370917, 0.0945273631840796, 0.09148665819567979, 0.08695652173913043, 0.08760879523591387, 0.07007837713231904, 0.0993540895565716, 0.08232872684504558, 0.11240875912408758]]
            self.assertEqual(calcular_probabilidad_voto_por_partido_canton(lista_catones,lista_votos_totales),resultado)
            print("Input:")
            print(lista_catones)
            print("\n y \n")
            print(lista_votos_totales)
            print("Output:")
            print(resultado)
            
    ################################### 6 ##################################
    """
    Funcion de testeo para escoger_canton_segun_voto que asigna canton a un voto especifico dependiendo de la probabilidad que este tenga.
    input: string , lista, int
    output: lista
    """
    def test_escoger_canton_segun_voto(self):
            global lista_aleatorio
            print("__________________________________________________________________\n")
            print("Test : escoger_canton_segun_voto(nombre_partido, probalidades_voto, nuestras)")
            entrada1= "ACCESIBILIDAD SIN EXCLUSION"
            entrada2= [['CARTAGO', 'CARTAGO CENTRAL', 0.2544769085768143, 0.3400755570262519, 0.5565878378378378, 0.3301707779886148, 0.27420123986647593, 0.31807366198599146, 0.34406620410523275, 0.337953091684435, 0.36255823803473103, 0.3135549872122762, 0.3017063673843335, 0.25037004683215647, 0.33558313375426374, 0.3257865333725375, 0.2686131386861314], ['CARTAGO', 'PARAISO', 0.1998114985862394, 0.11689278623428193, 0.07111486486486486, 0.13092979127134724, 0.12780162136385312, 0.2125406347397701, 0.09789679098005204, 0.1122956645344705, 0.11393477340110122, 0.1442455242966752, 0.16445258818140174, 0.1119361335565747, 0.09434646926482328, 0.13525433695971772, 0.12992700729927006], ['CARTAGO', 'LA UNION', 0.18096135721017909, 0.16410213986322525, 0.0670608108108108, 0.15749525616698293, 0.18025751072961374, 0.1389121619357217, 0.15251879155825382, 0.212864250177683, 0.19822109275730623, 0.1534526854219949, 0.14320888685295466, 0.2585717405547063, 0.2106103490819363, 0.10849750073507791, 0.10656934306569343], ['CARTAGO', 'JIMENEZ', 0.034872761545711596, 0.028154643723803222, 0.021621621621621623, 0.036053130929791274, 0.04482594182164998, 0.0260062334528637, 0.03803483665799364, 0.0255863539445629, 0.03430749682337993, 0.023529411764705882, 0.042830966559780116, 0.03200601781077868, 0.01889348525534025, 0.04351661276095266, 0.04671532846715328], ['CARTAGO', 'TURRIALBA', 0.11969839773798303, 0.14042852415618795, 0.07787162162162162, 0.1347248576850095, 0.16070577014783025, 0.10127685244143571, 0.13788305868748194, 0.10376687988628287, 0.07878017789072427, 0.13657289002557546, 0.11589555657352267, 0.18216010288515203, 0.12669037424099475, 0.1487797706556895, 0.20145985401459854], ['CARTAGO', 'ALVARADO', 0.03110273327049953, 0.02672071475843812, 0.012837837837837839, 0.036053130929791274, 0.011921793037672867, 0.02463219276785415, 0.028223474992772477, 0.020966595593461264, 0.04066073697585769, 0.029156010230179028, 0.040368758589097574, 0.022445463589818252, 0.023320511890074266, 0.03940017641870038, 0.04671532846715328], ['CARTAGO', 'OREAMUNO', 0.0942507068803016, 0.09887215971762629, 0.10168918918918919, 0.09867172675521822, 0.13590844062947066, 0.09313314789369617, 0.0985111303845042, 0.09203980099502487, 0.08005082592121983, 0.11253196930946291, 0.10392808062299588, 0.07243211763849458, 0.09120158695599584, 0.11643634225227874, 0.08759124087591241], ['CARTAGO', 'EL GUARCO', 0.08482563619227144, 0.0847534745201853, 0.09121621621621621, 0.07590132827324478, 0.06437768240343347, 0.08542511478266698, 0.10286571263370917, 0.0945273631840796, 0.09148665819567979, 0.08695652173913043, 0.08760879523591387, 0.07007837713231904, 0.0993540895565716, 0.08232872684504558, 0.11240875912408758]]
            entrada3= 50
            resultado1 = ['CARTAGO CENTRAL', 'CARTAGO CENTRAL', 'CARTAGO CENTRAL', 'CARTAGO CENTRAL', 'CARTAGO CENTRAL', 'CARTAGO CENTRAL', 'CARTAGO CENTRAL', 'CARTAGO CENTRAL', 'CARTAGO CENTRAL', 'CARTAGO CENTRAL', 'CARTAGO CENTRAL', 'CARTAGO CENTRAL', 'PARAISO', 'PARAISO', 'PARAISO', 'PARAISO', 'PARAISO', 'PARAISO', 'PARAISO', 'PARAISO', 'PARAISO', 'LA UNION', 'LA UNION', 'LA UNION', 'LA UNION', 'LA UNION', 'LA UNION', 'LA UNION', 'LA UNION', 'LA UNION', 'JIMENEZ', 'TURRIALBA', 'TURRIALBA', 'TURRIALBA', 'TURRIALBA', 'TURRIALBA', 'ALVARADO', 'OREAMUNO', 'OREAMUNO', 'OREAMUNO', 'OREAMUNO', 'EL GUARCO', 'EL GUARCO', 'EL GUARCO', 'EL GUARCO']
            self.assertEqual(escoger_canton_segun_voto(entrada1,entrada2,entrada3),resultado1)
            print("Input:")
            print(entrada1)
            print("\n y \n")
            print(entrada2)
            print("\n y \n")
            print(entrada3)
            print("Output:")
            print(resultado1)
            
    ################################### 7 ##################################
    """
    Funcion de testeo para aleatorio que simula los votos a nivel de provincia.
    input: int , string
    output: lista de sublistas
    """
    def test_aleatorio(self):
            global lista_aleatorio
            print("__________________________________________________________________\n")
            print("Test : aleatorio(n, provincia)")
            resultado1 = 500
            resultado2 = 35
            self.assertEqual(len(aleatorio(500,"CARTAGO")),resultado1)
            x = aleatorio(500,"CARTAGO")
            self.assertEqual(len(x[0]),resultado2)
            print("Input:")
            print(500)
            print("Output:")
            print(resultado1)
            print("\n y \n")
            print(resultado2)

    ################################### 8 ##################################
    """
    Funcion de testeo para suma_partes_lista que suma un rango de valores dentro de una lista.
    input: lista
    output: int
    """

    def test_suma_partes_lista(self):
            print("__________________________________________________________________\n")
            print("Test : suma_partes_lista(lista)")
            entrada = [32,34,322,765,456,789,56]
            resultado = 2454
            self.assertEqual(suma_partes_lista(entrada),resultado)
            print("Input:")
            print(entrada)
            print("Output:")
            print(resultado)

    ################################### 9 ##################################
    """
    Funcion de testeo para prueba_cantones que revisa la cantidad de votos asignados a un canton.
    input: lista , string
    output: lista
    """

    def test_prueba_cantones(self):
            global lista_catones
            print("__________________________________________________________________\n")
            print("Test : prueba_cantones(lista, nombre)")
            entrada = "ALVARADO"
            resultado = [['CARTAGO', 'ALVARADO', 33, 1938, 76, 19, 25, 735, 1562, 59, 96, 57, 705, 925, 964, 134, 32, 14312, 81.1, 177, 62.6, 100.3, 47.6, 3612, 3.95, 72.4, 3.1, 97.2, 98.8, 96.4, 6.6, 7.3, 5.2, 29.5, 16.4, 82.4, 35.7, 5.5, 47, 53, 79.7, 26.7, 18.1, 1.4, 8.9, 14.3, 19.5, 8.8]]
            self.assertEqual(prueba_cantones(lista_catones, entrada),resultado)
            print("Input:")
            print(entrada)
            print("\n y \n")
            print(lista_catones)
            print("Output:")
            print(resultado)

    ################################### 10 ##################################
    """
    Funcion de testeo para obtener_inidicadores_canton que asigna los indicadores correspondientes a cada canton.
    input: string, lista
    output: lista
    """

    def test_obtener_inidicadores_canton(self):
            global lista_catones
            print("__________________________________________________________________\n")
            print("Test : obtener_inidicadores_canton(nombre_canton, lista_cantones))")
            entrada = "ALVARADO"
            resultado = [14312, 81.1, 177, 62.6, 100.3, 47.6, 3612, 3.95, 72.4, 3.1, 97.2, 98.8, 96.4, 6.6, 7.3, 5.2, 29.5, 16.4, 82.4, 35.7, 5.5, 47, 53, 79.7, 26.7, 18.1, 1.4, 8.9, 14.3, 19.5, 8.8]
            self.assertEqual(obtener_inidicadores_canton(entrada,lista_catones),resultado)
            print("Input:")
            print(entrada)
            print("\n y \n")
            print(lista_catones)
            print("Output:")
            print(resultado)

    ################################### 11 ##################################
    """
    Funcion de testeo para asignar_sexo que asigna el genero a cada voto simulado.
    input: int, int
    output: string
    """
    def test_asignar_sexo(self):
            print("__________________________________________________________________\n")
            print("Test : asignar_sexo(probabilidad_hombre, probabilidad_mujer)")
            entrada1 = 100
            entrada2 = 0
            resultado = "HOMBRE"
            self.assertEqual(asignar_sexo(100,0),resultado)
            print("Input:")
            print(entrada1)
            print("\n y \n")
            print(entrada2)
            print("Output:")
            print(resultado)

    ################################### 12 ##################################
    """
    Funcion de testeo para verificar_probabilidad que verifica probabilidad de hombres y mujeres.
    input: string, lista
    output:
    """
    def test_verificar_probabilidad(self):
            global lista_catones
            print("__________________________________________________________________\n")
            print("Test : verificar_probabilidad(nombre_canton, lista)")
            entrada1 = "OREAMUNO"
            self.assertTrue(verificar_probabilidad(entrada1, lista_catones))
            print("Input:")
            print(entrada1)
            print("\n y \n")
            print(lista_catones)
            print("Output:")

    ################################### 13 ##################################
    """
    Funcion de testeo para obtenerDatosProvincia que obtiene datos para una provincia especifica.
    input: lista
    output: lista
    """
    def test_obtenerDatosProvincia(self):
            global lista_catones
            print("__________________________________________________________________\n")
            print("Test : obtenerDatosProvincia(lista_cantones)")
            resultado = ['CARTAGO', 1061, 72528, 5920, 527, 2097, 29839, 55344, 2814, 2361, 1955, 17464, 41211, 41337, 3401, 685]
            self.assertEqual(obtenerDatosProvincia(lista_catones),resultado)
            print("Input:")
            print(lista_catones)
            print("Output:")
            print(resultado)
    
    ################################### 14 ##################################
    """
    Funcion de testeo para obtener_votos_cada_provincias que obtiene datos para todas las provincias.
    input: 
    output: lista de sublistas
    """
    def test_obtener_votos_cada_provincias(self):
            print("__________________________________________________________________\n")
            print("Test : obtener_votos_cada_provincias()")
            resultado = [['SAN JOSE', 2370, 179358, 2688, 1514, 5956, 68765, 137825, 7773, 6442, 4110, 35365, 174879, 137230, 5739, 1177], ['HEREDIA', 580, 64238, 682, 400, 1896, 19075, 41784, 2405, 2435, 1236, 8790, 49930, 42777, 1780, 351], ['CARTAGO', 1061, 72528, 5920, 527, 2097, 29839, 55344, 2814, 2361, 1955, 17464, 41211, 41337, 3401, 685], ['ALAJUELA', 1381, 92292, 1312, 888, 3176, 37428, 76789, 3847, 3036, 2057, 22455, 113123, 64427, 4241, 888], ['LIMON', 989, 16050, 1003, 453, 1434, 15810, 26684, 1963, 657, 1215, 6878, 64710, 14041, 2818, 769], ['GUANACASTE', 520, 20672, 432, 254, 925, 15335, 32426, 1328, 678, 800, 7118, 34812, 23794, 2362, 625], ['PUNTARENAS', 650, 20241, 601, 323, 1344, 19382, 31146, 1800, 946, 933, 8168, 59776, 22955, 2641, 597]]
            self.assertEqual(obtener_votos_cada_provincias(),resultado)
            print("Input:")
            print("Output:")
            print(resultado)

    ################################### 15 ##################################
    """
    Funcion de testeo para votos_totales que obtiene los votos totales de todos los partidos politicos.
    input: lista
    output: lista
    """
    def test_votos_totales(self):
            global votos_provincia
            print("__________________________________________________________________\n")
            print("Test : votos_totales(lista_votos)")
            resultado = [7551, 465379, 12638, 4359, 16828, 205634, 401998, 21930, 16555, 12306, 106238, 538441, 346561, 22982, 5092]
            self.assertEqual(votos_totales(votos_provincia),resultado)
            print("Input:")
            print(votos_provincia)
            print("Output:")
            print(resultado)

    ################################### 16 ##################################
    """
    Funcion de testeo promedio_votos_por_provincia para que calcula promedio de votos por provincia.
    input: 
    output: lista de sublistas
    """
    def test_promedio_votos_por_provincia(self):
            print("__________________________________________________________________\n")
            print("Test : promedio_votos_por_provincia()")
            resultado = [['SAN JOSE', 0.001084920430013019, 0.08210513016298526, 0.001230492032014766, 0.0006930673126749835, 0.0027264920173660514, 0.03147871450204441, 0.06309247184242378, 0.003558264347042699, 0.002948969371368721, 0.0018814442900225773, 0.016189118568527602, 0.08005476788196066, 0.06282009730408718, 0.002627155421031526, 0.000538798036339799], ['HEREDIA', 0.00026550795333651943, 0.029406379149019543, 0.00031220073133707976, 0.00018310893333553063, 0.0008679363440104152, 0.008732007258438118, 0.01912755917622953, 0.001100942461679878, 0.0011146756316800428, 0.0005658066040067896, 0.004023818810048286, 0.022856572603607614, 0.019582127103234984, 0.0008148347533431114, 0.00016067808900192812], ['CARTAGO', 0.00048569644567249504, 0.033201311792398415, 0.0027100122133658536, 0.0002412460196695616, 0.0009599485830115193, 0.013659468654497247, 0.025334952016304018, 0.001288171346015458, 0.0010808004790129695, 0.000894944911677406, 0.007994536029429268, 0.018865255629226384, 0.018922934943227075, 0.0015568837056853494, 0.0003135740483370962], ['ALAJUELA', 0.0006321835923409195, 0.04224872418850698, 0.0006005973013405405, 0.000406501832004878, 0.0014538849306841132, 0.017133502892205603, 0.035151879704755154, 0.001761050166354466, 0.0013897968040166775, 0.0009416376896779664, 0.010279277745123352, 0.05178457966428808, 0.02949289812002058, 0.0019414124656899636, 0.000406501832004878], ['LIMON', 0.0004527368376720995, 0.007347245950088167, 0.0004591456503388431, 0.00020737086700248845, 0.0006564455260078773, 0.007237380590086848, 0.012215196942813249, 0.0008986070903441166, 0.0003007564230036091, 0.0005561933850066743, 0.003148558108704449, 0.02962244769035547, 0.0064275813324104645, 0.0012900024353488134, 0.00035202692433755763], ['GUANACASTE', 0.00023804161333618984, 0.009463069674780224, 0.0001977576480023731, 0.00011627417266806196, 0.00042343940833841463, 0.007019938731750906, 0.01484372568084479, 0.0006079216586739617, 0.00031036964200372444, 0.00036621786667106126, 0.0032584234687057676, 0.015935970468191233, 0.01089223489946404, 0.0010812582513463084, 0.00028610770833676665], ['PUNTARENAS', 0.00029755201667023727, 0.009265769799111189, 0.0002751211723366348, 0.000147860463668441, 0.000615246016007383, 0.008872543364773137, 0.014257777094171094, 0.0008239902000098879, 0.00043305262733853, 0.0004271015870051252, 0.0037390844187115357, 0.027363798997661698, 0.010508163911792765, 0.001208976732347841, 0.00027329008300327947]]
            self.assertEqual(promedio_votos_por_provincia(),resultado)
            print("Input:")
            print("Output:")
            print(resultado)

    ################################### 17 ##################################
    """
    Funcion de testeo para lista_probalidades_voto_provincia que retorna lista con nombre de provincia y el voto, segun la probabilidad.
    input: lista, int
    output: lista de sublistas
    """
    def test_lista_probalidades_voto_provincia(self):
            global promedio_votos_x_provincia
            print("__________________________________________________________________\n")
            print("Test : lista_probalidades_voto_provincia()")
            entrada2 = 100
            resultado = [['SAN JOSE', 'ACCION CIUDADANA'], ['SAN JOSE', 'ACCION CIUDADANA'], ['SAN JOSE', 'ACCION CIUDADANA'], ['SAN JOSE', 'ACCION CIUDADANA'], ['SAN JOSE', 'ACCION CIUDADANA'], ['SAN JOSE', 'ACCION CIUDADANA'], ['SAN JOSE', 'ACCION CIUDADANA'], ['SAN JOSE', 'ACCION CIUDADANA'], ['SAN JOSE', 'INTEGRACION NACIONAL'], ['SAN JOSE', 'INTEGRACION NACIONAL'], ['SAN JOSE', 'INTEGRACION NACIONAL'], ['SAN JOSE', 'LIBERACION NACIONAL'], ['SAN JOSE', 'LIBERACION NACIONAL'], ['SAN JOSE', 'LIBERACION NACIONAL'], ['SAN JOSE', 'LIBERACION NACIONAL'], ['SAN JOSE', 'LIBERACION NACIONAL'], ['SAN JOSE', 'LIBERACION NACIONAL'], ['SAN JOSE', 'REPUBLICANO SOCIAL CRISTIANO'], ['SAN JOSE', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'RESTAURACION NACIONAL'], ['SAN JOSE', 'UNIDAD SOCIAL CRISTIANA'], ['SAN JOSE', 'UNIDAD SOCIAL CRISTIANA'], ['SAN JOSE', 'UNIDAD SOCIAL CRISTIANA'], ['SAN JOSE', 'UNIDAD SOCIAL CRISTIANA'], ['SAN JOSE', 'UNIDAD SOCIAL CRISTIANA'], ['SAN JOSE', 'UNIDAD SOCIAL CRISTIANA'], ['HEREDIA', 'ACCION CIUDADANA'], ['HEREDIA', 'ACCION CIUDADANA'], ['HEREDIA', 'LIBERACION NACIONAL'], ['HEREDIA', 'RESTAURACION NACIONAL'], ['HEREDIA', 'RESTAURACION NACIONAL'], ['HEREDIA', 'UNIDAD SOCIAL CRISTIANA'], ['CARTAGO', 'ACCION CIUDADANA'], ['CARTAGO', 'ACCION CIUDADANA'], ['CARTAGO', 'ACCION CIUDADANA'], ['CARTAGO', 'INTEGRACION NACIONAL'], ['CARTAGO', 'LIBERACION NACIONAL'], ['CARTAGO', 'LIBERACION NACIONAL'], ['CARTAGO', 'RESTAURACION NACIONAL'], ['CARTAGO', 'UNIDAD SOCIAL CRISTIANA'], ['ALAJUELA', 'ACCION CIUDADANA'], ['ALAJUELA', 'ACCION CIUDADANA'], ['ALAJUELA', 'ACCION CIUDADANA'], ['ALAJUELA', 'ACCION CIUDADANA'], ['ALAJUELA', 'INTEGRACION NACIONAL'], ['ALAJUELA', 'LIBERACION NACIONAL'], ['ALAJUELA', 'LIBERACION NACIONAL'], ['ALAJUELA', 'LIBERACION NACIONAL'], ['ALAJUELA', 'REPUBLICANO SOCIAL CRISTIANO'], ['ALAJUELA', 'RESTAURACION NACIONAL'], ['ALAJUELA', 'RESTAURACION NACIONAL'], ['ALAJUELA', 'RESTAURACION NACIONAL'], ['ALAJUELA', 'RESTAURACION NACIONAL'], ['ALAJUELA', 'RESTAURACION NACIONAL'], ['ALAJUELA', 'UNIDAD SOCIAL CRISTIANA'], ['ALAJUELA', 'UNIDAD SOCIAL CRISTIANA'], ['LIMON', 'LIBERACION NACIONAL'], ['LIMON', 'RESTAURACION NACIONAL'], ['LIMON', 'RESTAURACION NACIONAL'], ['GUANACASTE', 'LIBERACION NACIONAL'], ['GUANACASTE', 'RESTAURACION NACIONAL'], ['GUANACASTE', 'UNIDAD SOCIAL CRISTIANA'], ['PUNTARENAS', 'LIBERACION NACIONAL'], ['PUNTARENAS', 'RESTAURACION NACIONAL'], ['PUNTARENAS', 'RESTAURACION NACIONAL'], ['PUNTARENAS', 'UNIDAD SOCIAL CRISTIANA']]
            self.assertEqual(lista_probalidades_voto_provincia(promedio_votos_x_provincia,entrada2),resultado)
            print("Input:")
            print(promedio_votos_x_provincia)
            print("\n y \n")
            print(entrada2)
            print("Output:")
            print(resultado)

    ################################### 18 ##################################
    """
    Funcion de testeo para aleatorio_provincia que genera los votos pais.
    input: int
    output: lista de sublistas
    """
    def test_aleatorio_provincia(self):
            global lista_aleatorio
            print("__________________________________________________________________\n")
            print("Test : aleatorio_provincia(numero)")
            resultado1 = 500
            resultado2 = 36
            x = aleatorio_provincia(500)
            self.assertEqual(len(x),resultado1)
            self.assertEqual(len(x[0]),resultado2)
            print("Input:")
            print(500)
            print("Output:")
            print(resultado1)
            print("\n y \n")
            print(resultado2)
        
if __name__ == '__main__':
    unittest.main()
