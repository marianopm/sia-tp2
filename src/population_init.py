import numpy as np

from character import Character 
from stats import random_stats

def generate(N, maxStatsValue,type):
    
    equipment_data = random_stats(N, maxStatsValue)

    # Asignar valores aleatorios de la lista proporcionada a 'height'
    height_values = [1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
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

    poblacion_0 = equipment_data.sort_values(by='performance', ascending=True)

    return poblacion_0