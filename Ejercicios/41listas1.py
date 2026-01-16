"""
Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos 
valores almacenan un valor superior a 100.

"""
lista=[102, 150, 50, 60, 14, 650, 798, 30]
suma=0
x=0
while x<len(lista):
    if lista[x]>=100:
        suma=suma+1
    x=x+1
print("La lista esta constituida por los elementos: ", lista)    
print("Los valores superiores a 100 son: ", suma)