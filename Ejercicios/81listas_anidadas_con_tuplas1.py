"""
Almacenar en una lista de 5 elementos los nombres de empleados de una empresa junto a sus últimos tres 
sueldos (estos tres valores en una tupla) El programa debe tener las siguientes funciones: 

a)Carga de los nombres de empleados y sus últimos tres sueldos. 
b)Imprimir el monto total cobrado por cada empleado. 
c)Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a 10000 en los últimos tres meses.

"""
def cargar_empleados():
    empleados=[]
    for x in range(5):
        nombre=input("Ingrese nombre del empleado: ")
        suel1=int(input("Ingrese primer sueldo: "))
        suel2=int(input("Ingrese segundo sueldo: "))
        suel3=int(input("Ingrese tercer sueldo: "))
        empleados.append([nombre,(suel1, suel2, suel3)])
    return empleados

def monto_total(empleados):
    print("Monto total cobrado por empleado: ")
    for x in range(5):
        sueldo=empleados[x][1][0]+empleados[x][1][1]+empleados[x][1][2]
        print(empleados[x][0],": ", sueldo)

def ingreso_mayor(empleados):
    print("Empleados con un ingreso trimestral superior: ")
    for x in range(5):
        sueldo=empleados[x][1][0]+empleados[x][1][1]+empleados[x][1][2]
        if sueldo>10000:
            print(empleados[x][0],": ", sueldo)



#Bloque principal:
print("--------------------------")
empleados=cargar_empleados()
print("--------------------------")
monto_total(empleados)
print("--------------------------")
ingreso_mayor(empleados)
