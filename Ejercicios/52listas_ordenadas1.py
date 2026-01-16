"""
Crear una lista y almacenar los nombres de 5 países. Ordenar alfabéticamente la lista e imprimirla.

"""

paises=[]
#Creacion de lista:

for x in range(5):
    nombre=input("Ingrese país: ")
    paises.append(nombre)

print("Lista de paises sin ordenar", paises)

#Ordenamiento de lista

for k in range(4):
    for x in range(4):
        if paises[x]>paises[x+1]:
            aux=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux

print("Lista de paises ordenados alfabeticamente: ", paises)