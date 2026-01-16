"""
Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor al 
segundo mostrar por pantalla su suma y diferencia, en caso contrario informar el producto y la división
del primero respecto al segundo.

"""

num1=int(input("Ingrese primer valor: "))
num2=int(input("Ingrese segundo valor: "))
if num1>num2:
    suma=num1+num2
    diferencia=num1-num2
    print("La suma de los dos valores es: ",suma)
    print("La diferencia entre los dos valores es: ",diferencia)
else:
    producto=num1*num2
    division=num1/num2
    print("El producto de ambos valores es: ",producto)
    print("La division de ambos valores es: ",division)