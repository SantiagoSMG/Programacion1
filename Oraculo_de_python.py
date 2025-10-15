from datetime import datetime  
def calcular_elemento(año):
    ultimo_digito = año % 10
    if ultimo_digito in [0, 1]:
        return "Metal"
    elif ultimo_digito in [2, 3]:
        return "Agua"
    elif ultimo_digito in [4, 5]:
        return "Madera"
    elif ultimo_digito in [6, 7]:
        return "Fuego"
    else:
        return "Tierra"
def prediccion(nombre, elemento, numeroSuerte):
    match numeroSuerte:
        case 1:
            return f"{nombre}, tu conexión con el elemento {elemento} te traerá gran sabiduría. ¡Es un buen momento para aprender algo nuevo!"
        case 2:
            return f"Veo que el elemento {elemento} guía tu camino, {nombre}. La fortuna sonríe a los valientes, ¡atrévete a tomar ese riesgo que tienes en mente!"
        case 3:
            return f"{nombre}, el poder del {elemento} te rodea. Hoy es un día ideal para dejar atrás lo viejo y comenzar de nuevo."
        case 4:
            return f"El elemento {elemento} te impulsa, {nombre}. ¡La energía positiva fluirá hacia ti si actúas con confianza!"
        case _:
            return "Número de la suerte inválido."
def iniciar_oraculo():
    while True:
        inicio_oraculo = input("¿Deseas conocer tu destino? (si/no): ").lower()
        if inicio_oraculo != "si":
            print("🔮 El Oráculo se despide. ¡Hasta la próxima!")
            break
        
        nombre = input("Ingresa tu nombre: ")
        año = int(input("Ingresa tu año de nacimiento: "))
        numero = int(input("Elige tu número de la suerte (1-4): "))
        año_actual = datetime.now().year
        edad = año_actual - año
        elemento = calcular_elemento(año)
        mensaje = prediccion(nombre, elemento, numero)
        print("\n" + "*" * 60)
        print(f"✨ Hola {nombre}, tienes {edad} años ✨")
        print(mensaje)
        print("*" * 60 + "\n")
iniciar_oraculo()
