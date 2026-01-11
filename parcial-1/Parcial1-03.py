"""
Descripción: El Programa analiza cadenas ingresadas por el usuario:

- Imprime cada letra de la cadena por separado.
- Muestra la cantidad total de letras.
- Solicita nuevas cadenas de forma indefinida.
- Finaliza cuando el usuario ingresa la palabra clave `salir`.
"""

clave="salir"
cadena=""
while cadena!=clave:
    cadena=input("Ingrese una cadena de caracteres: ")
    if cadena==clave:
        print("saliendo del programa")
    else:
        for x in range(len(cadena)):
            print(cadena[x])
        print("La cantidad de letras es: ", len(cadena))


    