"""
Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir dos valores 
enteros x e y (distintos a cero).

Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto. 
(1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)

"""
x=int(input("Ingrese primer valor de coordenada: "))
y=int(input("Ingree segundo valor de coordenada: "))
if x>0 and y>0:
    print("1° cuadrante")
else:
    if x<0 and y>0:
        print("2° cuadrante")
    else:
        if x<0 and y<0:
            print("3° cuadrante")
        else:
            print("4° cuadrante")