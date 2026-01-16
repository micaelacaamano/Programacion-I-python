"""
Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float) Obtener 
el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas.

"""
lista=[]
altas=0
bajas=0
for x in range(5):
    altura=float(input("Ingrese su altura: "))
    lista.append(altura)
promedio=(lista[0]+lista[1]+lista[2]+lista[3]+lista[4])//5
print("Los elementos de la lista son: ", lista)
print("El promedio de la lista es: ", promedio)
for x in range(5):
    if promedio>=lista[x]:
        altas=altas+1
    else:
        bajas=bajas+1
print("Las personas superiores al promedio son: ", altas)
print("Las personas debajo del promedio son: ", bajas)