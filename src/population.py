import numpy as np
import pandas as pd

from character import Character 
from stats import random_stats

def generate_init(N, maxStatsValue,type):
    
    equipment_data = random_stats(N, maxStatsValue)

    # Asignar valores aleatorios de la lista proporcionada a 'height'
    height_values = [1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
    #height_values = range(130,201)
    equipment_data['height'] = np.random.choice(height_values, size=N)
    # Asignar valores aleatorios de la lista proporcionada a 'type'
    #equipment_data['type'] = np.random.choice(list(CharacterType), size=N)
    equipment_data['type'] = type
    # Agregar objetos de la clase Personaje y calcular el desempeño
    personajes = []
    for index, row in equipment_data.iterrows():
        personaje = Character(row['type'],row['height'],row['strength'],row['agility'],row['expertise'],row['resistance'],row['life'])
        personajes.append(personaje)
    equipment_data['performance'] = [personaje.performance for personaje in personajes]

    poblacion_0 = equipment_data.sort_values(by='performance', ascending=False)
    #print(poblacion_0)
    return poblacion_0

def eval_performace(generation,type):
    data=pd.DataFrame(generation)
    data['type'] = type
    personajes = []
    for index, row in data.iterrows():
        personaje = Character(row['type'],row['height'],row['strength'],row['agility'],row['expertise'],row['resistance'],row['life'])
        personajes.append(personaje)
    data['performance'] = [personaje.performance for personaje in personajes]

    poblacion_0 = data.sort_values(by='performance', ascending=False)

    return poblacion_0