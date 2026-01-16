"""
Crear un diccionario en Python que defina como clave el número de documento de una persona y como 
valor un string con su nombre. 
Desarrollar las siguientes funciones: 

a) Cargar por teclado los datos de 4 personas. 
b) Listado completo del diccionario. 
c) Consulta del nombre de una persona ingresando su número de documento.

"""
def cargar():
    listado={}
    for x in range(4):
        nombre=input("ingrese nombre de la persona: ")
        documento=int(input("Ingrese el DNI de la persona: "))
        listado[documento]=nombre
    return listado

def listado_completo(lista):
    print("Listado completo de nombres y sus documentos: ")
    for documento in lista:
        print(documento, lista[documento])

def consulta_persona(lista):
    nro=int(input("Ingrese el documento de la persona que desea consultar: "))
    if nro in lista:
        print("Nombre de la persona: ", lista[nro])
    else:
        print("No existe una persona con ese documento.")


#Bloque principal:

lista=cargar() 
listado_completo(lista)
consulta_persona(lista)