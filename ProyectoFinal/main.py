import tkinter as tk
from tkinter import ttk
from modelos.genero import generoPel


catalogo = {                                                                   #Catalogo de peliculas, divididas por generos 
    "acción": ["Mad Max", "John Wick", "Misión Imposible", "Alerta Roja", ""],
    "terror": ["El Conjuro", "It", "Annabelle"],
    "comedia": ["Superbad", "Step Brothers", "Ted", "Proyecto X"],
    "romance": ["Titanic", "The Notebook", "La La Land"]
}

ventana = tk.Tk()                                 
ventana.title("Catálogo de Películas")
ventana.geometry("500x400")

tk.Label(ventana, text="Genero de tu preferencia:").pack()  #Muestra el titulo arriba de donde el usuario va a ingresar el genero

#Crea el espacio donde el usuario va a ingresar el genero
intro_genero = tk.Entry(ventana, width=40)
intro_genero.pack()

#crea el boton donde el usuario va a interactuar para ingresar el genero
boton_enter = tk.Button(ventana, text="Ingresar", background="#b10ee2", foreground="#f2f2f2", command=generoPel)  
boton_enter.pack(pady=5)

#Es donde se muestran las peliculas "SI" el genero introducido existe
lista_peliculas = tk.Listbox(ventana, width=75, height=18)
lista_peliculas.pack()

ventana.mainloop()