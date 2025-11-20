import tkinter as tk
from tkinter import ttk
from modelos.genero import generoPel   # Ahora sí funciona

catalogo = {
    "acción": ["Mad Max", "John Wick", "Misión Imposible", "Alerta Roja"],
    "terror": ["El Conjuro", "It", "Annabelle"],
    "comedia": ["Superbad", "Step Brothers", "Ted", "Proyecto X"],
    "romance": ["Titanic", "The Notebook", "La La Land"]
}

ventana = tk.Tk()
ventana.title("Catálogo de Películas")
ventana.geometry("500x400")

tk.Label(ventana, text="Genero de tu preferencia:").pack()

intro_genero = tk.Entry(ventana, width=40)
intro_genero.pack()

lista_peliculas = tk.Listbox(ventana, width=75, height=18)
lista_peliculas.pack()

boton_enter = tk.Button(
    ventana, 
    text="Ingresar", 
    background="#b10ee2", 
    foreground="#f2f2f2", 
    command=lambda: generoPel(intro_genero, catalogo, lista_peliculas)
)
boton_enter.pack(pady=5)

ventana.mainloop()
