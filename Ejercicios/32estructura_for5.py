"""
Realizar un programa que lea los lados de n triángulos, e informar:
a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles 
(dos lados iguales), o escaleno (ningún lado igual)

b) Cantidad de triángulos de cada tipo.

"""

triangulo=int(input("Ingresa datos a analizar: "))
escaleno=0
equilatero=0
isosceles=0
for x in range(triangulo):
    lado1=int(input("Ingrese valor del lado: "))
    lado2=int(input("Ingrese valor del lado: "))
    lado3=int(input("Ingrese valor del lado: "))
    if lado1==lado2 and lado1==lado3 and lado2==lado1 and lado2==lado3 and lado3==lado1 and lado3==lado2:
        equilatero=equilatero+1
        print("Este triangulo es equilatero")
    else: 
        if lado1!=lado2 and lado1!=lado3 and lado2!=lado1 and lado2!=lado3 and lado3!=lado1 and lado3!=lado2:
            escaleno=escaleno+1
            print("Este triangulo es escaleno")
        else:
            isosceles=isosceles+1
            print("Estre triangulo es isosceles")
print("Cantidad de triangulos escalenos: ",escaleno)
print("Cantidad de triangulos isosceles: ",isosceles)
print("Cantidad de triangulos equilateros: ",equilatero)