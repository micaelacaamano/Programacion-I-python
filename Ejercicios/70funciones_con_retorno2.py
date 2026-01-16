"""
Elaborar una función que nos retorne el perímetro de un cuadrado pasando como parámetros el valor de un lado.

"""
def retornar_perimetro(lado):
    perimetro=lado*4
    return perimetro       

#Bloque principal:

la=int(input("Ingrese lado del cuadrado: "))
perim=retornar_perimetro(la)
print("El perimetro del cuadrado es: ", perim)