"""
Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos.

"""
def promedio(v1, v2, v3):
    prom=(v1+v2+v3)//3
    return prom
    
#bloque principal:

valor1=int(input("Ingrese primer valor: "))
valor2=int(input("Ingrese segundo valor: "))
valor3=int(input("Ingrese tercer valor: "))
print("El promedio de los valores es: ", promedio(valor1, valor2, valor3))