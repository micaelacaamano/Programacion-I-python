"""
Se desea saber la temperatura media trimestral de cuatro paises. Para ello se tiene como dato 
las temperaturas medias mensuales de dichos paises. Se debe ingresar el nombre del país y seguidamente 
las tres temperaturas medias mensuales. Seleccionar las estructuras de datos adecuadas para el almacenamiento 
de los datos en memoria.

a) Cargar por teclado los nombres de los paises y las temperaturas medias mensuales. 
b) Imprimir los nombres de las paises y las temperaturas medias mensuales de las mismas. 
c) Calcular la temperatura media trimestral de cada país. c - Imprimr los nombres de los paises 
y las temperaturas medias trimestrales. b - Imprimir el nombre del pais con la temperatura media trimestral mayor.

"""
#Ingreso de datos:
paises=[]
temperatura=[]
promedio=[]

for x in range(4):
    pais=input("Ingrese el pais: ")
    paises.append(pais)
    temp1=int(input("Ingrese primer medida: "))
    temp2=int(input("Ingrese segunda medida: "))
    temp3=int(input("Ingrese tercer medida: "))
    temperatura.append([temp1, temp2, temp3])

#Listado sin calcular.
print("Listado de paises y sus temperatura en los ultimos tres meses: ")
for x in range(4):
    print(paises[x], temperatura[0])

#Listado calculado el promedio.
for x in range(4):
    prom=(temperatura[x][0]+temperatura[x][1]+temperatura[x][2])/3
    promedio.append(prom)

print("Nombre de los paises y su temperatura trimestral: ")
for x in range(4):
    print(paises[x], promedio[x])

print("Pais con la temperatura media trimestral mayor: ")
for x in range(3):
    if promedio[x]<promedio[x+1]:
        aux=promedio[x]
        promedio[x]=promedio[x+1]
        promedio[x+1]=aux
        aux2=paises[x]
        paises[x]=paises[x+1]
        paises[x+1]=aux2
print(paises[x], promedio[x])