import tkinter as tk
from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox

#la funcion recorre el catalogo y busca si el genero que ingreso el usuario esta disponible     
#Si esta disponible, se muestra el catalogo de peliculas de ese genero en especifico
#Sino esta disponible, lanza un mensaje de error
def generoPel(intro_genero, catalogo, lista_peliculas):
    genero = intro_genero.get().lower()

    if genero not in catalogo:
        messagebox.showwarning("Error", "Debes escribir un título")
        return
    
    lista_peliculas.delete(0, tk.END)

    for pelicula in catalogo[genero]:
        lista_peliculas.insert(tk.END, pelicula)
        
        #Catalogo de peliculas, divididas por generos
        #Muestra el titulo arriba de donde el usuario va a ingresar el genero
        #Crea el espacio donde el usuario va a ingresar el genero
        #crea el boton donde el usuario va a interactuar para ingresar el genero
        #Es donde se muestran las peliculas "SI" el genero introducido existe