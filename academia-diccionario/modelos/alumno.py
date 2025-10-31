import modelos.curso
from modelos.curso import mostrarCursos
def agregarAlumno(cursos): 
    if len(cursos) == 0:
        print("Primero debes agregar un curso.\n")
        return
    
    mostrarCursos(cursos)
    try:
        idCurso = int(input("Selecciona el ID del curso donde agregarás al alumno: "))
    except:
        print("ID inválido.\n")
        return

    if idCurso < 0 or idCurso >= len(cursos):
        print("Curso no válido.\n")
        return

    nombre = input("Nombre del alumno: ")
    edad = input("Edad del alumno: ")
    carrera = input("Carrera del alumno: ")
    semestre = input("Semestre del alumno: ")

    alumno = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera,
        "semestre": semestre
    }

    cursos[idCurso][3].append(alumno)
    print("Alumno agregado correctamente.\n")


def mostrarAlumnos(cursos):
    if len(cursos) == 0:
        print("No hay cursos registrados.\n")
        return

    mostrarCursos(cursos)
    try:
        idCurso = int(input("Selecciona el ID del curso para ver sus alumnos: "))
    except:
        print("ID inválido.\n")
        return

    if idCurso < 0 or idCurso >= len(cursos):
        print("Curso no válido.\n")
        return

    alumnos = cursos[idCurso][3]

    if len(alumnos) == 0:
        print("No hay alumnos en este curso.\n")
    else:
        print(f"\n----- Alumnos del curso {cursos[idCurso][0]} -----")
        for i, alumno in enumerate(alumnos):
            print(f"ID {i} - Nombre: {alumno['nombre']}, Edad: {alumno['edad']}, Carrera: {alumno['carrera']}, Semestre: {alumno['semestre']}")
        print()


def darBajaAlumno(cursos):
    if len(cursos) == 0:
        print("No hay cursos registrados.\n")
        return

    mostrarCursos(cursos)
    try:
        idCurso = int(input("Selecciona el ID del curso: "))
    except:
        print("ID inválido.\n")
        return

    if idCurso < 0 or idCurso >= len(cursos):
        print("Curso no válido.\n")
        return

    alumnos = cursos[idCurso][3]

    if len(alumnos) == 0:
        print("No hay alumnos en este curso.\n")
        return

    print(f"----- Alumnos del curso {cursos[idCurso][0]} -----")
    for i, alumno in enumerate(alumnos):
        print(f"ID {i} - {alumno['nombre']}")

    try:
        idAlumno = int(input("Escribe el ID del alumno que quieres dar de baja: "))
    except:
        print("ID inválido.\n")
        return

    if idAlumno < 0 or idAlumno >= len(alumnos):
        print("ID de alumno no válido.\n")
        return

    eliminado = alumnos.pop(idAlumno)
    print(f"Se eliminó al alumno: {eliminado['nombre']}\n")
