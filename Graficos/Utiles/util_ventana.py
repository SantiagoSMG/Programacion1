#Crear una funcion para centrar la ventana

def centrar_ventana(ventana,ancho,alto):
    pantalla_ancho= ventana.winfo_screenwidth()
    pantalla_alto= ventana.winfo_screenheight()
    x = int((pantalla_ancho/2)- (ancho/2))#Determina el centro de la pantalla horizontal
    y = int((pantalla_alto/2)- (alto/2))#Dtermina el centro de la pantalla vertical
    return ventana.geometry(f"{ancho}x{alto}+{x}+{y}")#WxH+X+Y
