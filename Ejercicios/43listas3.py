"""
Definir una lista que almacene por asignación los nombres de 5 personas. 
Contar cuantos de esos nombres tienen 5 o más caracteres.

"""
lista=["luna", "noha", "manuel", "daniela", "julieta"]
suma=0
x=0
while x<len(lista):
    if len(lista[x])>=5:
        suma=suma+1
    x=x+1
print("Los nombres con mas de 5 caracteres son: ", suma )