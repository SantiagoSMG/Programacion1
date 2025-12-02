import tkinter as tk
from modelos.datos import catalogo_peliculas, catalogo_series
from modelos.sinopsis import crear_botones
from tkinter import messagebox

def mostrar_genero(genero,lista_peliculas,catalogo):
    # limpiar la lista
    lista_peliculas.delete(0, tk.END)
    
    # verifica si existe el género
    if genero in catalogo:
        # muestra cada pelicula
        for pelicula in catalogo[genero]:
            lista_peliculas.insert(tk.END, pelicula)
    else:
        # si no existe
        messagebox.showwarning("Error", "Ese género no existe")

    

def mostrar_botones_generos(tipo, frame_botones, frame_peliculas):

    # Elegir catálogo según el tipo
    catalogo_actual = catalogo_peliculas if tipo == "peliculas" else catalogo_series

    # Limpiar frame de botones
    for widget in frame_botones.winfo_children():
        widget.destroy()

    # Crear botones para cada género
    for genero in catalogo_actual:
        tk.Button(
            frame_botones,
            text=genero.capitalize(),
            background="#b10ee2",
            foreground="#f2f2f2",
            command=lambda g=genero: crear_botones(g, frame_peliculas, catalogo_actual)
        ).pack(side="left", padx=5)