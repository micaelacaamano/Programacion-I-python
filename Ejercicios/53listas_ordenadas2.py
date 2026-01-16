"""
Solicitar por teclado la cantidad de empleados que tiene la empresa. 
Crear y cargar una lista con todos los sueldos de dichos empleados. 
Imprimir la lista de sueldos ordenamos de menor a mayor.

"""
#Cantidad de empleados:

cant=int(input("Ingrese cantidad de empleados: "))

#Sueldos de empleados:

sueldos=[]
for x in range(cant):
    valor=int(input("Ingrese sueldo: "))
    sueldos.append(valor)

#Ordenamiento de sueldos: 

for k in range(cant-1):
    for x in range(cant-1):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux

print("Lista de sueldos ordenada: ", sueldos)