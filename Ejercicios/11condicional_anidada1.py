"""
Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos.

"""
num1=int(input("ingrese primer valor: "))
num2=int(input("ingrese segundo valor: "))
num3=int(input("ingrese tercer valor: "))
if num1>num2:
    print("El mayor de los valores es: ",num1)
else:
    if num2>num3:
        print("El mayor de los valores es: ",num2)
    else:
        print("El mayor de los valores es: ",num3)