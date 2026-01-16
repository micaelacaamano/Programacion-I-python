"""
Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. 
Contar la cantidad de vocales. Crear un segundo string con toda la oración en minúsculas 
para que sea más fácil disponer la condición que verifica que es una vocal.

"""
oracion=input("Ingrese su oracion: ")
oracion1=oracion.lower()
cantidad=0
x=0
while x<len(oracion1):
    if oracion1[x]=="a" or oracion1[x]=="e" or oracion1[x]=="i" or oracion1[x]=="o" or oracion1[x]=="u":
        cantidad=cantidad+1
    x=x+1
print("Cantidad de vocales en su oracion: ", cantidad)