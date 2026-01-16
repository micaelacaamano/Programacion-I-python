"""
Confeccionar una función que calcule la superficie de un rectángulo y la retorne, la función 
recibe como parámetros los valores de dos lados distintos:

def retornar_superficie(lado1,lado2):
En el bloque principal del programa cargar los lados de dos rectángulos y luego mostrar 
cual de los dos tiene una superficie mayor.

"""
def retornar_superficie(lado1, lado2):
    superficie = lado1 * lado2
    return superficie

# Bloque principal
base1 = int(input("Ingrese base del primer rectángulo: "))
altura1 = int(input("Ingrese altura del primer rectángulo: "))

base2 = int(input("Ingrese base del segundo rectángulo: "))
altura2 = int(input("Ingrese altura del segundo rectángulo: "))

sup1 = retornar_superficie(base1, altura1)
sup2 = retornar_superficie(base2, altura2)

if sup1 > sup2:
    print("El primer rectángulo tiene mayor superficie.")
else:
    print("El segundo rectángulo tiene mayor superficie.")
