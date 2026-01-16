""""
Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales. 
Llamar a la función desde el bloque principal del programa 3 veces con string distintos.

"""
def cantidad_vocales(cadena):
    cantidad=0
    for x in range(len(cadena)):
        if cadena[x]=="a" or cadena[x]=="e" or cadena[x]=="i" or cadena[x]=="o" or cadena[x]=="u":
            cantidad=cantidad+1
    print("La cantidad de vocales de la palabra", cadena, "es: ",cantidad)

#Bloque principal:

cantidad_vocales("Hola")
cantidad_vocales("Hola mundo")
cantidad_vocales("instituto Santo Domingo")