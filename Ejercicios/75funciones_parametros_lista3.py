"""
Definir una lista de enteros por asignación en el bloque principal. 
Llamar a una función que reciba la lista y nos retorne el producto de todos sus elementos. 
Mostrar dicho producto en el bloque principal de nuestro programa.

""" 
def producto(lista):
    multi=1
    for x in range(len(lista)):
        multi=multi*lista[x]
    return multi

#Bloque principal:
lista=[1, 2, 3, 4, 5]
print("El producto de todos los elementos en la lista es: ", producto(lista))