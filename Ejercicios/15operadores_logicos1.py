"""
Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde a Navidad.

"""

dia=int(input("Ingrese dia: "))
mes=int(input("Ingrese mes: "))
año=int(input("Ingrese año: "))
if dia==25 and mes==12:
    print("Esta fecha corresponde a navidad.")
else:
    print("Esta fecha NO corresponde a navidad.")