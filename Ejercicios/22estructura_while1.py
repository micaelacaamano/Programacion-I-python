"""
Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.

"""
x=1
suma=0
n=int(input("Ingrese cantidad de personas: "))
while x<=n:
    altura=float(input("Ingrese altura de la persona: "))
    suma=suma+altura
    x=x+1
promedio=suma/n
print("El promedio es: ",promedio)