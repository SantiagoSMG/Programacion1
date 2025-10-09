#if else elif
edad = 25 #int(input("dime tu edad"))

if edad >= 10 and edad < 18:
    print("Eres un adolescente")
elif edad >= 18:
    print("Eres un adulto")
else:
    print("Todavía eres un niño")
    
    
#match
    
opcion = int(input("""
1. Agregar
2. Editar
3. Eliminar
4. Resgistrar
5. Finalizar
"""))

match opcion:
    case 1:
        print("Se ha agregado correctamente.")
    case 2:
        print("Se ha modificado correctamente.")
    case 3:
        print("Se ha eliminado correctamente.")
    case 4:
        print("El usuario registrado se llama Jorge.")
    case 5:
        print("Se finalizará el programa.") 