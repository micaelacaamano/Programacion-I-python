"""
Descripción: El Programa solicita dos números enteros y determina si el primero es divisible por el segundo.

- El proceso se repite de forma infinita.
- El programa finaliza cuando el usuario ingresa 0 como divisor.
- Se controla explícitamente el caso de división por cero.

"""

contador=0
divisor=1
while divisor>0:
    entero=int(input("Ingrese el numero: "))
    divisor=int(input("Es divisible por: "))
    if divisor==0:
        print("No es posible dividir por 0")
    else:
        if entero%divisor==0:
            print("Si.")
            contador=contador+1
        else:
            print("No.")
            contador=contador+1