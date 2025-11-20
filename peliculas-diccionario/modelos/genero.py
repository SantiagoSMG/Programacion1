import tkinter as tk
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

    






