import random
palabras = ("salir", "tener", "tocar", "golpe", "deseo", "arbol", "abeto", "calle", "casas", "adobe")
while True:
    palabra = palabras[random.randint(0,len(palabras)-1)]
    wordle = list(palabra)
    print("""\033[1;37;44m
====================================[WORDLE]======================================
   Bienvenido ya he elegido la palabra secreta. Tienes 5 intentos para adivinarla.
==================================================================================
\033[0;30;47m""")
    
    for i in range(5):
        intento = input("ingrese una palabra de 5 letras sin acentos.").lower()[:5]
        indice = 0
        resultado = ""
        correctas = 0
        for letra in intento:
            if letra == wordle[indice]:
                correctas += 1
                resultado += "\033[1;32m"+letra+"\033[0,30m"
            elif letra in wordle:
                resultado += "\033[1;33m"+letra+"\033[0;30m"
            else:
                resultado += "\033[1;31m"+letra+"\033[0;30m"
            indice+=1
        if correctas == 5:
         break
        print(resultado)
    if correctas == 5:
            print(f"Felicidades la palabra era \033[1;32m{palabra}\033[0;30m has acertado.")
    else:
            print(f"Lo siento has fallado. La palabra era: \033[1;31m{palabra}\033[0;30m")
    opcion = input("Deseas jugar otra ronda? (si/no)").lower()
    if opcion == "no":
        print("Hasta luego!! Gracias por jugar😁")
    break
