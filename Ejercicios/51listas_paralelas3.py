"""
Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada una. 
Generar una tercer lista que surja de la suma de los elementos de la misma posición de cada lista. 
Mostrar esta tercer lista.

"""
lista1=[]
lista2=[]
for x in range(4):
    valor1=int(input("Ingrese primer valor: "))
    lista1.append(valor1)
    valor2=int(input("Ingrese segundo valor: "))
    lista2.append(valor2)
lista3=[]
for x in range(4):
    suma=lista1[x]+lista2[x]
    lista3.append(suma)

print("Tercera lista: ", lista3)