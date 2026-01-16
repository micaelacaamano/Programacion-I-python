"""
Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. 
Mostrar el nombre de persona menor en orden alfabético.

"""
lista=[]
for x in range(5):
    nombre=input("Ingrese su nombre: ")
    lista.append(nombre)
menor=lista[0]
for x in range(1, 5):
    if lista[x]<menor:
        menor=lista[x]

print("Lista completa: ",lista)
print("Menor de la lista: ", menor)