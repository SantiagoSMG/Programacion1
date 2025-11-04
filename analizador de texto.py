
texto = input("Ingresa un texto de tu agrado:\n")
texto = texto.lower()
print("Texto en minusculas:")
print(f"{texto}")
letra = input("ingresa una primera letra: ").lower()
letra1 = input("ingresa una segunda letra: ").lower()
letra2 = input("ingresa una tercera letra: ").lower()
Contador = 0
Contador1 = 0
Contador2 = 0
for letras in texto:
    if letras == letra: 
        Contador += 1
    elif letras == letra1:
        Contador1 += 1
    elif letras == letra2:
        Contador2 += 1
print(f"Esta son las veces que aparece tu primera letra: {Contador}")
print(f"Esta son las veces que aparece tu primera letra: {Contador1}")
print(f"Esta son las veces que aparece tu primera letra: {Contador2}")
print("Estas es la cantidad de palabras que aparece en tu texto:")
lista = texto.split(" ")
lista = len(lista)
print(f"{lista}")

primera_letra = texto[0]
ultima_letra = texto[-1]
print(f"esta es tu primera letra del texto: {primera_letra}")
print(f"esta es la ultima letra del texto: {ultima_letra}")

texto_invertido ="".join(texto)[::-1]
print(texto_invertido)

if "python" in texto:
    print("La palabra 'python' SÍ está en el texto ")
else:
    print("La palabra 'python' NO está en el texto ")
