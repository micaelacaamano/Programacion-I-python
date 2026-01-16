"""
En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que 
lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos 
cobran más de $300. Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.

"""
x=0
suma=0
contador1=0
contador2=0
n=int(input("Ingrese cantidad de empleados: "))
while x<=n:
    sueldos=int(input("Ingrese sueldo: "))
    suma=suma+sueldos
    if sueldos<=300:
        contador1=contador1+1
    else:
        contador2=contador2+1
    x=x+1
print("Los empleados que cobran entre $100 y $300 son: ",contador1)
print("Los empleados que cobran mas de $300 son: ",contador2)
print("Importe de gastos de la empresa: ",suma)