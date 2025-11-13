import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Fuente 1: Ventas internas
sales_data = {
    "GameID": ["G1","G2","G3","G4","G5","G6",],
    "Title": ["Cyber-Punk 2077","Spiderman 2","Minecraft","Raft","Sons of the forest","Project Zomboid"],
    "Genere": ["Simulation","RPG","Aventure","Mundo abierto"],
    "Publisher": ["Rockstar","Bethesda","Sony",],
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

print("--- Datos de Ventas ---")
print(sales_df)
print("--- Datos de Reseñas ---")
print(reviews_df)