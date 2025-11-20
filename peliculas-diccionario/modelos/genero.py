import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
#la funcion recorre el catalogo y busca si el genero que ingreso el usuario esta disponible
#Si esta disponible, se muestra el catalogo de peliculas de ese genero en especifico


def generoPel(intro_genero, catalogo, lista_peliculas):
    genero = intro_genero.get().lower()

    if genero not in catalogo:
        messagebox.showwarning("Error", "Debes escribir un género")
        return
    
    lista_peliculas.delete(0, tk.END)

    for pelicula in catalogo[genero]:
        lista_peliculas.insert(tk.END, pelicula)
