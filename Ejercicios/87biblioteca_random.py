"""
Confeccionar un programa que genere un número aleatorio entre 1 y 100 y no se muestre. 
El operador debe tratar de adivinar el número ingresado. 
Cada vez que ingrese un número mostrar un mensaje "Gano" si es igual al generado o 
"El número aleatorio es mayor" o "El número aleatorio es menor". 
Mostrar cuando gana el jugador cuantos intentos necesitó.

"""
import random

juego=random.randint(1, 100)
elegido=0
intentos=0
while elegido!=juego:
    elegido=int(input("Ingrese su número entre el 1 y 100: "))
    if elegido<juego:
            print("El número aleatorio es mayor.")
    else:
        if elegido>juego:
            print("El número aleatorio es menor.")
        else:
             print("Gano.")
    intentos=intentos+1
print("Ganaste en ", intentos, "intentos.")