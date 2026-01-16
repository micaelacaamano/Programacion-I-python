"""
Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. 
Tener en cuenta que un espacio en blanco es igual a " ", en cambio una cadena vacía es ""

"""
oracion=input("Ingrese su oracion: ")
cantidad=0
x=0
while x<len(oracion):
    if oracion[x]==" ":
        cantidad=cantidad+1
    x=x+1
print("Espacios vacios en la oracion: ", cantidad)