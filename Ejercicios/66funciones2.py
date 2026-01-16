"""
Desarrollar un programa que solicite la carga de tres valores y muestre el menor. 
Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)

""" 
def carga_valores():
    x=0
    valor1=int(input("Ingrese primer valor: "))
    valor2=int(input("Ingrese segundo valor: "))
    valor3=int(input("Ingrese tercer valor: "))
    if valor1<valor2 and valor1<valor3:
        print("El valor menor es: ", valor1)
    else:
        if valor2<valor1 and valor2<valor3:
            print("El valor menor es: ", valor2)
        else:
            print("El valor menor es: ", valor3)

#Programa principal:
carga_valores()
carga_valores()