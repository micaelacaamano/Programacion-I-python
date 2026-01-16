"""
Crear una lista de 5 enteros y cargarlos por teclado. 
Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores.

"""
lista=[]

for x in range(5):
    valor=int(input("Ingrese valor: "))
    lista.append(valor)

print("Lista sin modificar: ")
print(lista)

posicion=0
while posicion<len(lista):
    if lista[posicion]>=10:
        lista.pop(posicion)
    else:
        posicion=posicion+1
print("Nueva lista de elementos: ")
for x in range(len(lista)):
    print(lista[x])