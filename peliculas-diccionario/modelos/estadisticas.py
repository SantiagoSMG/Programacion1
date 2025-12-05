import matplotlib.pyplot as plt
import pandas as pd
import os

from modelos.datos import catalogo_peliculas, catalogo_series
from modelos.favoritos import get_all

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "estadisticas_favoritos.csv")


# ---------------------------------------------------
# CALCULAR FAVORITOS POR GÉNERO
# ---------------------------------------------------
def calcular_favoritos_por_genero(tipo="peliculas"):
    """
    Regresa un diccionario con el número de favoritos por género.
    Ej: {"acción": 3, "terror": 1}
    """
    catalogo = catalogo_peliculas if tipo == "peliculas" else catalogo_series
    favoritos = get_all()  # lista de favoritos

    conteo = {genero: 0 for genero in catalogo.keys()}

    for genero, lista_titulos in catalogo.items():
        for titulo in lista_titulos:
            if titulo in favoritos:
                conteo[genero] += 1

    return conteo


# ---------------------------------------------------
# EXPORTAR CSV
# ---------------------------------------------------
def exportar_csv(tipo="peliculas"):
    """
    Crea o actualiza un archivo CSV con los favoritos por género.
    """
    conteo = calcular_favoritos_por_genero(tipo)

    df = pd.DataFrame(list(conteo.items()), columns=["Género", "Favoritos"])

    df.to_csv(CSV_PATH, index=False, encoding="utf-8")

    print(f"CSV generado en: {CSV_PATH}")
    return CSV_PATH


# ---------------------------------------------------
# MOSTRAR GRÁFICA
# ---------------------------------------------------
def mostrar_grafica(tipo="peliculas"):
    """
    Muestra una gráfica de barras con los favoritos por género.
    """
    conteo = calcular_favoritos_por_genero(tipo)

    generos = list(conteo.keys())
    valores = list(conteo.values())

    plt.figure(figsize=(8, 4))
    plt.bar(generos, valores)
    plt.title("Favoritos por Género")
    plt.xlabel("Género")
    plt.ylabel("Cantidad de Favoritos")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()