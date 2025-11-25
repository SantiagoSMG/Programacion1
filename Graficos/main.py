import tkinter as tk
from tkinter import font
from Graficos.config import TITULO,COLOR_BARRA_SUPERIOR,COLOR_MENU_LATERAL,COLOR_PANEL_PRINCIPAL
from Utiles.util_ventana import centrar_ventana

root = tk.Tk()
root.title(TITULO)
#Geometry
centrar_ventana(root,1024,600)



root.mainloop()