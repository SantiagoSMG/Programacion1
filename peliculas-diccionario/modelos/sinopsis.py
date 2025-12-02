import tkinter as tk
from tkinter import messagebox
from modelos.datos import reseñas

# Mostrar reseña de película o serie
def mostrar_reseña(nombre):
    texto = reseñas.get(nombre, "Reseña no disponible.")
    messagebox.showinfo("Reseña", texto)

# Crear botones de películas/series según género
def crear_botones(genero, frame, catalogo):
    # Limpiar lista anterior
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