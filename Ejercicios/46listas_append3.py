"""
Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados 
(4 por la mañana y 4 por la tarde) Confeccionar un programa que permita almacenar 
los sueldos de los empleados agrupados en dos listas. Imprimir las dos listas de sueldos.

"""
lista1=[]
lista2=[]
print("Sueldos del turno mañana: ")
for x in range(4):
    valor=int(input("Ingrese su valor: "))
    lista1.append(valor)
print("Sueldos del turno tarde: ")
for x in range(4):
    valor=int(input("Ingrese su valor: "))
    lista2.append(valor)
print("Lista de sueldos turno mañana: ",lista1)
print("Lista de sueldos turno tarde: ",lista2)