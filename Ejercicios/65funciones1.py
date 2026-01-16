"""
Desarrollar un programa con dos funciones. 
La primer solicite el ingreso de un entero y muestre el cuadrado de dicho valor. 
La segunda que solicite la carga de dos valores y muestre el producto de los mismos. 
LLamar desde el bloque del programa principal a ambas funciones.

"""
def carga_cuadrado():
    valor=int(input("Ingrese valor: "))
    cuadrado=valor*valor
    print("El cuadrado de su valor es: ",cuadrado)
    
def carga_dos_valores():
    valor1=int(input("Ingrese primer valor: "))
    valor2=int(input("Ingrese segundo valor: "))
    producto=valor1*valor2
    print("El producto de sus valores es: ",producto)

#Programa principal
carga_cuadrado()
print("---------------------------------------")
carga_dos_valores()