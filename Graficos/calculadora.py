import tkinter as tk
#1. Creación de la ventana principal
root = tk.Tk()
root.title("Calculadora")
root.geometry("305x500")

#2. Agregar los widgets 
botones_text = ("C","/","*","-",
                "7","8","9","+",
                "4","5","6","",
                "1","2","3","=",
                "0","",".","")

historico = tk.Label(root,bg="#f2f2f2",font="Roboto 14",width=15,bd=0)
historico.pack(pady=5, padx=10, fill="x")

resultado = tk.Entry(root,bg="#ffffff",bd=1,font="Roboto 24",width=15,justify="right")
resultado.pack(padx=10,fill="x")

contenedor_botones = tk.Frame(root,bg="#898787")
contenedor_botones.pack(pady=5,padx=10,fill="both")

acumulador=0
for row in range(5):
    for column in range(4): 
        boton = tk.Button(contenedor_botones
                          ,text=botones_text[acumulador]
                          ,bg="#0DF2EA"
                          ,fg="#ffffff"
                          ,font="Roboto 20"
                          ,bd=0
                          ,width=4)
    if botones_text[acumulador]=="C":
        boton.config(bg="#EE6A6A")
    elif botones_text[acumulador] in ("/","*","-","+"):
        boton.config(bg="#026789")
    
    
    
    
    
    if botones_text[acumulador] != "":
        
        if botones_text[acumulador] != "+":
            boton.config(height=3)
            boton.grid(row=row, column=column,rowspan=2,padx=1,pady=5)
        
        elif botones_text[acumulador] == "=":
            boton.config(height=3)
            boton.grid(row=row, column=column,rowspan=2,padx=1,pady=5, bg="#E78D16")
        
        elif botones_text[acumulador] == "0":
            boton.config(width=8)
            boton.grid(row=row, column=column,rowspan=2,padx=1,pady=5)
             
        else:
            
            boton.grid(row=row, column=column, padx=1, pady=5)
    acumulador+=1

root.mainloop()