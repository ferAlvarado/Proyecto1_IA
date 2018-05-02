"""
=====================================
Proyecto Corto #1 ­ Simulador Votantes
                (Main)
=====================================
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
#-----------------------------------------------------------------------
import os
import sys
import csv
import random
os . system('ls -lah')
total = []
segundaRonda = []
votos_validos = []
votos_provincia = []
partidos_politicos = [
    "ACCESIBILIDAD SIN EXCLUSION",
    "ACCION CIUDADANA",
    "ALIANZA DEMOCRATA CRISTIANA",
    "DE LOS TRABAJADORES",
    "FRENTE AMPLIO",
    "INTEGRACION NACIONAL",
    "LIBERACION NACIONAL",
    "MOVIMIENTO LIBERTARIO",
    "NUEVA GENERACION",
    "RENOVACION COSTARRICENSE",
    "REPUBLICANO SOCIAL CRISTIANO",
    "RESTAURACION NACIONAL",
    "UNIDAD SOCIAL CRISTIANA",
    "NULO",
    "BLANCO"]
provincias = [
    "SAN JOSE",
    "HEREDIA",
    "CARTAGO",
    "ALAJUELA",
    "LIMON",
    "GUANACASTE",
    "PUNTARENAS"]
#-----------------------------------------------------------------------

################################### 1 ##################################
"""
Funcion que lee el archivo y almacena los datos en variable global total
"""
#-----------------------------------------------------------------------


def leerArchivoCSV(nombre):
    global total
    total = []
    with open(nombre) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            tempo = []
            for i in range(0, 48):
                if i == 0 or i == 1:
                    tempo += [row[i]]
                else:
                    tipo_variable = type(eval(row[i]))
                    if tipo_variable is int:
                        tempo += [int(row[i])]
                    if tipo_variable is str:
                        tempo += [str(row[i])]
                    if tipo_variable is float:
                        tempo += [float(row[i])]
            total += [tempo]
    return True


#-----------------------------------------------------------------------
"""
Funcion que lee el archivo y almacena los datos en variable segundaRonda 
"""
#-----------------------------------------------------------------------


def leerArchivoCSV2(nombre):
    global segundaRonda
    segundaRonda = []
    with open(nombre) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            tempo = []
            for i in range(0, 6):
                if i == 0 or i == 1:
                    tempo += [row[i]]
                else:
                    tipo_variable = type(eval(row[i]))
                    if tipo_variable is int:
                        tempo += [int(row[i])]
                    if tipo_variable is str:
                        tempo += [str(row[i])]
                    if tipo_variable is float:
                        tempo += [float(row[i])]
            segundaRonda += [tempo]
    return True


def leerArchivoCSV3(nombre):
    segundaRonda = []
    with open(nombre) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            tempo = []
            for i in range(0, 36):
                if i == 0 or i == 1:
                    tempo += [row[i]]
                else:
                    tipo_variable = type(eval(row[i]))
                    if tipo_variable is int:
                        tempo += [int(row[i])]
                    if tipo_variable is str:
                        tempo += [str(row[i])]
                    if tipo_variable is float:
                        tempo += [float(row[i])]
            segundaRonda += [tempo]
    return segundaRonda
#-----------------------------------------------------------------------


################################### 2 ##################################
"""
Esta funcion suma todos los votos para cada partido en una provincia determinada
input: string
output: lista de sublistas
"""
#-----------------------------------------------------------------------


def sumar_todos_por_provincia(nombre_provincia):
    global total, votos_provincia
    votos_provincia = []
    tempo = []
    for i in total:
        if i[0] == nombre_provincia:
            tempo += [i]
            votos_provincia = [i[0]]
    partidos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for j in tempo:
        for k in range(2, 17):
            partidos[k - 2] += j[k]
    votos_provincia += [partidos]
    votos_finales = 0
    for votos in partidos:
        votos_finales += votos
    votos_provincia += [votos_finales]
    return votos_provincia
#-----------------------------------------------------------------------


################################### 3 ##################################
"""
Funcion que carga los datos referentes a los cantones para una provincia dada.
input: string
output: lista de sublistas
"""
#-----------------------------------------------------------------------


def cargar_datos_cantones(nombre_provincia):
    global total, votos_provincia
    votos_provincia = []
    tempo = []
    for i in total:
        if i[0] == nombre_provincia:
            tempo += [i]
    return tempo
#-----------------------------------------------------------------------


################################### 4 ##################################
"""
Funcion que retorna el total de votos para cada canton en especifico.
input: lista
output: lista
"""
#-----------------------------------------------------------------------


def calcular_cantidad_voto_por_canton(lista_cantones):
    cantidad_total_votos_partidos = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for canton in lista_cantones:
        for i in range(2, 17):
            cantidad_total_votos_partidos[i - 2] += canton[i]
    return cantidad_total_votos_partidos
#-----------------------------------------------------------------------


################################### 5 ##################################
"""
Funcion que calcula la probabilidad de un voto para cada partido en un detreminado canton.
input: lista , lista
output: lista
"""
#-----------------------------------------------------------------------


def calcular_probabilidad_voto_por_partido_canton(
        lista_cantones, lista_votos_totales):
    promedio = []
    for canton in lista_cantones:
        tempo = [canton[0], canton[1]]
        for i in range(2, 17):
            tempo += [canton[i] / lista_votos_totales[i - 2]]

        promedio += [tempo]
        tempo = []
    return promedio
#-----------------------------------------------------------------------


################################### 6 ##################################
"""
Funcion que asigna canton a un voto especifico dependiendo de la probabilidad que este tenga.
input: string , lista, int
output: lista
"""
#-----------------------------------------------------------------------


def escoger_canton_segun_voto(nombre_partido, probalidades_voto, nuestras):
    global partidos_politicos
    final = []
    if nombre_partido == partidos_politicos[0]:
        for proba in probalidades_voto:
            final += int(proba[2] * nuestras) * [proba[1]]
    elif nombre_partido == partidos_politicos[1]:
        for proba in probalidades_voto:
            final += int(proba[3] * nuestras) * [proba[1]]
    elif nombre_partido == partidos_politicos[2]:
        for proba in probalidades_voto:
            final += int(proba[4] * nuestras) * [proba[1]]
    elif nombre_partido == partidos_politicos[3]:
        for proba in probalidades_voto:
            final += int(proba[5] * nuestras) * [proba[1]]
    elif nombre_partido == partidos_politicos[4]:
        for proba in probalidades_voto:
            final += int(proba[6] * nuestras) * [proba[1]]
    elif nombre_partido == partidos_politicos[5]:
        for proba in probalidades_voto:
            final += int(proba[7] * nuestras) * [proba[1]]
    elif nombre_partido == partidos_politicos[6]:
        for proba in probalidades_voto:
            final += int(proba[8] * nuestras) * [proba[1]]
    elif nombre_partido == partidos_politicos[7]:
        for proba in probalidades_voto:
            final += int(proba[9] * nuestras) * [proba[1]]
    elif nombre_partido == partidos_politicos[8]:
        for proba in probalidades_voto:
            final += int(proba[10] * nuestras) * [proba[1]]
    elif nombre_partido == partidos_politicos[9]:
        for proba in probalidades_voto:
            final += int(proba[11] * nuestras) * [proba[1]]
    elif nombre_partido == partidos_politicos[10]:
        for proba in probalidades_voto:
            final += int(proba[12] * nuestras) * [proba[1]]
    elif nombre_partido == partidos_politicos[11]:
        for proba in probalidades_voto:
            final += int(proba[13] * nuestras) * [proba[1]]
    elif nombre_partido == partidos_politicos[12]:
        for proba in probalidades_voto:
            final += int(proba[14] * nuestras) * [proba[1]]
    elif nombre_partido == partidos_politicos[13]:
        for proba in probalidades_voto:
            final += int(proba[15] * nuestras) * [proba[1]]
    elif nombre_partido == partidos_politicos[14]:
        for proba in probalidades_voto:
            final += int(proba[16] * nuestras) * [proba[1]]
    if len(final) == 0:
        final += [proba[16]]

    return final
#-----------------------------------------------------------------------


################################### 7 ##################################
"""
Funcion que simula los votos a nivel de provincia.
input: int , string
output: lista de sublistas
"""
#-----------------------------------------------------------------------


def generar_muestra_provincia(n, provincia):
    global votos_provincia, partidos_politicos
    partidos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    leerArchivoCSV("datos.csv")
    cantones = cargar_datos_cantones(provincia)
    votos_t = calcular_cantidad_voto_por_canton(cantones)
    promedio_voto = calcular_probabilidad_voto_por_partido_canton(
        cantones, votos_t)
    sumar_todos_por_provincia(provincia)
    votos = votos_provincia[1]
    # print(votos_provincia[1])
    votantes_simulados = []
    for i in range(1, n + 1):
        numero = random.randrange(votos_provincia[2])
        edad = random.randrange(18, 82, 2)
        if (numero <= suma_partes_lista([votos[0]])):
            partidos[0] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[0], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            tempo = [[lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[0]]]
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista([votos[0]]) and numero <= suma_partes_lista(votos[:2])):
            partidos[1] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[1], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            tempo = [
                [lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[1]]] 
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:2]) and numero <= suma_partes_lista(votos[:3])):
            partidos[2] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[2], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            tempo = [
                [lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[2]]] 
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:3]) and numero <= suma_partes_lista(votos[:4])):
            partidos[3] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[3], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            tempo = [
                [lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[3]]] 
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:4]) and numero <= suma_partes_lista(votos[:5])):
            partidos[4] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[4], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            tempo = [
                [lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad] + [partidos_politicos[4]]] 
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:5]) and numero <= suma_partes_lista(votos[:6])):
            partidos[5] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[5], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            tempo = [
                [lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[5]]] 
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:6]) and numero <= suma_partes_lista(votos[:7])):
            partidos[6] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[6], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            tempo = [
                [lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[6]]] 
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:7]) and numero <= suma_partes_lista(votos[:8])):
            partidos[7] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[7], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            tempo = [
                [lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[7]]] 
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:8]) and numero <= suma_partes_lista(votos[:9])):
            partidos[8] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[8], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            tempo = [
                [lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[8]]] 
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:9]) and numero <= suma_partes_lista(votos[:10])):
            partidos[9] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[9], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            tempo = [
                [lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[9]]] 
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:10]) and numero <= suma_partes_lista(votos[:11])):
            partidos[10] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[10], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            tempo = [
                [lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[10]]] 
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:11]) and numero <= suma_partes_lista(votos[:12])):
            partidos[11] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[11], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            tempo = [
                [lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[11]]] 
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:12]) and numero <= suma_partes_lista(votos[:13])):
            partidos[12] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[12], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            tempo = [
                [lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[12]]] 
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:13]) and numero <= suma_partes_lista(votos[:14])):
            partidos[13] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[13], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            tempo = [[lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[13]]] 
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:14]) and numero <= suma_partes_lista(votos)):
            partidos[14] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[14], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            tempo = [[lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[14]]] 
            votantes_simulados += tempo
            tempo = []
    # print(partidos)
    return votantes_simulados
#-----------------------------------------------------------------------


################################### 8 ##################################
"""
Funcion que suma un rango de valores dentro de una lista.
input: lista
output: int
"""
#-----------------------------------------------------------------------


def suma_partes_lista(lista):
    numero = 0
    for i in lista:
        numero += i
    return numero
#-----------------------------------------------------------------------


################################### 9 ##################################
"""
Funcion que revisa la cantidad de votos asignados a un canton.
input: lista , string
output: lista
"""
#-----------------------------------------------------------------------


def prueba_cantones(lista, nombre):
    result = []
    for i in lista:
        if i[1] == nombre:
            result += [i]
    return result
#-----------------------------------------------------------------------


################################### 10 ##################################
"""
Funcion que asigna los indicadores correspondientes a cada canton.
input: string, lista
output: lista
"""
#-----------------------------------------------------------------------


def obtener_inidicadores_canton(nombre_canton, lista_cantones):
    
    for canton in lista_cantones:
        
        if canton[1] == nombre_canton:
            
            return canton[17:]
#-----------------------------------------------------------------------


################################### 11 ##################################
"""
Funcion que asigna el genero a cada voto simulado.
input: int, int
output: string
"""
#-----------------------------------------------------------------------


def asignar_sexo(probabilidad_hombre, probabilidad_mujer):
    tempo = []
    cantidad_hombres = int(5 * (probabilidad_hombre / 100))
    cantidad_mujeres = int(10 * (probabilidad_mujer / 100))
    tempo += cantidad_hombres * ["HOMBRE"]
    tempo += cantidad_mujeres * ["MUJER"]
    numero = random.randrange(len(tempo))
    return tempo[numero]
#-----------------------------------------------------------------------


################################### 12 ##################################
"""
Funcion que verifica probabilidad de hombres y mujeres.
input: string, lista
output:
"""
#-----------------------------------------------------------------------


def verificar_probabilidad(nombre_canton, lista):
    hombres = 0
    mujeres = 0
    total = 0
    for i in lista:
        if i[1] == nombre_canton:
            if i[-1] == "HOMBRE":
                hombres += 1
                total += 1
            else:
                mujeres += 1
                total += 1
##    print("Hombres", hombres)
##    print("Mujeres", mujeres)
##    print("Total", total)
    return True
#-----------------------------------------------------------------------


################################### 13 ##################################
"""
Funcion que obtiene datos para una provincia especifica.
input: lista
output: lista
"""
#-----------------------------------------------------------------------


def obtenerDatosProvincia(lista_cantones):
    provincia = [lista_cantones[0][0]]
    votos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for canton in lista_cantones:
        for i in range(2, 17):
            votos[i - 2] += canton[i]
    provincia += votos
    return provincia
#-----------------------------------------------------------------------


################################### 14 ##################################
"""
Funcion que obtiene datos para todas las provincias.
input:
output: lista de sublistas
"""
#-----------------------------------------------------------------------


def obtener_votos_cada_provincias():
    global provincias
    votos_provincia = []
    for provincia in provincias:
        cantones = cargar_datos_cantones(provincia)
        tempo = obtenerDatosProvincia(cantones)
        votos_provincia += [tempo]
    return votos_provincia
#-----------------------------------------------------------------------


################################### 15 ##################################
"""
Funcion que obtiene los votos totales de todos los partidos politicos.
input: lista
output: lista
"""
#-----------------------------------------------------------------------


def votos_totales(lista_votos):
    votos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for voto in lista_votos:
        for i in range(1, 16):
            votos[i - 1] += voto[i]
    return votos
#-----------------------------------------------------------------------


################################### 16 ##################################
"""
Funcion que calcula promedio de votos por provincia.
input:
output: lista de sublistas
"""
#-----------------------------------------------------------------------


def promedio_votos_por_provincia():
    global total
    if len(total) == 0:
        leerArchivoCSV()
    votos_por_provincia = obtener_votos_cada_provincias()
    cantidad_de_votos = votos_totales(votos_por_provincia)
    total_votos = suma_partes_lista(cantidad_de_votos)
    for provincia in votos_por_provincia:
        for i in range(1, 16):
            provincia[i] = provincia[i] / total_votos
   # print(total_votos)
    #print(votos_por_provincia )
    return votos_por_provincia
#-----------------------------------------------------------------------


################################### 17 ##################################
"""
Funcion que retorna lista con nombre de provincia y el voto, segun la probabilidad.
input: lista, int
output: lista de sublistas
"""
#-----------------------------------------------------------------------


def lista_probalidades_voto_provincia(
        lista_promedio_votos_por_provincia, numero):
    global partidos_politicos
    probabilidades = []
    for provincia in lista_promedio_votos_por_provincia:
        for i in range(1, 16):
            probabilidades += int(provincia[i] * numero) * \
                [[provincia[0], partidos_politicos[i - 1]]]
    return probabilidades
#-----------------------------------------------------------------------


################################### 18 ##################################
"""
Funcion que genera los votos pais.
input: int
output: lista de sublistas
"""
#-----------------------------------------------------------------------


def generar_muestra_pais(numero):
    global total
    if len(total) == 0:
        leerArchivoCSV("datos.csv")
    
    promedio_votos_x_provincia = promedio_votos_por_provincia()
    lista_voto_provincia = lista_probalidades_voto_provincia(
        promedio_votos_x_provincia, numero)
    votantes = []
    for i in range(numero):
        edad = random.randrange(18, 82, 2)
        numero = random.randrange(len(lista_voto_provincia))
        cantones = cargar_datos_cantones(lista_voto_provincia[numero][0])
        votos_t = calcular_cantidad_voto_por_canton(cantones)
        promedio_voto = calcular_probabilidad_voto_por_partido_canton(
            cantones, votos_t)
        lista_promedio_cantones = escoger_canton_segun_voto(
            lista_voto_provincia[numero][1], promedio_voto, numero)

        canton = random.randrange(len(lista_promedio_cantones))

        if isinstance(lista_promedio_cantones[canton], float):
            canton_x= seleccionar_canton_random(
                    lista_voto_provincia[numero][0])
            indicadores = obtener_inidicadores_canton(canton_x
                , cantones)
            
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            tempo = [
                    [lista_voto_provincia[numero][0]] + 
                     [canton_x] +
                     indicadores + [sexo] + [edad] + [lista_voto_provincia[numero][1]]]
           
##            if tempo[0][0]=="SAN JOSE" :
##                print(tempo[0][0],tempo[0][1])
##                tempo[0] += [voto_segunda_ronda_canton(tempo[0][0],tempo[0][1])]
##            
           
        else:
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)

            sexo = asignar_sexo(indicadores[23], indicadores[24])
            tempo = [
                    [lista_voto_provincia[numero][0]] +
                     [lista_promedio_cantones[canton]] +
                     indicadores + [sexo] + [edad] + [lista_voto_provincia[numero][1]]]
            
           
##            if tempo[0][0]=="SAN JOSE"  :
##                print(tempo[0][0],tempo[0][1])
##                tempo[0] += [voto_segunda_ronda_canton(tempo[0][0],tempo[0][1])]
         
        votantes += tempo

    return votantes
#-----------------------------------------------------------------------


################################### 19 ##################################
"""
Funcion que genera un canton random en caso de error.
input:  string
output: string
"""
#-----------------------------------------------------------------------


def seleccionar_canton_random(provincia):
    global total
    tempo = []
    for i in total:
        if i[0] == provincia:
            tempo += [i[1]]
    numero = random.randrange(len(tempo))
    return tempo[numero]
#-----------------------------------------------------------------------


################################### 20 ##################################
"""
Funcion que calcula votos de un partido para una provincia.
input: string, string, lista
output: lista de sublistas
"""
#-----------------------------------------------------------------------
# def contar_votos_partidos(provincia, partido, lista):
##    contador = 0
# for i in lista:
# if i[0] == provincia and i[1] == partido:
##            contador += 1
# return contador

#-----------------------------------------------------------------------

################################### 21 ##################################
"""
Funcion que retorna cantidad votos validos por canton
"""
#-----------------------------------------------------------------------
# def calcular_votos_validos():
##    global total, votos_validos
##    num_total = 0
##    tempo = []
# for i in total:
##        tempo += [i[0], i[1]]
# for j in range(2, 15):
##            num_total += i[j]
##        tempo += [num_total]
##        votos_validos += [tempo]
##        tempo = []
# return
#-----------------------------------------------------------------------
################################### 22 ##################################
"""
Funcion que escribe los datos generados en un archivo txt.
input: lista de sublistas
output: file
"""
#-----------------------------------------------------------------------
def escribir_archivo(lista):
    file = open("testfile.txt", "w")
    for i in lista:
        file.write(str(i))
        file.write("\n")
    file.close()
    print("termine")
#-----------------------------------------------------------------------


###############################################################################
####################Codigo Primer Proyecto#####################################

"""
Funcion que busca y retorna los datos de un canton en la segunda ronda.
input: string nombrecanton
output: lista datos canton
"""

def buscar_canton_segunda_ronda(nombre_provincia,nombre_canton):
    global segundaRonda 
    if segundaRonda == []:
        leerArchivoCSV2("segundaRonda.csv")
    else:
        tempo = []
        for canton in segundaRonda:
            if  canton[1]== nombre_canton:
                return canton
        
def voto_segunda_ronda_canton(nombre_provincia,nombre_canton):
    
    global segundaRonda
    if segundaRonda == []:
        leerArchivoCSV2("segundaRonda.csv")
    datos_canton= buscar_canton_segunda_ronda(nombre_provincia,nombre_canton)
    total_votos = datos_canton[2] + datos_canton[3] + datos_canton[4] + datos_canton[5]
    rango_pac = datos_canton[2]
    rango_rn = [rango_pac+1, rango_pac+datos_canton[3]]
    rango_nulo = [rango_rn[1]+1, rango_rn[1]+ datos_canton[4]]
    rango_blanco = [rango_nulo[1]+1, rango_nulo[1]+ datos_canton[4]]
    voto = random.randrange(1,total_votos, 1)
    if (voto<= rango_pac):
        return "ACCION CIUDADANA"
    elif voto >= rango_rn[0] and voto <= rango_rn[1]:
        return "RESTAURACION NACIONAL"
    elif voto >= rango_nulo[0] and voto <= rango_nulo[1]:
        return "NULO"
    elif voto >= rango_blanco[0] and voto <= rango_blanco[1]:
        return "BLANCO"

    

def prueba_segunda_ronda():
    pac=0
    rn=0
    n=0
    b=0
    for i in range(0,1000):
        x= voto_segunda_ronda_canton("SAN JOSÉ","ESCAZU")
        if x =="ACCION CIUDADANA":
            pac+=1
        elif x == "RESTAURACION NACIONAL":
            rn+=1
        elif x == "NULOS":
            n+=1
        elif x == "BLANCO":
            b+=1
    return (pac,rn,n,b)

###################
def dividir_entradas_salidas(lista_votos):
    inputs=[]
    outputs=[]
    for i in lista_votos:
        x = cambiar_nombre_por_numero(i[0])
        i[0] = x
        i[1] = cambiar_nombre_por_numero_cantones(i[1])
        
        i[-1] = cambiar_nombre_por_numero_voto(i[-1])
        if i[1] == None:
            i[1] = 1
        if i[-3]=="HOMBRE":
            i[-3]=1
        if i[-3]=="MUJER":
            i[-3]=0
            
        inputs += [i]
    
    return inputs

def cambiar_nombre_por_numero(nombre):
    lista_numero_provincias = [["SAN JOSE",1],["HEREDIA",4],["CARTAGO",3],["ALAJUELA",2],["LIMON",7],["GUANACASTE",5],["PUNTARENAS",6]]
    for i in lista_numero_provincias:
        if nombre == i[0]:
            return i[1]
def cambiar_nombre_por_numero_voto(nombre):
    partidos_politicos_n = [
        ["ACCESIBILIDAD SIN EXCLUSION",1],
        ["ACCION CIUDADANA",2],
        ["ALIANZA DEMOCRATA CRISTIANA",3],
        ["DE LOS TRABAJADORES",4],
        ["FRENTE AMPLIO",5],
        ["INTEGRACION NACIONAL",6],
        ["LIBERACION NACIONAL",7],
        ["MOVIMIENTO LIBERTARIO",8],
        ["NUEVA GENERACION",9],
        ["RENOVACION COSTARRICENSE",10],
        ["REPUBLICANO SOCIAL CRISTIANO",11],
        ["RESTAURACION NACIONAL",12],
        ["UNIDAD SOCIAL CRISTIANA",13],
        ["NULO",14],
        ["BLANCO",15]]
    for i in partidos_politicos_n:
        if nombre == i[0]:
            return i[1]


def cambiar_nombre_por_numero_cantones(nombre):
    cantones = [['SAN JOSE CENTRAL',1],['ESCAZU',2],['DESAMPARADOS',3],['PURISCAL',4],['TARRAZU',5],['ASERRI',6],['MORA',7],['GOICOCHEA',8],['SANTA ANA',9],['ALAJUELITA',10],
        ['VAZQUEZ DE CORONADO',11],['ACOSTA',12],['TIBAS',13],['MORAVIA',14],['MONTES DE OCA',15],['TURRUBARES',16],['DOTA',17],['CURRIDABAT',18],['PEREZ ZELEDON',19],
        ['LEON CORTEZ CASTRO',20],['ALAJUELA CENTRAL',21],['SAN RAMON',22],['GRECIA',23],['SAN MATEO',24],['ATENAS',25],['NARANJO',26],['PALMARES',27],['POAS',28],['OROTINA',29],
        ['SAN CARLOS',30],['ZARCERO',31],['VALVERDE VEGA',32],['UPALA',33],['LOS CHILES',34],['GUATUSO',35],['CARTAGO CENTRAL',36],['PARAISO',37],['LA UNION',38],['JIMENEZ',39],
        ['TURRIALBA',40],['ALVARADO',41],['OREAMUNO',42],['EL GUARCO',43],['HEREDIA CENTRAL',44],['BARVA',45],['SANTO DOMINGO',46],['SANTA BARBARA',47],['SAN RAFAEL',48],['SAN ISIDRO',49],
        ['BELEN',50],['FLORES',51],['SAN PABLO',52],['SARAPIQUI',53],['LIBERIA',54],['NICOYA',55],['SANTA CRUZ',56],['BAGACES',57],['CARRILLO',58],['CAÑAS',59],['ABANGARES',60],
        ['TILARAN',61],['NANDAYURE',62],['LA CRUZ',63],['HOJANCHA',64],['PUNTARENAS CENTRAL',65],['ESPARZA',66],['BUENOS AIRES',67],['MONTES DE ORO',68],['OSA',69],['QUEPOS',70],['GOLFITO',71],
        ['COTO BRUS',72],['PARRITA',73],['CORREDORES',74],['GARABITO',75],['LIMON CENTRAL',76],['POCOCI',77],['SIQUIRRES',78],['TALAMANCA',79],['MATINA',80],['GUACIMO',81]]
    for i in cantones:
        if nombre == i[0]:
            return i[1]

def escribir_csv(res):
    for i in res:
        tempo = i[0]
        i[0] = i[-1]
        i[-1] = tempo
        
    with open("testfile.csv", "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerow(['Voto', 'CANTON', 'Poblacion_total', 'Superficie (km2)', 'Densidad de población', 'Porcentaje de población urbana', 'Relación hombres-mujeres', 'Relación de dependencia demográfica', 'Viviendas individuales ocupadas', 'Promedio de ocupantes', 'Porcentaje de viviendas en buen estado', 'Porcentaje de viviendas hacinadas', 'Porcentaje de alfabetismo', '10 a 24 años', '25 y más años', 'Escolaridad promedio', '25 a 49 años', '50 o más años', 'Porcentaje de asistencia a la educación regular', 'Menor de 5 años', '5 a 17 años', '18 a 24 años', '25 y más años.1', 'Personas fuera de la fuerza de trabajo (15 años y más)', 'Tasa neta de participación', 'Hombres', 'Mujeres', 'Porcentaje de población ocupada no asegurada', 'Porcentaje de población nacida en el extranjero', 'Porcentaje de población con discapacidad', 'Porcentaje de población no asegurada', 'Porcentaje de hogares con jefatura femenina', 'Porcentaje de hogares con jefatura compartida','Sexo','Edad','PROVINCIA'])
        writer.writerows(res)
        print("Termine")
###################################################################################
        #####SegundaRegresion
####################################################################################
def generar_muestra_pais_con_segunda(numero):
    global total,segundaRonda
    if len(total) == 0:
        leerArchivoCSV("datos.csv")
    promedio_votos_x_provincia = promedio_votos_por_provincia()
    lista_voto_provincia = lista_probalidades_voto_provincia(
        promedio_votos_x_provincia, numero)
    votantes = []
    for i in range(numero):
        edad = random.randrange(18, 82, 2)
        numero = random.randrange(len(lista_voto_provincia))
        cantones = cargar_datos_cantones(lista_voto_provincia[numero][0])
        votos_t = calcular_cantidad_voto_por_canton(cantones)
        promedio_voto = calcular_probabilidad_voto_por_partido_canton(
            cantones, votos_t)
        lista_promedio_cantones = escoger_canton_segun_voto(
            lista_voto_provincia[numero][1], promedio_voto, numero)

        canton = random.randrange(len(lista_promedio_cantones))

        if isinstance(lista_promedio_cantones[canton], float):
            canton_x= seleccionar_canton_random(
                    lista_voto_provincia[numero][0])
            indicadores = obtener_inidicadores_canton(canton_x
                , cantones)
            
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            voto_segunda= voto_segunda_ronda_canton(lista_voto_provincia[numero][0],canton_x)
            tempo = [
                    [lista_voto_provincia[numero][0]] + 
                     [canton_x] +
                     indicadores + [sexo] + [edad] + [lista_voto_provincia[numero][1]]+[voto_segunda]]
  
        else:
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            voto_segunda= voto_segunda_ronda_canton(lista_voto_provincia[numero][0],lista_promedio_cantones[canton])
            tempo = [
                    [lista_voto_provincia[numero][0]] +
                     [lista_promedio_cantones[canton]] +
                     indicadores + [sexo] + [edad] + [lista_voto_provincia[numero][1]]+[voto_segunda]]
              
         
        votantes += tempo

    return votantes
#-----------------------------------------------------------------------

def dividir_entradas_salidas2(lista_votos):
    inputs=[]
    outputs=[]
    for i in lista_votos:
        i[0] = cambiar_nombre_por_numero(i[0])
        i[1] = cambiar_nombre_por_numero_cantones(i[1])
        
        i[-1] = cambiar_nombre_por_numero_voto(i[-1])
        i[-2] = cambiar_nombre_por_numero_voto(i[-2])
        if i[1] == None:
            i[1] = 1
        if i[-4]=="HOMBRE":
            i[-4]=1
        if i[-4]=="MUJER":
            i[-4]=0
            
        inputs += [i]
    
    return inputs

def escribir_csv2(res):
    for i in res:
        tempo = i[0]
        i[0] = i[-1]
        i[-1] = tempo
        
    with open("testfile.csv", "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerow(['Voto', 'CANTON', 'Poblacion_total', 'Superficie (km2)', 'Densidad de población', 'Porcentaje de población urbana', 'Relación hombres-mujeres', 'Relación de dependencia demográfica', 'Viviendas individuales ocupadas', 'Promedio de ocupantes', 'Porcentaje de viviendas en buen estado', 'Porcentaje de viviendas hacinadas', 'Porcentaje de alfabetismo', '10 a 24 años', '25 y más años', 'Escolaridad promedio', '25 a 49 años', '50 o más años', 'Porcentaje de asistencia a la educación regular', 'Menor de 5 años', '5 a 17 años', '18 a 24 años', '25 y más años.1', 'Personas fuera de la fuerza de trabajo (15 años y más)', 'Tasa neta de participación', 'Hombres', 'Mujeres', 'Porcentaje de población ocupada no asegurada', 'Porcentaje de población nacida en el extranjero', 'Porcentaje de población con discapacidad', 'Porcentaje de población no asegurada', 'Porcentaje de hogares con jefatura femenina', 'Porcentaje de hogares con jefatura compartida','Sexo','Edad','Voto primera','PROVINCIA'])
        writer.writerows(res)
        print("Termine")

def generar_muestra_provincia2(n, provincia):
    global votos_provincia, partidos_politicos
    partidos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    leerArchivoCSV("datos.csv")
    cantones = cargar_datos_cantones(provincia)
    votos_t = calcular_cantidad_voto_por_canton(cantones)
    promedio_voto = calcular_probabilidad_voto_por_partido_canton(
        cantones, votos_t)
    sumar_todos_por_provincia(provincia)
    votos = votos_provincia[1]
    # print(votos_provincia[1])
    votantes_simulados = []
    for i in range(1, n + 1):
        numero = random.randrange(votos_provincia[2])
        edad = random.randrange(18, 82, 2)
        if (numero <= suma_partes_lista([votos[0]])):
            partidos[0] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[0], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            voto_segunda= voto_segunda_ronda_canton("",lista_promedio_cantones[canton])
            tempo = [[lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[0]]+[voto_segunda]]
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista([votos[0]]) and numero <= suma_partes_lista(votos[:2])):
            partidos[1] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[1], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            voto_segunda= voto_segunda_ronda_canton("",lista_promedio_cantones[canton])
            tempo = [[lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[1]]+[voto_segunda]] 
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:2]) and numero <= suma_partes_lista(votos[:3])):
            partidos[2] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[2], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            voto_segunda= voto_segunda_ronda_canton("",lista_promedio_cantones[canton])
            tempo = [[lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[2]]+[voto_segunda]]
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:3]) and numero <= suma_partes_lista(votos[:4])):
            partidos[3] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[3], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            voto_segunda= voto_segunda_ronda_canton("",lista_promedio_cantones[canton])
            tempo = [[lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[3]]+[voto_segunda]] 
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:4]) and numero <= suma_partes_lista(votos[:5])):
            partidos[4] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[4], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            voto_segunda= voto_segunda_ronda_canton("",lista_promedio_cantones[canton])
            tempo = [[lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[4]]+[voto_segunda]] 
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:5]) and numero <= suma_partes_lista(votos[:6])):
            partidos[5] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[5], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            voto_segunda= voto_segunda_ronda_canton("",lista_promedio_cantones[canton])
            tempo = [[lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[5]]+[voto_segunda]]
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:6]) and numero <= suma_partes_lista(votos[:7])):
            partidos[6] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[6], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            voto_segunda= voto_segunda_ronda_canton("",lista_promedio_cantones[canton])
            tempo = [[lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[6]]+[voto_segunda]] 
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:7]) and numero <= suma_partes_lista(votos[:8])):
            partidos[7] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[7], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            voto_segunda= voto_segunda_ronda_canton("",lista_promedio_cantones[canton])
            tempo = [[lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[7]]+[voto_segunda]]
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:8]) and numero <= suma_partes_lista(votos[:9])):
            partidos[8] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[8], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            voto_segunda= voto_segunda_ronda_canton("",lista_promedio_cantones[canton])
            tempo = [[lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[8]]+[voto_segunda]]
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:9]) and numero <= suma_partes_lista(votos[:10])):
            partidos[9] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[9], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            voto_segunda= voto_segunda_ronda_canton("",lista_promedio_cantones[canton])
            tempo = [[lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[9]]+[voto_segunda]]
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:10]) and numero <= suma_partes_lista(votos[:11])):
            partidos[10] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[10], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            voto_segunda= voto_segunda_ronda_canton("",lista_promedio_cantones[canton])
            tempo = [[lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[10]]+[voto_segunda]]
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:11]) and numero <= suma_partes_lista(votos[:12])):
            partidos[11] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[11], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            voto_segunda= voto_segunda_ronda_canton("",lista_promedio_cantones[canton])
            tempo = [[lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[11]]+[voto_segunda]]
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:12]) and numero <= suma_partes_lista(votos[:13])):
            partidos[12] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[12], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            voto_segunda= voto_segunda_ronda_canton("",lista_promedio_cantones[canton])
            tempo = [[lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[12]]+[voto_segunda]]
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:13]) and numero <= suma_partes_lista(votos[:14])):
            partidos[13] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[13], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            voto_segunda= voto_segunda_ronda_canton("",lista_promedio_cantones[canton])
            tempo = [[lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[13]]+[voto_segunda]]
            votantes_simulados += tempo
            tempo = []
        elif (numero > suma_partes_lista(votos[:14]) and numero <= suma_partes_lista(votos)):
            partidos[14] += 1
            lista_promedio_cantones = escoger_canton_segun_voto(
                partidos_politicos[14], promedio_voto, n)
            canton = random.randrange(len(lista_promedio_cantones))
            indicadores = obtener_inidicadores_canton(
                lista_promedio_cantones[canton], cantones)
            sexo = asignar_sexo(indicadores[23], indicadores[24])
            voto_segunda= voto_segunda_ronda_canton("",lista_promedio_cantones[canton])
            tempo = [[lista_promedio_cantones[canton]] + indicadores + [sexo] + [edad]+ [partidos_politicos[14]]+[voto_segunda]]
            votantes_simulados += tempo
            tempo = []
    # print(partidos)
    return votantes_simulados



def retornarArray():
    datos= leerArchivoCSV('testfile.csv')
    array = datos[0] + datos[1] + datos[-1]
    print(array)


def escribir_csv3(res):
    for i in res:
        tempo = i[0]
        i[0] = i[-1]
        i[-1] = tempo
        
    with open("testfile.csv", "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(res)
        print("Termine")


def escribir_csv4(res):
    for i in res:
        tempo = i[0]
        i[0] = i[-1]
        i[-1] = tempo
        
    with open("testfile.csv", "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(res)
        print("Termine")

def leerArchivoCSV_with_header(nombre):
    result = []
    with open(nombre) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            result += [row]
    return cambiar_valores_csv(result)

def leerArchivoCSV_with_header2(nombre):
    result = []
    with open(nombre) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            result += [row]
    return result

def cambiar_valores_csv(lista):
    for i in range(1,len(lista)):
        
        for j in range(len(lista[i])):
            if type(eval(lista[i][j])) == int:
                lista[i][j]=int(lista[i][j])
            elif type(eval(lista[i][j])) == float:
                lista[i][j]=float(lista[i][j])
    return dar_formato_arbol_decision_edad(lista)

def dar_formato_arbol_decision_edad(lista):
    for i in range(1,len(lista)):
        if int(lista[i][-3]) <= 25:
            lista[i][-3] = "18-25"
        elif int(lista[i][-3]) >= 26 and int(lista[i][-3]) <= 40:
         
            lista[i][-3] = "26-40"
        elif int(lista[i][-3]) >= 41 and int(lista[i][-3]) <= 55  :
            lista[i][-3] = "41-55"
        elif int(lista[i][-3]) > 55  :
            lista[i][-3] = "55+"
    return lista



##################################################################################
##########################arbol###################################################

import math
def funcion_B(q):
    if q ==0 or q == 1:
        return 0
    else:
        result = -(q * math.log2(q)+(1-q)*math.log2(1-q))
        return result

def funcion_H_Goal(lista):
    positivos = 0
    negativos = 0
    for i in range(1,len(lista)):
        if int(lista[i][0]) == 2:
            positivos += 1
        elif int(lista[i][0]) == 12:
            negativos += 1
    return funcion_B((positivos/(positivos+negativos)))



def encontrar_diferentes_columna(lista,columna):
    tempo = []
    for i in range(1,len(lista)):
        if lista[i][columna] not in tempo:
            tempo.append(lista[i][columna])
    tempo2 = []
    for j in tempo:
        tempo2 +=[[j,0,0,0]]
    return contador_atributos(lista,tempo2,columna)

def contador_atributos(lista1,lista2,columna):
    for i in lista1:
        for j in lista2:
           if i[columna] == j[0]:
               j[1] += 1
               if i[0] == 2:
                   j[2] += 1
               elif i[0] == 12:
                   j[3] += 1
    return lista2

def remainder_general(parametros):
    total = 0
    for i in parametros:
        total += i[1]
    result = 0
    for j in parametros:
        suma = j[2]+j[3]
        if suma == 0:
            suma = 1
        result += ((suma)/total)*funcion_B(j[2]/(suma))
    return result

def gain():
    x = leerArchivoCSV_with_header("testfile.csv")
    for i in range(len(x[0])):
        print("Calculando valor con: ",x[0][i])
        y = encontrar_diferentes_columna(x,i)
        print(funcion_H_Goal(x)-remainder_general(y))
    return

