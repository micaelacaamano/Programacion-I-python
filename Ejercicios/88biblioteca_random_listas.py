"""
Confeccionar una programa con las siguientes funciones: 

a) Generar una lista con 5 elementos enteros aleatorios comprendidos entre 1 y 3. 
b) Controlar que el primer elemento de la lista sea un 1, en el caso que haya un 2 o mezclar la lista 
y volver a controlar hasta que haya un 1. c) Imprimir la lista.

"""
import random


def cargar():
    lista=[]
    for x in range(4):
        lista.append(random.randint(1, 3))
    lista.append(1)
    return lista

def controlar(lista):
    while lista[0]!=1:
        random.shuffle(lista)

def imprimir(lista):
    print("La lista generada es: ",lista)

#Bloque principal
lista=cargar()
imprimir(lista)
controlar(lista)
imprimir(lista)