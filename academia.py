#Listado cursos (agregar,modificar,eliminar)
#Se desea saber nombre, instructor, aula  y listado de alumnos 
#Se desea saber cuantos estan inscritos por curso
#Modificar instructor, aula, dar de alta alumnos y de baja alumnos
#Mostrar listado de alumnos de un curso
#Interfaz atractiva y solo salir cuando se indique
while True:
    inicio_academia = input("¿Deseas agregar otro curso? (si/no): ").lower()
    if inicio_academia != "si":
        print("Hasta pronto, aqui esta la lista ya terminada: ",cursos)
        break
cursos = ["Nombre","Instructor","Aula","Lista"]
curso = []
nombre = input("Ingrese el nombre del curso: ")
instructor = input("Ingrese el nombre del instructor: ")
aula = int(input("Ingrese el número del aula: "))
ListadoAlumnos = input("Ingrese la lista de alumnos: ")
curso.append(nombre)
curso.append(instructor)
curso.append(aula)
curso.append(ListadoAlumnos)
print("Este es el listado del curso:", curso)
