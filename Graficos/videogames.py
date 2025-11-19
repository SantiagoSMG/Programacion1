import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Fuente 1: Ventas internas
sales_data = {
    "GameID": ["G1","G2","G3","G4","G5","G6"],
    "Title": ["Cyber-Punk 2077","Spiderman 2","Minecraft","Raft","Sons of the forest","Project Zomboid"],
    "Genere": ["Simulation","RPG","Aventure","Mundo abierto","Shooter","Survival"],
    "Publisher": ["Rockstar","Bethesda","Sony","Ubisoft","Activision","Epic games"],
    "Unit_sold_Millions": [15.5,20.1,8.0,12.3,18.2,19.6]
}

sales_df = pd.DataFrame(sales_data)

#Fuente 2: Reseñas de críticos (externo)
reviews_data = {
    "GameId": ["G1","G2","G3","G4","G5","G7"], #Nota. G6 falta, G7 sobra
    "Critic_Score": [7.5,9.5,8.8,9.7,6.1,8.0], #Puntuación de 0 a 10
    "User_Score": [5.1,9.1,8.5,9.2,np.nan,7.5] #Un NaN! Alguien olvido puntuar Sons of the forest
}
reviews_df = pd.DataFrame(reviews_data)

print("--- Datos de Ventas (crudos) ---")
print(sales_df)
print("--- Datos de Reseñas (crudos) ---")
print(reviews_df)

#Limpieza de datos y preparación
#Desición: Rellenaremos el User_Score que falta con el promedio (Sons of the forest)
mean_user_score = reviews_df["User_Score"].mean()#Promedio de calificaciones de usuario
reviews_df["User_Score"] = reviews_df["User_Score"].fillna(mean_user_score)

print(f"\n--- Reseñas (Limpias, NaN rellenado con {mean_user_score})---")
print(reviews_df)

#Fusion de tablas (merge)
#Fusionar tabla de ventas con reseñas, GameID como llave
#INNER JOIN. Nos quedamos con los juegos que existen en ambas tablas
#G6 va a desaparecer, G7 desaparecer
df = pd.merge(sales_df,reviews_df, on = "GameId", how = "inner")
print("\n--- Tabla fusionada de ventas + reseñas ---")
print(df)

#Crear nuevas columnas que nos den más información
#Columna Estimación de ingresos (asuminedo que valen $50 cada juego)
df["Revenue_Estimate_Billions"] = (df["Revenue_Estimate_Billions"]*50)/1000

#Columna Brecha que hay entre reseñas críticos y la de los usuarios
df["Score_Gap"] = df["Critic_Score"]-df["User_Score"]

#Columna Estandar puntuación de los criticos (a 100)
df["Critic_Score_100"] = df["Critic_Score"] * 10

print("\n--- Tabla transformada (Con nuevas columnas)")
print(df)