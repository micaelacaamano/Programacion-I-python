"""
Crear una lista de enteros por asignación. Definir una función que reciba una lista
de enteros y un segundo parámetro de tipo entero. Dentro de la función mostrar
cada elemento de la lista multiplicado por el valor entero enviado.
"""

def multiplicar(lista, valor):
    for x in range(len(lista)):
        print(lista[x] * valor)

# Bloque principal

lista = [3, 7, 8, 10, 2]
print("Lista creada:", lista)
print("Multiplicación de cada elemento de la lista:")
multiplicar(lista, 3)
