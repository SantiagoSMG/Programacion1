import modelos.curso as curso
import modelos.alumno as alumno

#edad,carrera y semestre


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
            alumno.agregarAlumno(cursos)
        case 2:
            alumno.darBajaAlumno(cursos)
        case 3:
            curso.agregarCurso(cursos)
        case 4:
           alumno.mostrarAlumnos(cursos)
        case 5:
            curso.mostrarCursos(cursos)
        case 7:
            curso.eliminarCurso(cursos)
        case 6:
            print("Saliendo del programa...")
            break
        case _:
            print("Opción inválida, intenta de nuevo.\n")

