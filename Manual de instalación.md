# Proyecto1_IA
##Prediccion votos

Para utilizar este programa se deben instalar las siguientes librerías:

-Instalacion de tensorflow,keras y librerias dependientes:

 - Descargar python 3.6.2
 - pip3.6 install tensorflow
 - pip3.6 install keras
 - pip3.6 install pandas
 - pip3.6 install seaborn
 - pip3.6 install sklearn

Una vez instaladas esas librerías, se puede utilizar el programa; para eso se debe:
- Descargar el proyecto
- Abrir el shell de Python.
- Abrir en el shell de pytho la ubicación del proyecto.
- Escribir la instruccion: 
 - Para regresión logística para la primer ronda por país: _py main.py regresion_logistica_primer_ronda_pais cant_muestra porcentaje l1/l2_
 - Para regresión logística para la primer ronda por provincia: _py main.py regresion_logistica_primer_ronda_provincia cant_muestra  nombreProvincia porcentaje l1/l2_
 - Para regresión logística para la segunda ronda por país: _py main.py regresion_logistica_primer_ronda_pais cant_muestra porcentaje l1/l2_
 - Para regresión logística para la segunda ronda por país: _py main.py regresion_logistica_primer_ronda_pais cant_muestra  nombreProvincia porcentaje l1/l2_
 - Para regresión logística para la primer y segunda ronda por país: _py main.py regresion_logistica_segunda_y_primer_ronda_pais cant_muestra porcentaje l1/l2_
 - Para regresión logística para la primer y segunda ronda por provincia: _py main.py regresion_logistica_segunda_y_primera_ronda_provincia cant_muestra nombreProvincia porcentaje l1/l2 _
 - Para a red neuronal primer ronda por país: _py main.py red_neuronal_primer_ronda_pais cant_muestra porcentaje cantCapas cantNodos funcionActivacion_ 
 - Para a red neuronal primer ronda por provincia: _py main.py red_neuronal_primer_ronda_provincia cant_muestra provincia porcentaje cantCapas cantNodos funcionActivacion_
 - Para a red neuronal segunda ronda por país: _py main.py red_neuronal_segunda_ronda_pais cant_muestra porcentaje cantCapas cantNodos funcionActivacion_
 - Para a red neuronal segunda ronda por provincia: _py main.py red_neuronal_segunda_ronda_provincia cant_muestra provincia porcentaje cantCapas cantNodos funcionActivacion_
 - Para a red neuronal primera y segunda ronda por país: _py main.py red_neuronal_segunda_y_primera_ronda_pais cant_muestra porcentaje cantCapas cantNodos funcionActivacion_
 - Para a red neuronal primera y segunda ronda por provincia: _py main.py red_neuronal_segunda_y_primera_ronda_provincia cant_muestra provincia porcentaje cantCapas cantNodos funcionActivacion_
 - Para el árbol de desición primer ronda por país: _py main.py decision_tree_primera_pais cantMuestra porcentaje umbral_
 - Para el árbol de desición primer ronda por provincia: _py main.py decision_tree_primera_provincia cantMuestra provincia porcentaje umbral_
 - Para el árbol de desición segunda ronda por país: _py main.py decision_tree_segunda_pais cantMuestra porcentaje umbral_
 - Para el árbol de desición segunda ronda por provincia: _py main.py decision_tree_segunda_provincia cantMuestra provincia porcentaje umbral_
 - Para el árbol de desición primer y segunda ronda por país: _py main.py decision_tree_segunda_y_primer_pais cantMuestra porcentaje umbral_
 - Para el árbol de desición primer y segunda ronda por provincia: _py main.py decision_tree_segunda_y_primer_provincia cantMuestra provincia porcentaje umbral_
 - K-D Tree para la primer ronda por país: _py main.py kd_tree_primera_pais cantMuestras porcentaje k_
 - K-D Tree para la primer ronda por provincia: _py main.py kd_tree_primera_provincia cantMuestras provincia porcentaje k_
 - K-D Tree para la segunda ronda por país: _py main.py kd_tree_segunda_pais cantMuestras k_
 - K-D Tree para la segunda ronda por provincia: _py main.py kd_tree_segunda_provincia cantMuestras provincia porcentaje k_
 - K-D Tree para la primera y segunda ronda por país: _py main.py kd_tree_segunda_y_primer_pais cantMuestras porcentaje k_
 - K-D Tree para la primera y segunda ronda por provincia: _py main.py kd_tree_segunda_y_primer_provincia cantMuestras provincia porcentaje k_
