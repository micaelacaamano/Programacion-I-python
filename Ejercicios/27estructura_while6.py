"""
Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos 
valores fueron pares y cuántos impares.

"""
contador=1
pares=0
impares=0
empleados=int(input("Ingrese la cantidad de numeros a ingresar: "))
while contador<=empleados:
    valor=int(input("Ingrese valor entero: "))
    if valor%2==0:
        pares=pares+1
    else:
        impares=impares+1
    contador=contador+1
print("La cantidad de numeros impares son: ",impares)
print("La cantidad de numeros pares son: ",pares)