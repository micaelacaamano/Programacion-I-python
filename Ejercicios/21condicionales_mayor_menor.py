"""
Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe 
cuántos tienen notas mayores o iguales a 7 y cuántos menores.

"""
x=0
altas=0
bajas=0
while x<=10:
    alumno=int(input("Ingrese nota del alumno: "))
    if alumno>=7:
        altas=altas+1
    else:
        bajas=bajas+1
    x=x+1
print("La cantidad de alumnos con notas superiores a 7 es: ",altas)
print("La cantidad de alumnos con notas inferiores a 7 es: ",bajas)