"""
Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. Al 
comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.

"""
cuadrante1=0
cuadrante2=0
cuadrante3=0
cuadrante4=0
puntos=int(input("Ingresa puntos a procesar: "))
for t in range(puntos):
    x=int(input("Ingresar coordenadas X: "))
    y=int(input("Ingresar coordenadas Y: "))
    if x>0 and y>0:
        cuadrante1=cuadrante1+1
    else:
        if x<0 and y>0:
            cuadrante2=cuadrante2+1
        else:
            if x<0 and y<0:
                cuadrante3=cuadrante3+1
            else:
                if x>0 and y<0:
                    cuadrante4=cuadrante4+1
print("Se han ingresado al cuadrante 1: ",cuadrante1, "puntos")
print("Se han ingresado al cuadrante 2: ",cuadrante2, "puntos")
print("Se han ingresado al cuadrante 3 ",cuadrante3, "puntos")
print("Se han ingresado al cuadrante 4: ",cuadrante4, "puntos")
