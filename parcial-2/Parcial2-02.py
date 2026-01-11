"""Descripción: Programa que permite ingresar una cantidad variable de palabras por 
teclado y almacenarlas en una lista de strings.

Desde el bloque principal se solicita:

- El ingreso de las palabras
- Una letra a buscar dentro de las palabras
- La impresión de los resultados obtenidos a partir de las funciones
"""

#Generando lista de elementos tipo string.

def ingresar_palabras():
    palabras = []
    n = int(input("Ingrese cantidad de palabras a ingresar: "))
    for x in range(n):
        palabra = input("Ingrese palabra: ")
        palabras.append(palabra)
    return palabras


# Buscar palabras dentro de la lista que contengan la letra a elección
def encontrar_palabras_con_letra(palabras, letra):
    encontradas = []
    for x in range(len(palabras)):
        if palabras[x][0] == letra:
            encontradas.append(palabras[x])

    print("Cantidad de palabras encontradas con la letra ingresada:", len(encontradas))
    print("Palabras encontradas:", encontradas)


# Ordenando palabras según la longitud de las mismas
def ordenar_palabras_longitud(palabras):
    for k in range(len(palabras) - 1):
        for x in range(len(palabras) - 1):
            if len(palabras[x]) > len(palabras[x + 1]):
                aux = palabras[x]
                palabras[x] = palabras[x + 1]
                palabras[x + 1] = aux

    print("Listado de palabras ordenadas de menor a mayor longitud:")
    print(palabras)


# Bloque principal
palabras = ingresar_palabras()
letra = input("Ingrese la letra que quiere buscar: ")
encontrar_palabras_con_letra(palabras, letra)
ordenar_palabras_longitud(palabras)
