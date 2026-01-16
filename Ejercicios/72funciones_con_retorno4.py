"""
Plantear una función que reciba un string en mayúsculas o minúsculas y retorne la cantidad de letras 'a' o 'A'.

"""
def retornar_a(cadena):
    contador=0
    for x in range(len(cadena)):
        if cadena[x]=="a" or cadena[x]=="A":
            contador=contador+1
    return contador

#Bloque principal
string=input("Ingrese texto: ")
print("La cantidad de letras A en su texto es de: ",retornar_a(string))