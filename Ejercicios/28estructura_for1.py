"""
Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida 
de la base y la altura de un triángulo. El programa deberá informar:

a) De cada triángulo la medida de su base, su altura y su superficie.
b) La cantidad de triángulos cuya superficie es mayor a 12 (la superficie se calcula multiplicando la base por la altura y a este valor dividiendolo en 2)

"""

base=0
altura=0
contador = 0
cantidad=int(input("Ingrese cantidad de triangulos a analizar: "))
for x in range(cantidad):
    dato1=int(input("Ingrese la medida de la base: "))
    dato2=int(input("Ingrese la medida de altura: "))
    superficie=dato1*dato2/2
    print("La base de este triangulo es: ",dato1)
    print("La altura de este triangulo es: ",dato2)
    print("La superficie del triangulo es: ",superficie)

    if superficie > 12:
        contador = contador + 1

print("Cantidad de triangulos con superficie mayor a 12:", contador)