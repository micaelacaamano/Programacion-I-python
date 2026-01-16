# Realizar la carga de dos nombres de personas distintos. 
# Mostrar por pantalla luego ordenados en forma alfabética.

nom1=input("Ingrese el nombre de la primer persona: ")
nom2=input("Ingrese el nombre de la segunda persona: ")
print("Listado alfabetico:")
if nom1<nom2:
    print(nom1)
    print(nom2)
else:
    print(nom2)
    print(nom1)

