"""
Se cuenta con la siguiente información:
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.

Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.

"""
manana=0
tarde=0
noche=0
for x in range(5):
    alumno=int(input("Ingrese edad del alumno turno mañana: "))
    manana=manana+alumno
for x in range(6):
    alumno=int(input("Ingrese edad del alumno turno tarde: "))
    tarde=tarde+alumno
for x in range(11):
    alumno=int(input("Ingrese edad del alumno turno noche: "))
    noche=noche+alumno
promañana=manana/5
protarde=tarde/6
pronoche=noche/11
print("El promedio de edad en el turno mañana es: ",promanana)
print("El promedio de edad en el turno tarde es: ",protarde)
print("El promedio de edad en el turno noche es: ",pronoche)
if promañana>protarde and promañana>pronoche:
    print("El turno mañana tiene un promedio mayor")
else:
    if protarde>pronoche:
        print("El turno tarde tiene un promedio mayor")
    else:
        print("El turno noche tiene un promedio mayor")