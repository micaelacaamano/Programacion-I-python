"""
Realizar la carga del precio de un producto y la cantidad a llevar. Mostrar cuanto
 se debe pagar (se ingresa un valor entero en el precio del producto)

"""

producto=int(input("Ingrese el valor del producto: "))
cantidad=int(input("Ingrese la cantidad a llevar: "))
total=producto*cantidad
print("El total que se debe abonar es de: ", total)