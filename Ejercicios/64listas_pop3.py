"""
Crear una lista y almacenar 5 enteros pedidos por teclado. 
Eliminar todos los elementos que sean iguales al número entero 5.

"""

lista=[]
for x in range(5):
    valor=int(input("Ingrese valor: "))
    lista.append(valor)

print("Lista original:")
print(lista)

posicion=0
while posicion < len(lista):
    if lista[posicion] == 5:
        lista.pop(posicion)
    else:
        posicion = posicion + 1

print("Lista luego de eliminar los valores iguales a 5:")
print(lista)
