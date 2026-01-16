"""
En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
a) Carga de los sueldos en una lista.
b) Impresión de todos los sueldos.
c) Cuántos tienen un sueldo superior a $4000.
d) Retornar el promedio de los sueldos.
e) Mostrar todos los sueldos que están por debajo del promedio.

"""
def cargar_sueldos():
    lista=[]
    for x in range(10):
        valor=int(input("Ingrese sueldo: "))
        lista.append(valor)
    return lista

def imprimir_sueldos(lista):
    print("Listado de sueldos:")
    for x in range(len(lista)):
        print(lista[x])

def sueldos_superior(lista):
    cant1=0
    for x in range(len(lista)):
        if lista[x] > 4000:
            cant1 = cant1 + 1
    print("Cantidad de sueldos superiores a 4000:", cant1)

def promedio(sueldos):
    suma=0
    for x in range(len(sueldos)):
        suma = suma + sueldos[x]
    prom = suma / len(sueldos)
    return prom

def sueldos_inferiores(lista):
    pro = promedio(lista)
    print("Promedio de sueldos:", pro)
    print("Sueldos inferiores al promedio:")
    for x in range(len(lista)):
        if lista[x] < pro:
            print(lista[x])

# Bloque principal

sueldos = cargar_sueldos()
imprimir_sueldos(sueldos)
sueldos_superior(sueldos)
sueldos_inferiores(sueldos)
