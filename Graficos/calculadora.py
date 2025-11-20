import tkinter as tk
#1. Creación de la ventana principal
root = tk.Tk()
root.title("Calculadora")
root.geometry("300x500")

#2. Agregar los widgets 
botones_text = ("C","/","*","-",
                "7","8","9","+",
                "4","5","6",
                "1","2","3","=",
                "0",".")

historico = tk.Label(root,bg="#f2f2f2",font="Roboto 14",width=15,bd=0)
historico.pack(pady=5, padx=10, fill="x")

resultado = tk.Entry(root,bg="#ffffff",bd=1,font="Roboto 24",width=15,justify="right")
resultado.pack(padx=10,fill="x")

contenedor_botones = tk.Frame(root,bg="#898787")
contenedor_botones.pack(pady=5,padx=10,fill="both")
root.mainloop()