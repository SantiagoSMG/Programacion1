import random
print("-🎱Preguntale algo a la bola mágica🎱-")
while True:
    inicio_bolaMágica = input("¿Deseas hacerle una pregunta a la bola mágica? (si/no): ").lower()
    if inicio_bolaMágica != "si":
        print("!Hasta pronto!😁")
        break
    input("⭐¿Qué desea preguntar?⭐ ")
    dado = random.randint(1,20)
    if dado == 1:
        print("Sí")
    elif dado == 2:
        print("No")
    elif dado == 3:
        print("Tal vez")
    elif dado == 4:
        print("Puede ser")
    elif dado == 5:
        print("A lo mejor")
    elif dado == 6:
        print("Parece probable")
    elif dado == 7:
        print("Mejor no decirte ahora")
    elif dado == 8:
        print("Las señales apuntan a que sí")
    elif dado == 9:
        print("Sin lugar a dudas")
    elif dado == 10:
        print("Es decididamente así")
    elif dado == 11:
        print("Es cierto")
    elif dado == 12:
        print("Mis fuentes dicen que no")
    elif dado == 13:
        print("Puedes confiar en ello")
    elif dado == 14:
        print("Al parecer no")
    elif dado == 15:
        print("No se puede predecir ahora")
    elif dado == 16:
        print("Mejor no decirte ahora")
    elif dado == 17:
        print("Perspectiva buena")
    elif dado == 18:
        print("No cuentes con ello")
    elif dado == 19:
        print("Muy dudoso")
    elif dado == 20:
        print("Concéntrate y vuelve a preguntar")