playlist_musica = ["Bohemian Rhapsody","Hotel California","Stairway to haven"]
print("La playlist de hoy es: ",playlist_musica)
CancionFav = input("Escribe tu canción favorita: ")
playlist_musica.append(CancionFav)
print("Esta es la playlist de la noche: ", playlist_musica)
print("El DJ sugiere eliminar Hotel California y agregar Shape of You")
playlist_musica[1] = "Shape of You"
print("Modificaron la playlist, ahora quedo así: ", playlist_musica)
can2 = "Watermelon Sugar"
playlist_musica.insert(0,can2)
print("Se acabo la fiesta no se podrá reproducir la ultima canción")
playlist_musica.pop()
print("Lamentablemente no se pudo reproducir la ultima canción asi quedo la playlist de la noche: ", playlist_musica)
print("Esta fue la cantidad de canciones que se reproducieron durante la noche: ", len(playlist_musica))