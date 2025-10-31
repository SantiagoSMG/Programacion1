while True:
     print("""
    1.- Comprar un juego
    2.- Devolver un juego
    4.- Ver eslogan
    3.- Salir
    """)
     break
op = input("Selecciona una opción: ")

info_tienda = {
    'eslogan': 'Game On!',
    'Año de fundación': 2010 
}
print(info_tienda)
print("Este es el catalogo de juegos")
inv_juegos = {
    "Spiderman 2": {"precio":999,"stock":20},
    "Minecraft": {"precio":799, "stock":22},
    "pac-man": {"precio":50, "stock":25}
}
print(inv_juegos)