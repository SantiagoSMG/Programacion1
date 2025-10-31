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