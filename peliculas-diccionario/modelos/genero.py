import tkinter as tk
from tkinter import ttk
from modelos.sinopsis import crear_botones
from modelos.datos import catalogo_peliculas, catalogo_series

#Le da fyncionalidad a los botones de los generos
def mostrar_botones_generos(tipo, frame_botones, frame_items, parent):
    catalogo_actual = catalogo_peliculas if tipo == "peliculas" else catalogo_series

    for w in frame_botones.winfo_children():
        w.destroy()
    for w in frame_items.winfo_children():
        w.destroy()

    for genero in catalogo_actual.keys():
        btn = ttk.Button(frame_botones, text=genero.capitalize(), style="Genero.TButton",
                         command=lambda g=genero: crear_botones(g, frame_items, catalogo_actual, parent))
        btn.pack(side="left", padx=6, pady=6)