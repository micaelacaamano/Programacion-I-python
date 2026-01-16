"""
En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente: 
a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas) 
b) Realizar un listado que muestre los nombres, notas y condición del alumno. 
En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está 
entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4. 
c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.

"""
alumno=[]
nota=[]
for x in range(4):
    nom=input("Ingrese nombre del alumno: ")
    alumno.append(nom)
    nota1=int(input("Ingrese nota del alumno: "))
    nota.append(nota1)
print("Listado de los alumnos: ")
cantidad=0
for x in range (4):
    if nota[x]>=8:
        print(alumno[x],",Nota:",nota[x],", ", "Condicion: Muy bueno")
        cantidad=cantidad+1    
    else:
        if nota[x]>=4 and nota[x]<=7:
            print(alumno[x],",Nota:",nota[x],", ", "Condicion: Bueno")
        else:
            print(alumno[x],",Nota:", nota[x],", ", "Condicion: Insuficiente")
print("Alumnos con las mejores condiciones son: ", cantidad)