"""
Crear y cargar en un lista los nombres de 5 países y en otra lista paralela la cantidad de habitantes del mismo. 
Ordenar alfabéticamente e imprimir los resultados. 
Por último ordenar con respecto a la cantidad de habitantes (de mayor a menor) e imprimir nuevamente.

"""
#Creacion de listas:

paises=[]
habitantes=[]
for x in range(5):
    pais=input("Ingrese pais: ")
    paises.append(pais)
    habitan=int(input("Ingrese cantidad de habitantes: "))
    habitantes.append(habitan)

#Ordenamiento alfabetico: 

for f in range(4):
    for x in range(4):
        if paises[x]>paises[x+1]:
            aux1=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux1
            aux2=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux2

print("Lista de paises y sus habitantes ordenados alfabeticamente: ")
for x in range(5):
    print(paises[x], habitantes[x])

#Ordenamiento de habitantes. De mayor a menor:

for f in range(4):
    for x in range(4):
        if habitantes[x]<habitantes[x+1]:
            aux2=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux2
            aux1=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux1

print("Lista de paises y sus habitantes ordenados de mayor a menor: ")
for x in range(5):
    print(paises[x], habitantes[x])
