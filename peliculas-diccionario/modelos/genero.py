import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
#la funcion recorre el catalogo y busca si el genero que ingreso el usuario esta disponible
#Si esta disponible, se muestra el catalogo de peliculas de ese genero en especifico


def mostrar_genero(genero,lista_peliculas,catalogo):
    # limpiar la lista
    lista_peliculas.delete(0, tk.END)
    
    # verificar si existe el género
    if genero in catalogo:
        # mostrar cada película
        for pelicula in catalogo[genero]:
            lista_peliculas.insert(tk.END, pelicula)
    else:
        # si no existe
        messagebox.showwarning("Error", "Ese género no existe")

    






