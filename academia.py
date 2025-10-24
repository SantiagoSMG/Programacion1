def agregarCurso(cursos):
    nombre = input("Nombre del curso: ")
    instructor = input("Nombre del instructor: ")
    aula = input("Aula: ")
    cursos.append([nombre, instructor, aula, []])
    print("Curso agregado correctamente.\n")

def mostrarCursos(cursos):
    if len(cursos) == 0:
        print("No hay cursos registrados.\n")
    else:
        print("----- Cursos registrados -----")
        for i in range(len(cursos)):
            curso = cursos[i]
            print(f"ID {i} - {curso[0]} | Instructor: {curso[1]} | Aula: {curso[2]} | Alumnos: {len(curso[3])}")
        print()

def agregarAlumno(cursos):
    if len(cursos) == 0:
        print("Primero debes agregar un curso.\n")
        return
    mostrarCursos(cursos)
    try:
        idCurso = int(input("Selecciona el ID del curso donde agregarás el alumno: "))
    except:
        print("ID inválido.\n")
        return
    if idCurso < 0 or idCurso >= len(cursos):
        print("Curso no válido.\n")
        return
    nombre_alumno = input("Nombre del alumno: ")
    cursos[idCurso][3].append(nombre_alumno)
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
        print(f"----- Alumnos del curso {cursos[idCurso][0]} -----")
        for i in range(len(alumnos)):
            print(f"ID {i} - {alumnos[i]}")
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
    for i in range(len(alumnos)):
        print(f"ID {i} - {alumnos[i]}")
    try:
        idAlumno = int(input("Escribe el ID del alumno que quieres dar de baja: "))
    except:
        print("ID inválido.\n")
        return
    if idAlumno < 0 or idAlumno >= len(alumnos):
        print("ID de alumno no válido.\n")
        return
    eliminado = alumnos.pop(idAlumno)
    print(f"Se eliminó al alumno: {eliminado}\n")

def eliminarCurso(cursos):
    if len(cursos) == 0:
        print("No hay cursos para eliminar.\n")
        return
    mostrarCursos(cursos)
    try:
        idCurso = int(input("Selecciona el ID del curso que quieres eliminar: "))
    except:
        print("ID inválido.\n")
        return
    if idCurso < 0 or idCurso >= len(cursos):
        print("Curso no válido.\n")
        return
    eliminado = cursos.pop(idCurso)
    print(f"Se eliminó el curso: {eliminado[0]}\n")

cursos = []

while True:
    print("""
    1.- Agregar Alumno
    2.- Dar de baja un Alumno
    3.- Agregar Curso
    4.- Mostrar lista de Alumnos (por curso)
    5.- Mostrar Cursos
    7.- Eliminar Curso
    6.- Salir
    """)
    opcion = input("Selecciona una opción: ")

    try:
        opcion_int = int(opcion)
    except:
        print("Por favor ingresa un número válido.\n")
        continue

    match opcion_int:
        case 1:
            agregarAlumno(cursos)
        case 2:
            darBajaAlumno(cursos)
        case 3:
            agregarCurso(cursos)
        case 4:
            mostrarAlumnos(cursos)
        case 5:
            mostrarCursos(cursos)
        case 7:
            eliminarCurso(cursos)
        case 6:
            print("Saliendo del programa...")
            break
        case _:
            print("Opción inválida, intenta de nuevo.\n")