import tkinter as tk
from tkinter import ttk
from modelos.genero import mostrar_genero


catalogo = {                                                                   #Catalogo de peliculas, divididas por generos 
    "acción": ["Mad Max", "John Wick", "Misión Imposible", "Alerta Roja", ""],
    "terror": ["El Conjuro", "It", "Annabelle"],
    "comedia": ["Superbad", "Step Brothers", "Ted", "Proyecto X", "Son como niños", "Son como niños 2"],
    "romance": ["Titanic", "The Notebook", "La La Land"]
}

ventana = tk.Tk()                                 
ventana.title("Catálogo de Películas")
ventana.geometry("500x400")

tk.Label(ventana, text="Genero de tu preferencia:").pack()  #Muestra el titulo arriba de donde el usuario va a ingresar el genero

#crea el boton donde el usuario va a interactuar para ingresar el genero
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=0)

boton_accion = tk.Button(ventana, text="Acción", background="#b10ee2", foreground="#f2f2f2", command=lambda: mostrar_genero("acción",lista_peliculas, catalogo))
boton_terror = tk.Button(ventana, text="Terror", background="#b10ee2", foreground="#f2f2f2", command=lambda: mostrar_genero("terror",lista_peliculas,catalogo))
boton_comedia = tk.Button(ventana, text="Comedia", background="#b10ee2", foreground="#f2f2f2", command=lambda: mostrar_genero("comedia",lista_peliculas,catalogo))
boton_romance = tk.Button(ventana, text="Romance", background="#b10ee2", foreground="#f2f2f2", command=lambda: mostrar_genero("romance", lista_peliculas,catalogo))
boton_romance.pack(side="left",padx=5)
boton_accion.pack(side="left",padx=5)
boton_comedia.pack(side="left",padx=5)
boton_terror.pack(side="left",padx=5)

#Es donde se muestran las peliculas "SI" el genero introducido existe
lista_peliculas = tk.Listbox(ventana, width=75, height=18)
lista_peliculas.pack()

ventana.mainloop()