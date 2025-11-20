import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ProyectoFinal.main import lista_peliculas, catalogo, intro_genero

def generoPel():                       #la funcion recorre el catalogo y busca si el genero que ingreso el usuario esta disponible
    genero = intro_genero.get().lower()      #Si esta disponible, se muestra el catalogo de peliculas de ese genero en especifico
    if genero in catalogo:                   #Sino esta disponible, lanza un mensaje de error
        print(catalogo[genero])
    else: messagebox.showwarning("Error", "Debes escribir un título")
    lista_peliculas.delete(0, tk.END)
    for pelicula in catalogo[genero]:
        lista_peliculas.insert(tk.END, pelicula)
    return