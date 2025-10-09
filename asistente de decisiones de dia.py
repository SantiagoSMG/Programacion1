print("Indique que día de la semana es")
dia = int(input("""
1. Lunes
2. Martes
3. Miercoles
4. Jueves
5. Viernes
6.Sábado
7. Domingo
"""))
Clima = int(input("""
1. Soleado
2. Nublado
3. Lluvioso
"""))
match dia:
    case 1:
        if Clima == 1:{
            print("Es un buen día para trabajar en su casa")
        }
        if Clima == 2:{
            print("Es un buen día para salir a hacer ejercicio")
        }
        if Clima == 3:{
            print("Es un buen día para quedarse en casa y tomar café")
        }
    case 2:
        if Clima == 1:{
            print("Es un buen día para ir a trabajar")
        }
        if Clima == 2:{
            print("Es un buen día para meditar")
        }
        if Clima == 3:{
            print("Es un buen día para leer")
        }
    case 3:
        if Clima == 1:{
            print("Es un buen día para cocinar un postre")
        }    
        if Clima == 2:{
            print("Es un buen día para ir al supermercado")
        }
        if Clima == 3:{
            print("Es un buen día para cocinar un caldo")
        }
    case 4:
        if Clima == 1:{
            print("Es un buen día para jugar futbol")
        }    
        if Clima == 2:{
            print("Es un buen día para escalar un cerro")
        }    
        if Clima == 3:{
            print("Es un buen día para jugar videojuegos")
        }
    case 5:
        if Clima == 1:{
            print("Es un buen día para ir a la playa")
        }                
        if Clima == 2:{
            print("Es un buen día para salir con tus amigos")
        }                
        if Clima == 3:{
            print("Es un buen día para ver peliculas")
        }
    case 6:
        if Clima == 1:{
            print("Es un buen día para quedarse en casa y descansar")
        }                    
        if Clima == 2:{
            print("Es un buen día para jugar basketball")
        }                    
        if Clima == 3:{
            print("Es un buen día para leer comics")
        }                    
    case 7:
        if Clima == 1:{
            print("Es un buen día para ir de picnic")
        }                    
        if Clima == 2:{
            print("Es un buen día para salir de fiesta")
        }                    
        if Clima == 3:{
            print("Es un buen día para programar")
        }                        
        
       