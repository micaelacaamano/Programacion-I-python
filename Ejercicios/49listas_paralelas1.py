"""
Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. 
Definir dos listas paralelas. Mostrar cuantos productos tienen un precio mayor al primer producto ingresado.

"""
producto=[]
precio=[]
for x in range(5):
    prod=input("Ingrese nombre del producto: ")
    producto.append(prod)
    prec=int(input("Ingrese precio del producto: "))
    precio.append(prec)

mayor=precio[0]
cantidad=0
for x in range(1, 5):
    if mayor<precio[x]:
        cantidad=cantidad+1

print("Los productos con mayor precio al primero son: ", cantidad)