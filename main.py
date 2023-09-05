

import string
import random

filas = 10
columnas = 10
matriz = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(random.choice(string.ascii_letters).lower())
        #fila.append(".")        
    matriz.append(fila)
    
import nltk

from nltk.corpus import cess_esp

palabras_espanol = cess_esp.words()
palabras_espanol_filtradas = []

for palabra in palabras_espanol:
    if len(palabra) >= 4 & len(palabra) < filas:
        palabras_espanol_filtradas.append(palabra)



palabra = random.choice(palabras_espanol_filtradas)
palabra = palabra.upper()
    
print(palabra)    
print("SOPA DE LETRAS")
print("--------------")

#palabra = "breixo"

opcion_posicion = random.randint(0, 3)
opcion_reverse = random.randint(0, 1)

def invertir_cadena(cadena):
    return cadena[::-1]

if opcion_reverse == 1:
    palabra = invertir_cadena(palabra)


if opcion_posicion == 0:
    i = random.randint(0, filas - 1)
    j = random.randint(0, columnas - len(palabra))
    pos_letra = 0
    for y in range(j, j + len(palabra)): #columnas - len(palabra) es donde debe comenzar a dibujar la palabra
        matriz[i][y] = palabra[pos_letra]
        pos_letra += 1
elif opcion_posicion == 1:
    j = random.randint(0, columnas - 1)
    i = random.randint(0, filas - len(palabra))
    pos_letra = 0
    for x in range(i, i + len(palabra)): #columnas - len(palabra) es donde debe comenzar a dibujar la palabra
        matriz[x][j] = palabra[pos_letra]
        pos_letra += 1
elif opcion_posicion == 2:
    i = random.randint(0, filas - len(palabra))
    j = random.randint(0, columnas - len(palabra))
    pos_letra = 0
    for x in range(i, i + len(palabra)): #columnas - len(palabra) es donde debe comenzar a dibujar la palabra
        matriz[x][j] = palabra[pos_letra]
        j += 1
        pos_letra += 1
else:
    i = random.randint(0, filas - len(palabra))
    j = random.randint(len(palabra) - 1, filas - 1)
    pos_letra = 0
    for x in range(i, i + len(palabra)): #columnas - len(palabra) es donde debe comenzar a dibujar la palabra
        matriz[x][j] = palabra[pos_letra]
        j -= 1
        pos_letra += 1    





    
    
     
    
for x in range(filas):
    for y in range(columnas):
        print(matriz[x][y], end="")
    print("")



#la orientacion se atablece de manera random, tanto si la palabra se muestra de manera horizontal o vertical

#este practicamente ya no vale
"""j = random.randint(0, columnas)
i = random.randint(0, filas - len(palabra))
pos_letra = 0
for x in range(i, i + len(palabra)): #columnas - len(palabra) es donde debe comenzar a dibujar la palabra
    matriz[x][x] = palabra[pos_letra]
    pos_letra += 1"""
