import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

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


def crear_botones_peliculas(genero, frame_peliculas, catalogo):


    # Verifica si existe el género
    if genero in catalogo:
        
        # Limpia el frame de películas y series
        for widget in frame_peliculas.winfo_children():
            widget.destroy()
            #winfo_children() sirve para obtener todos los widgets hijos de un frame, es decir, todos los botones de peliculas o series que se han creado anteriormente
            
        # Crear botones para cada película/serie
        for pelicula in catalogo[genero]:
            tk.Button(
                frame_peliculas, 
                text=pelicula,
                background="#ffffff",
                foreground="#000000",
                width=25,
                height=2,
                wraplength=150,
                command=lambda p=pelicula: messagebox.showinfo("Información", f"Seleccionaste: {p}")
            ).pack(pady=5, padx=5)
    else:
        # Si no existe el género
        messagebox.showwarning("Error", "Ese género no existe")
    






