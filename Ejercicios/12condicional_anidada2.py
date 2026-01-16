"""
Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el 
número es positivo, negativo o nulo (es decir cero)

"""
num=int(input("Ingrese su valor: "))
if num>0:
    print("Su valor es positivo")
else:
    if num<0:
        print("Su valor es negativo")
    else:
        print("Su valor es nulo")