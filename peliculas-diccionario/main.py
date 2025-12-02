import tkinter as tk
from modelos.datos import catalogo_peliculas, catalogo_series
from modelos.genero import mostrar_botones_generos
from modelos.sinopsis import crear_botones

# Crear ventana
ventana = tk.Tk()
ventana.title("Catálogo de Películas y Series")
ventana.geometry("800x600")

# Frames
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

frame_peliculas = tk.Frame(ventana)
frame_peliculas.pack(pady=10)

# Botones principales
boton_peliculas = tk.Button(
    ventana,
    text="Mostrar Películas",
    width=20,
    command=lambda: mostrar_botones_generos("peliculas", frame_botones, frame_peliculas)
)
boton_peliculas.pack(pady=5)

boton_series = tk.Button(
    ventana,
    text="Mostrar Series",
    width=20,
    command=lambda: mostrar_botones_generos("series", frame_botones, frame_peliculas)
)
boton_series.pack(pady=5)

ventana.mainloop()