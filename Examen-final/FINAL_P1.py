#Cargamos a traves de esta funcion el listado de peliculas que deseamos agregar al diccionario. 

def cargar_diccionario():
    aceptar= "si"
    pelicula={}
    while aceptar=="si": 
        nombre=input("Ingrese nombre de la pelicula: ")
        minutos=int(input("Ingrese duracion de la pelicula: "))
        estreno=int(input("Ingrese año de estreno: "))
        pelicula[nombre]=(minutos, estreno)
        aceptar=input("¿Desea cargar otra pelicula? [si/no]")
    return pelicula

#Esta funcion me permite solicitar el listado completo de peliculas que se haya agregado al diccionario.

def obtener_titulo(diccionario):
    print("Listado de peliculas: ")
    for x in diccionario:
        minutos, estreno = diccionario[x]
        print("Pelicula:", x, "- Duracion:", minutos, "min - Estreno:", estreno)



#Bloque principal:
    
diccionario=cargar_diccionario()

obtener_titulo(diccionario)

