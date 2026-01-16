"""
Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el valor por hora.

"""


horastrabajadas=int(input("Ingrese cantidad de horas trabajadas: "))
costohora=int(input("Ingrese el pago por hora: "))
sueldomensual=horastrabajadas*costohora
print("Su sueldo mensual es de: ", sueldomensual)