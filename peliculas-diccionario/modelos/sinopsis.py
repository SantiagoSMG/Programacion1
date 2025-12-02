import tkinter as tk
from tkinter import ttk
from modelos.datos import reseñas
from modelos import favoritos   # ← IMPORT CORRECTO

def mostrar_reseña(nombre, parent):
    win = tk.Toplevel(parent)
    win.title(nombre)
    win.geometry("640x420")
    win.configure(bg="#121212")
    win.transient(parent)
    win.grab_set()

    # Título
    lbl = tk.Label(
        win, text=nombre,
        bg="#121212", fg="#FFFFFF",
        font=("Segoe UI", 18, "bold")
    )
    lbl.pack(pady=(12, 6), padx=12, anchor="w")

    # Área de texto con scroll
    frame_text = tk.Frame(win, bg="#121212")
    frame_text.pack(fill="both", expand=True, padx=12, pady=6)

    txt = tk.Text(
        frame_text, wrap="word",
        bg="#1B1B1B", fg="#E6E6E6",
        font=("Segoe UI", 11), relief="flat",
        padx=10, pady=10
    )
    txt.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(frame_text, orient="vertical", command=txt.yview)
    scrollbar.pack(side="right", fill="y")

    txt.config(yscrollcommand=scrollbar.set)

    texto = reseñas.get(nombre, "Reseña no disponible.")
    txt.insert("1.0", texto)
    txt.configure(state="disabled")

    # Footer
    footer = tk.Frame(win, bg="#121212")
    footer.pack(fill="x", pady=8)

    # Botón de favorito
    def toggle():
        favoritos.toggle_favorite(nombre)
        update_star_btn()

    star_btn = ttk.Button(
        footer,
        text="★" if favoritos.is_favorite(nombre) else "☆",
        width=4,
        command=toggle
    )
    star_btn.pack(side="right", padx=12)

    def update_star_btn():
        star_btn.config(text="★" if favoritos.is_favorite(nombre) else "☆")

    # Botón cerrar
    cerrar = ttk.Button(footer, text="Cerrar", command=win.destroy)
    cerrar.pack(side="right", padx=8)

    # Centrar ventana
    parent.update_idletasks()
    x = parent.winfo_x() + (parent.winfo_width() // 2) - 320
    y = parent.winfo_y() + (parent.winfo_height() // 2) - 210
    win.geometry(f"+{x}+{y}")


def crear_botones(genero, frame, catalogo, parent):
    # Limpiar frame
    for w in frame.winfo_children():
        w.destroy()

    titulos = catalogo.get(genero, [])

    if not titulos:
        lbl = tk.Label(
            frame, text="No hay títulos en este género",
            bg="#1B1B1B", fg="#ddd", font=("Segoe UI", 12)
        )
        lbl.pack(pady=10)
        return

    # Canvas + scroll
    canvas = tk.Canvas(frame, bg="#1B1B1B", highlightthickness=0)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg="#1B1B1B")

    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Crear botones de películas
    for title in titulos:
        row = tk.Frame(scroll_frame, bg="#1B1B1B")
        row.pack(fill="x", pady=4, padx=6)

        btn = ttk.Button(
            row, text=title, style="Item.TButton",
            command=lambda t=title: mostrar_reseña(t, parent)
        )
        btn.pack(side="left", padx=(0, 8), fill="x", expand=True)

        star = "★" if favoritos.is_favorite(title) else "☆"

        fav_btn = ttk.Button(
            row, text=star, width=3,
            command=lambda t=title, f=frame, p=parent: _toggle_and_refresh(t, f, p, genero, catalogo)
        )
        fav_btn.pack(side="right", padx=6)


def _toggle_and_refresh(title, frame, parent, genero, catalogo):
    favoritos.toggle_favorite(title)
    crear_botones(genero, frame, catalogo, parent)