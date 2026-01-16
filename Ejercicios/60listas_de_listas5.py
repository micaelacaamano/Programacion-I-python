"""
Definir una lista y almacenar los nombres de 3 empleados. Por otro lado definir otra lista y almacenar 
en cada elemento una sublista con los números de días del mes que el empleado faltó. Imprimir los nombres 
de empleados y los días que faltó. Mostrar los empleados con la cantidad de inasistencias. Finalmente mostrar 
el nombre o los nombres de empleados que faltaron menos días.

"""
#Definimos listas:

empleados=[]
dias=[]

for k in range(3):
    nombre=input("Ingrese nombre del empleado: ")
    empleados.append(nombre)
    cant=int(input("Ingrese cantidad de dias que falto: "))
    for x in range(cant):
        dia=int(input("Ingrese dias faltados: "))
        dias.append(dia)

print("Listado de empleados y los dias que se ausento: ")
for k in range(3):
    print(empleados[k])
    for x in range(len(dias[k])):
        print(dias[k][x])
              
print("Listado de empleados y la cantidad de inasistencias: ")
for x in range(3):
        print(empleados[x], dias[x])

print("Listados de empleados que faltaron menos dias: ")
for x in range(3):
        if dias[x]<dias[x+1]:
            aux=dias[x]
            dias[x]=dias[x+1]
            dias[x+1]=aux
            aux2=empleados[x]
            empleados[x]=empleados[x+1]
            empleados[x+1]=aux2
print(empleados[x], dias[x])
        