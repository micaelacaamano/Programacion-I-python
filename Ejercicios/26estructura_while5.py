"""
Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un mensaje 
cual de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.

"""
contador=1
lista1=0
lista2=0
print("Primera lista de valores: ")
while contador<=15:
    suma1=int(input("Ingrese valores: "))
    lista1=lista1+suma1
    contador=contador+1
print("Segunda lista de valores: ")
contador=1
while contador<=15:
    suma2=int(input("Ingrese valores: "))
    lista2=lista2+suma2
    contador=contador+1
if lista1>lista2:
    print("Lista 1 mayor")
else:
    if lista1<lista2:
        print("Lista 2 mayor")
    else:
        print("Listas iguales")