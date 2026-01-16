"""
Definir una función que cargue una lista con palabras y la retorne. 
Luego otra función tiene que mostrar todas las palabras de la lista que tienen más de 5 caracteres.

"""
def cargar_lista():
    palabras=[]
    cant=int(input("Ingrese cantidad de palabras a cargar en la lista: "))
    for x in range(cant):
        pal=input("Ingrese palabra: ")
        palabras.append(pal)
    return palabras

def mayor_caracteres(palabras):
    print("Palabras con mas de 5 caracteres: ")
    for palabra in palabras:
        if len(palabra)>5:
            print(palabra)

#Bloque principal:
palabras=cargar_lista()
mayor_caracteres(palabras)