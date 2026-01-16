"""
Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a) La cantidad de valores ingresados negativos.
b) La cantidad de valores ingresados positivos.
c) La cantidad de múltiplos de 15.
d) El valor acumulado de los números ingresados que son pares.

"""


positivo=0
negativo=0
multiplo15=0
suma=0
for x in range(10):
    valor=int(input("Ingrese valor: "))
    if valor>0:
        positivo=positivo+1
    else:
        negativo=negativo+1
    if valor%5==0:
        multiplo15=multiplo15+1
    if valor%2==0:
        suma=suma+valor
print("Valores positivos: ",positivo)
print("Valores negativos: ",negativo)
print("Valores multiplos de 15: ",multiplo15)
print("Valor acumulado de numeros pares: ",suma)