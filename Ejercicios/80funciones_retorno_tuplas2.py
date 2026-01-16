"""
Confeccionar un programa con las siguientes funciones: 
a) Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos valores. 
b)Una función que reciba como parámetro dos tuplas con los nombres y sueldos de empleados 
y muestre el nombre del empleado con sueldo mayor. En el bloque principal del programa 
llamar dos veces a la función de carga y seguidamente llamar a la función que muestra el 
nombre de empleado con sueldo mayor.

# bloque principal
empleado1=cargar_empleado()
empleado2=cargar_empleado()
mayor_sueldo(empleado1,empleado2)

"""

def cargar():
    empleado=input("Ingrese nombre del empleado: ")
    sueldo=int(input("Ingrese sueldo del empleado: "))
    return (empleado, sueldo)

def mayor_sueldo(empleado1, empleado2):
    if empleado1[1]>empleado2[1]:
        print(empleado1[0], " tiene mayor sueldo.")
    else:
        print(empleado2[0], "tiene mayor sueldo.")

#bloque principal

empleado1=cargar()
empleado2=cargar()
mayor_sueldo(empleado1, empleado2)