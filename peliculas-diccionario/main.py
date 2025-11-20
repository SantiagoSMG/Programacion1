import tkinter as tk
from tkinter import ttk
from modelos.genero import mostrar_genero


catalogo = {                                                                   #Catalogo de peliculas, divididas por generos 
    "acción": ["Mad Max","John Wick","Misión Imposible","Alerta Roja","Gladiador","Avengers: Endgame","Avengers: Infinity War","Batman inicia","Rápidos y furiosos 7",
               "Capitán América: El soldado del invierno","El hombre araña: Sin camino a casa","Terminator 2: El juicio final"],
    "terror": ["El Conjuro", "It", "Annabelle","La monja","La noche del demonio","It: Capítulo 2","Saw","El orfanato","El exorcista","Annabelle 2: La creación",
               "El conjuro 2","Viernes 13","El aro","La masacre de Texas","Un lugar en silencio","REC","Babadook","La noche del demonio 2"],
    "comedia": ["Superbad","Step Brothers","Ted","Proyecto X","Son como niños","Son como niños 2","Ted 2","¿Qué pasó ayer?","Guerra de papás","Jumanji: Bienvenidos a la jungla",
                "Mi pobre angelito","Las vacaciones de Mr. Bean","El dictador","Virgen a los 40","Un espía y medio","Zoolander","Guerra de papás 2","¿Qué pasó ayer? Parte II",
                "Una noche en el museo"],
    "romance": ["Titanic","El diario de una pasión","La La Land","Orgullo y prejuicio","Yo antes de ti","Votos de amor","Cartas a Julieta","Posdata: Te amo",
                "10 cosas que odio de ti","Bajo la misma estrella","A dos metros de ti","500 días con ella","Romeo y Julieta"]
}

ventana = tk.Tk()                                 
ventana.title("Catálogo de Películas")
ventana.geometry("500x400")

#Es el titulo o encabezado que esta arriba de los botones
tk.Label(ventana, text="Selecciona un género de tu preferencia:").pack(pady=5, anchor="n")

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=5, anchor="n")   #Esto los pone arriba de la interfaz, para que queden mejor visualmente

#Estos son los botones que se ven en la interfaz
boton_accion = tk.Button(frame_botones, text="Acción", background="#b10ee2", foreground="#f2f2f2",command=lambda: mostrar_genero("acción", lista_peliculas, catalogo))
boton_terror = tk.Button(frame_botones, text="Terror", background="#b10ee2", foreground="#f2f2f2",command=lambda: mostrar_genero("terror", lista_peliculas, catalogo))
boton_comedia = tk.Button(frame_botones, text="Comedia", background="#b10ee2", foreground="#f2f2f2",command=lambda: mostrar_genero("comedia", lista_peliculas, catalogo))
boton_romance = tk.Button(frame_botones, text="Romance", background="#b10ee2", foreground="#f2f2f2",command=lambda: mostrar_genero("romance", lista_peliculas, catalogo))

boton_accion.pack(side="left", padx=5)
boton_terror.pack(side="left", padx=5)
boton_comedia.pack(side="left", padx=5)
boton_romance.pack(side="left", padx=5)

#Aqui es donde se muestran las listas de peliculas
lista_peliculas = tk.Listbox(ventana, width=75, height=18)
lista_peliculas.pack(pady=20)


ventana.mainloop()