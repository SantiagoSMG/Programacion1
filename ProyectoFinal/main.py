import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def generoPel():
    genero = intro_genero.get().lower()
    if genero in catalogo:
        print(catalogo[genero])
    else: messagebox.showwarning("Error", "Debes escribir un título")
    lista_peliculas.delete(0, tk.END)
    for pelicula in catalogo[genero]:
        lista_peliculas.insert(tk.END, pelicula)
    return


catalogo = {
    "acción": ["Mad Max", "John Wick", "Misión Imposible", "Alerta Roja", ""],
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
boton_enter = tk.Button(ventana, text="Ingresar", background="#b10ee2", foreground="#f2f2f2", command=generoPel)
boton_enter.pack(pady=5)

lista_peliculas = tk.Listbox(ventana, width=75, height=18)
lista_peliculas.pack()

ventana.mainloop()