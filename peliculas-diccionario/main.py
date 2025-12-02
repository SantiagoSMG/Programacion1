import tkinter as tk
from tkinter import ttk
import os

from modelos.datos import catalogo_peliculas, catalogo_series
from modelos.genero import mostrar_botones_generos
from modelos.favoritos import get_all, toggle_favorite, is_favorite, add_favorite, remove_favorite
from modelos.estadisticas import exportar_csv, mostrar_grafica  # ← YA AGREGADO

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
ICON_PATH = os.path.join(ASSETS_DIR, "icon.png")

root = tk.Tk()
root.title("Catálogo de Películas y Series")
root.geometry("1000x650")
root.configure(bg="#0F0F0F")

# icon
try:
    icon_img = tk.PhotoImage(file=ICON_PATH)
    root.iconphoto(True, icon_img)
except Exception:
    pass

style = ttk.Style()
style.theme_use("clam")

style.configure("Sidebar.TFrame", background="#111111")
style.configure("Brand.TLabel", background="#111111", foreground="#FFFFFF", font=("Segoe UI", 18, "bold"))
style.configure("Sidebar.TButton", font=("Segoe UI", 11, "bold"),
                foreground="#FFFFFF", background="#E50914", padding=8, relief="flat")
style.map("Sidebar.TButton", background=[("active", "#B20710")])
style.configure("Genero.TButton", font=("Segoe UI", 10, "bold"),
                foreground="#FFFFFF", background="#6A1BB8", padding=8)
style.map("Genero.TButton", background=[("active", "#8A2DDB")])
style.configure("Item.TButton", font=("Segoe UI", 10),
                foreground="#FFFFFF", background="#13a3c7", padding=6)
style.map("Item.TButton", background=[("active", "#0d7b94")])

container = tk.Frame(root, bg="#0F0F0F")
container.pack(fill="both", expand=True)

sidebar = tk.Frame(container, bg="#111111", width=220)
sidebar.pack(side="left", fill="y")

brand = ttk.Label(sidebar, text="PELÍCULAS", style="Brand.TLabel")
brand.pack(pady=(16, 10), padx=12)

# Área de contenido
main_area = tk.Frame(container, bg="#1B1B1B")
main_area.pack(side="left", fill="both", expand=True)

header = tk.Frame(main_area, bg="#1B1B1B")
header.pack(fill="x", pady=10, padx=12)
title = tk.Label(header, text="Catálogo Multimedia", bg="#1B1B1B",
                 fg="#ffffff", font=("Segoe UI", 22, "bold"))
title.pack(side="left", anchor="w")

# Buscar UI
search_frame = tk.Frame(header, bg="#1B1B1B")
search_frame.pack(side="right")
entry_search = tk.Entry(search_frame, width=28, font=("Segoe UI", 11))
entry_search.pack(side="left", padx=(0, 6))

def on_search():
    q = entry_search.get().strip()
    from modelos.sinopsis import crear_botones_search
    crear_botones_search(q, frame_items)

ttk.Button(search_frame, text="Buscar", command=on_search).pack(side="left")

# Marcos
frame_generos = tk.Frame(main_area, bg="#1B1B1B")
frame_generos.pack(fill="x", padx=12, pady=(6, 12))

frame_items = tk.Frame(main_area, bg="#1B1B1B")
frame_items.pack(fill="both", expand=True, padx=12, pady=6)


# ---------------------------------------------------
# BOTONES DEL SIDEBAR
# ---------------------------------------------------

ttk.Button(
    sidebar,
    text="Películas",
    style="Sidebar.TButton",
    command=lambda: mostrar_botones_generos("peliculas", frame_generos, frame_items, root)
).pack(fill="x", padx=12, pady=6)

ttk.Button(
    sidebar,
    text="Series",
    style="Sidebar.TButton",
    command=lambda: mostrar_botones_generos("series", frame_generos, frame_items, root)
).pack(fill="x", padx=12, pady=6)

# FAVORITOS
def open_favorites_window():
    favs = get_all()
    win = tk.Toplevel(root)
    win.title("Favoritos")
    win.geometry("520x420")
    win.configure(bg="#121212")
    win.transient(root)
    win.grab_set()

    lbl = tk.Label(win, text="Favoritos", bg="#121212", fg="#fff", font=("Segoe UI", 18, "bold"))
    lbl.pack(pady=8, anchor="w", padx=12)

    list_frame = tk.Frame(win, bg="#121212")
    list_frame.pack(fill="both", expand=True, padx=12, pady=8)

    if not favs:
        tk.Label(list_frame, text="No hay favoritos.", bg="#121212",
                 fg="#ccc", font=("Segoe UI", 12)).pack(pady=20)
    else:
        for t in favs:
            row = tk.Frame(list_frame, bg="#121212")
            row.pack(fill="x", pady=4)
            ttk.Button(row, text=t, style="Item.TButton",
                       command=lambda tt=t: __open_review_from_win(tt, win)).pack(side="left", padx=6)
            star = "★" if is_favorite(t) else "☆"
            ttk.Button(row, text=star,
                       command=lambda tt=t, parent=win: _toggle_and_refresh(tt, parent)).pack(side="right", padx=6)

def __open_review_from_win(title, parent):
    from modelos.sinopsis import mostrar_reseña
    mostrar_reseña(title, root)

def _toggle_and_refresh(title, parent):
    toggle_favorite(title)
    parent.destroy()
    open_favorites_window()

ttk.Button(sidebar, text="Favoritos", style="Sidebar.TButton", command=open_favorites_window)\
    .pack(fill="x", padx=12, pady=6)

# ---------------------------------------------------
# NUEVOS BOTONES DE ESTADÍSTICAS (CSV + GRÁFICAS)
# ---------------------------------------------------

ttk.Button(
    sidebar,
    text="Gráfica Películas",
    style="Sidebar.TButton",
    command=lambda: mostrar_grafica("peliculas")
).pack(fill="x", padx=12, pady=6)

ttk.Button(
    sidebar,
    text="Gráfica Series",
    style="Sidebar.TButton",
    command=lambda: mostrar_grafica("series")
).pack(fill="x", padx=12, pady=6)

ttk.Button(
    sidebar,
    text="Exportar CSV",
    style="Sidebar.TButton",
    command=lambda: exportar_csv("peliculas")
).pack(fill="x", padx=12, pady=6)


footer = tk.Label(sidebar, text="v1.2", bg="#111111", fg="#7a7a7a", font=("Segoe UI", 9))
footer.pack(side="bottom", pady=12)


# CONTENIDO INICIAL
msg = tk.Label(frame_items, text="Selecciona Películas o Series en la barra izquierda",
               bg="#1B1B1B", fg="#cfcfcf", font=("Segoe UI", 12))
msg.pack(pady=20)

mostrar_botones_generos("peliculas", frame_generos, frame_items, root)

root.mainloop()