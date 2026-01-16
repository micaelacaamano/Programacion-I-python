"""
Se tiene que cargar los votos obtenidos por tres candidatos a una elección. 
En una lista cargar en la primer componente el nombre del candidato y en la segunda componente 
cargar una lista con componentes de tipo tupla con el nombre de la provincia y la cantidad de 
votos obtenidos en dicha provincia.

Se deben cargar los datos por teclado, pero si se cargaran por asignación tendría una estructura similar a esta:
candidatos=[("juan", [("cordoba",100),("buenos aires",200)]), ("ana", [("cordoba",55)]), ("luis", [("buenos aires",20)])]

a) Función para cargar todos los candidatos, sus nombres y las provincias con los votos obtenidos. 
b) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas las provincias.

"""
def cargar_candidatos():
    candidatos=[]
    for x in range(3):
        nombre=input("Ingrese nombre del candidato: ")
        cant=int(input("Los votos de cuantas provincias tiene que cargar: "))
        provincias=[]
        for i in range(cant):
            prov=input("Ingrese nombre de la provincia: ")
            votos=int(input("Ingrese cantidad de votos de dicha provincia: "))
            provincias.append((prov, votos))
        candidatos.append((nombre, provincias))
    return candidatos

def totalvotos_candidato(candidatos):
    for x in range(len(candidatos)):
        suma = 0
        for z in range(len(candidatos[x][1])):
            suma += candidatos[x][1][z][1]
        print(candidatos[x][0], "tiene", suma, "votos")


# bloque principal
candidatos = cargar_candidatos()
totalvotos_candidato(candidatos)
