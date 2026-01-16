"""
Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos y sus precios.
Definir las siguientes funciones:
a) Cargar los nombres de articulos y sus precios.
b) Imprimir los nombres y precios.
c) Imprimir el nombre de artículo con un precio mayor
d) Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor igual al valor ingresado.

"""
def definiendo():
    nombre=[]
    precios=[]
    for x in range(5):
        nom=input("Ingrese nombre del producto: ")
        nombre.append(nom)
        prec=int(input("Ingrese valor del producto: "))
        precios.append(prec)
    return [nombre, precios]

def imprimir_articulos(nombre, precios):
    print("Listado de los productos y sus precios: ")
    for x in range(5):
        print(nombre[x],": ",precios[x])

def mayor_articulo(nombre, precios):
    mayor=precios[0]
    pos=0
    for x in range(1, len(precios)):
        if precios[x]>mayor:
            mayor=precios[x]
            pos=x

    print("El articulo con mayor precio es: ",nombre[pos]," su precio es: ", mayor)

def importe(nombre, precios):
    imp=int(input("Ingrese valor a consultar: "))
    print("Articulos sugeridos: ")
    for x in range(len(precios)):
        if precios[x]<=imp:
            print(nombre[x],": ", precios[x])


#Bloque principal.
nombre, precios=definiendo() 
imprimir_articulos(nombre, precios)
mayor_articulo(nombre, precios)
importe(nombre, precios)