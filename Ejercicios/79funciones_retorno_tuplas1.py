"""
Confeccionar un programa con las siguientes funciones: 
a) Cargar una lista de 5 enteros. 
b) Retornar el mayor y menor valor de la lista mediante una tupla. 
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.

"""
def cargar():
    lista=[]
    for x in range(5):
        valor=int(input("Ingrese valor: "))
        lista.append(valor)
    return lista

def mayormenor(lista):
    mayor=lista[0]
    menor=lista[0]
    for x in range(1, len(lista)):
        if lista[x]>mayor:
            mayor=lista[x]
        else:
            if lista[x]<menor:
                menor=lista[x]
    return (mayor, menor)


#Bloque principal:

lista=cargar()
mayor, menor= mayormenor(lista)
print("El mayor de los elementos es: ",mayor)
print("El menor de los elementos es: ",menor)
