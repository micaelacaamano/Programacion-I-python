"""
Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo los elementos 
con valor iguales o superiores a 7.

"""
lista=[2, 5, 8, 14, 20]
x=0
print("Los elementos superiores a 7 de la lista son: ")
while x<len(lista):
    if lista[x]>=7:
        print(lista[x])
    x=x+1
