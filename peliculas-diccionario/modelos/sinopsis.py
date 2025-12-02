from main import reseñas
from tkinter import messagebox
import tkinter as tk

# Función para mostrar las reseñás de las peliculas y series 
def mostrar_reseña(nombre):
    texto = reseñas.get(nombre, "Reseña no disponible.")
    messagebox.showinfo("Reseña", texto)


# Función para crear botones de películas y series según categoría seleccionada
def crear_botones_peliculas(genero, frame, catalogo):
    # Limpia la lista anterior
    for widget in frame.winfo_children():
        widget.destroy()

    lista_items = catalogo[genero]

    for item in lista_items:
        tk.Button(
            frame,
            text=item,
            background="#13a3c7",
            foreground="#FFFEFE",
            width=35,
            command=lambda titulo=item: mostrar_reseña(titulo)
        ).pack(pady=3)