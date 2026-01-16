"""
Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje indicando 
si el número tiene uno o dos dígitos. (Tener en cuenta que condición debe cumplirse para tener dos 
dígitos un número entero)

"""

valor=int(input("Ingrese su valor: "))
if valor<10:
    print("Este valor tiene un digito")
else:
    print("Este valor tiene dos digitos.")