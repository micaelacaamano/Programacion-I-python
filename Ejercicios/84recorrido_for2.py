"""
Almacenar los nombres de 5 productos y sus precios. 
Utilizar una lista y cada elemento una tupla con el nombre y el precio. 
Desarrollar las funciones: 

a) Cargar por teclado. 
b) Listar los productos y precios. 
c) Imprimir los productos con precios comprendidos entre 10 y 15.

"""
def cargar_listas():
    mercaderia=[]
    for x in range(5):
        producto=input("Ingrese nombre del producto: ")
        valor=int(input("Ingrese precio del producto: "))
        mercaderia.append((producto, valor))
    return mercaderia

def imprimir(mercaderias):
    print("Listado de productos y sus precios: ")
    for producto, valor in mercaderias:
        print(producto,": ", valor)

def precios_entre15y10(mercaderias):
    print("Productos valorados entre 10 y 15: ")
    for producto, valor in mercaderias:
        if valor>=10 and valor<=15:
            print(producto, valor)



#bloque principal:

mercaderias=cargar_listas()
imprimir(mercaderias)
precios_entre15y10(mercaderias)