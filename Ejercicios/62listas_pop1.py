"""
Crear dos listas paralelas. En la primera ingresar los nombres de empleados y en la segunda los sueldos 
de cada empleado. Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa. 
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su nombre)

"""
empleados=[]
sueldos=[]

cant=int(input("Ingrese cantidad de empleados: "))

for x in range(cant):
    nombre=input("Ingrese nombre del empleado: ")
    empleados.append(nombre)
    valor=int(input("Ingrese sueldo: "))
    sueldos.append(valor)

print("Lista de empleados y sus respectivos sueldos: ")
for x in range(cant):
    print(empleados[x], sueldos[x])

posicion=0
while posicion<len(sueldos):
    if sueldos[posicion]>=10000:
        empleados.pop(posicion)
        sueldos.pop(posicion)
    else:
        posicion=posicion+1
print("Listado con empleados con sueldos menores a 10000: ")
for x in range(len(sueldos)):
    print(empleados[x], sueldos[x])