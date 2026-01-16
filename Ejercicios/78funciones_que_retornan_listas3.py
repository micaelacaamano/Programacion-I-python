"""
Confeccionar un programa que permita:
a) Cargar una lista de 10 elementos enteros.
b) Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
c) Imprimir las dos listas generadas.

"""
def cargar_listas():
    lista=[]
    for x in range(10):
        valor=int(input("Ingrese valor positivo o negativo: "))
        lista.append(valor)
    return lista

def generar_listas(lista):
    positiva=[]
    negativa=[]
    for x in range(len(lista)):
        if lista[x] > 0:
            positiva.append(lista[x])
        else:
            if lista[x] < 0:
                negativa.append(lista[x])
    return positiva, negativa

def imprimir_listas(positiva, negativa): 
    print("Lista de valores positivos:")
    for x in range(len(positiva)):
        print(positiva[x])

    print("Lista de valores negativos:")
    for x in range(len(negativa)):
        print(negativa[x])

# Bloque principal: 

lista = cargar_listas()
positiva, negativa = generar_listas(lista)
imprimir_listas(positiva, negativa)
