"""
Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la lista y el promedio de sueldos.

#Uso del metodo .append

"""

lista=[]
for x in range(5):
    sueldo=float(input("Ingrese su sueldo: "))
    lista.append(sueldo)
print("La lista de sueldos es: ", lista)
promedio=(lista[0]+lista[1]+lista[2]+lista[3]+lista[4])//5
print("El promedio de los sueldos es: ", promedio)