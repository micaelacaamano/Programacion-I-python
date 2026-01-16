"""
Se desea almacenar los datos de 3 alumnos. 
Definir un diccionario cuya clave sea el número de documento del alumno. 
Como valor almacenar una lista con componentes de tipo tupla donde almacenamos nombre de materia y su nota.
Crear las siguientes funciones: 

a) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las materias y sus notas) 
b) Listado de todos los alumnos con sus notas 
c) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas.

"""
def cargar():
    alumnado = {}

    for x in range(3):
        documento = int(input("Ingrese DNI del alumno: "))
        continua = "si"
        lista = []

        while continua == "si":
            materia = input("Ingrese nombre de la materia: ")
            nota = int(input("Ingrese nota de la materia: "))
            lista.append((materia, nota))
            continua = input("¿Desea registrar otras materias [si/no]? ")

        alumnado[documento] = lista

    return alumnado


def listado_completo(alumnado):
    print("Listado completo de alumnos, materias y notas:")
    for documento in alumnado:
        print("Alumno DNI:", documento)
        print("Materias que cursa y sus notas:")
        for materia, nota in alumnado[documento]:
            print(materia, "-", nota)
        print()


def consultar_alumno(alumnado):
    consulta = int(input("Ingrese DNI del alumno a consultar: "))
    if consulta in alumnado:
        print("Materias y notas del alumno:")
        for materia, nota in alumnado[consulta]:
            print(materia, "-", nota)
    else:
        print("Alumno no encontrado")


# Bloque principal
alumnado = cargar()
listado_completo(alumnado)
consultar_alumno(alumnado)
