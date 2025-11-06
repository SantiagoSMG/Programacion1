from colorama import Style,Fore,init
import random

#configuración del juego
COLORES_POSIBLES = {
    "R": Fore.RED+"■",
    "V": Fore.GREEN+"■",
    "N": Fore.BLACK+"■",
    "Y": Fore.YELLOW+"■",
    "M": Fore.MAGENTA+"■",
    "B": Fore.WHITE+"■",
    "C": Fore.CYAN+"■",
    "A": Fore.BLUE+"■"
}
LONGITUD_CODIGO = 4
MAX_INTENTOS = 8
def generar_codigo():
    colores = list(COLORES_POSIBLES.keys())
    codigo_secreto = []
    for _ in range(LONGITUD_CODIGO):
        codigo_secreto.append(random.choice(colores))
    return codigo_secreto

def mostrar_colores_disponibles():
    print("Colores disponibles:")
    for letra,color_formato in COLORES_POSIBLES.items():
        print(f"{letra}: {color_formato} {Style.RESET_ALL}",end ="")

def obtener_intento_usuario():
    while True:
        intento = input("Ingresa tu código de {LONGITUD_CODIGO} letras:\n").upper().strip()
        if len(intento) != LONGITUD_CODIGO:
            print(Fore.RED+f"Error: El código debe tener {LONGITUD_CODIGO} letras")
            continue
        
        valido = True
        for letra in intento:
            if letra not in COLORES_POSIBLES:
                print(Fore.RED+f"Error: La letra '{letra}' no es valor valido. "+Style.RESET_ALL)
            valido = False
            break
        if valido:
            return list(intento)

def evaluar_intento(intento,codigo_secreto):
    #Evalua el intento y devuelve las pistas
    return #posición correcta, color correcto
            
        