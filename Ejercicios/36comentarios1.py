# Programa que solicita al usuario el ingreso de 10 números decimales, los acumula mediante 
# un ciclo repetitivo y muestra por pantalla la suma total de los valores ingresados.

print("Bienvenidos al programa.")

x=0
suma=0
while x<10:
    valor=float(input("Ingrese valor con decimal. Ejemplo: 25.30, 24.36...:"))
    suma=suma+valor
    x=x+1
print("La suma de todos los valores es: ",suma)