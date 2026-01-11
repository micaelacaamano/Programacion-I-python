""" 
Números pares y suma acumulada: descripción:
Programa que solicita al usuario un número entero y:

- Imprime todos los números pares desde el 2 hasta el número ingresado (inclusive).
- Calcula la **suma total** de esos números pares.
- Muestra el resultado final por pantalla. 

"""

suma=0
usuario=int(input("Ingrese un valor entero par: "))
lista=[]
for x in range(2, usuario+1, 2):
    if x%2==0:
        lista.append(x)
        suma=suma+x
    
print("Listado de numeros pares: ", lista)
print("La suma de los numeros pares es: ", suma)