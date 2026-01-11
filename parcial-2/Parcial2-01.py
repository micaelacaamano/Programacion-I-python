"""
Descripción: El programa permite ingresar una cantidad variable de empleados por teclado,
almacenando la información en dos listas paralelas:

- Lista de nombres de empleados
- Lista de sueldos correspondientes

"""

def cargar():
    n = int(input("Ingrese la cantidad de empleados en la empresa: "))
    empleados = []
    sueldos = []

    for x in range(n):
        nombre = input("Ingrese nombre del empleado: ")
        empleados.append(nombre)

        valor = int(input("Ingrese monto de sueldo: "))
        sueldos.append(valor)

    return empleados, sueldos


# Calculo para obtener el promedio de todos los sueldos
def calcular_promedio_sueldos(empleados, sueldos):
    suma = 0
    for x in range(len(sueldos)):
        suma = suma + sueldos[x]

    promedio = suma / len(sueldos)
    print("El promedio de los sueldos es de:", promedio)


# Se analizan los sueldos y se obtiene el que tenga sueldo más alto
def obtener_empleado_sueldo_max(empleados, sueldos):
    pos_max = 0

    for x in range(1, len(sueldos)):
        if sueldos[x] > sueldos[pos_max]:
            pos_max = x

    print("Empleado con mayor sueldo es:", empleados[pos_max])


# Analizando la lista de sueldos, ordenamos de menor a mayor los valores
def ordenar_por_sueldos(empleados, sueldos):
    for k in range(len(sueldos) - 1):
        for x in range(len(sueldos) - 1):
            if sueldos[x] > sueldos[x + 1]:
                aux = sueldos[x]
                sueldos[x] = sueldos[x + 1]
                sueldos[x + 1] = aux
                aux2 = empleados[x]
                empleados[x] = empleados[x + 1]
                empleados[x + 1] = aux2

    print("Lista ordenada de empleados y sueldos:")
    for x in range(len(sueldos)):
        print(empleados[x], sueldos[x])


# Bloque principal
empleados, sueldos = cargar()
calcular_promedio_sueldos(empleados, sueldos)
obtener_empleado_sueldo_max(empleados, sueldos)
ordenar_por_sueldos(empleados, sueldos)
