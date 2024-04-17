import numpy as np
import pandas as pd
from stats import random_stats
from character import Character

def generate_init_population(populationNumber, maxStatsValue,characterType):
    
    equipment_data = random_stats(populationNumber, maxStatsValue)

    # Asignar valores aleatorios de la lista proporcionada a 'height'
    height_values = [1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
    #height_values = range(130,201)
    equipment_data['height'] = np.random.choice(height_values, size=populationNumber)
    # TODO: deprecado varios tipos de character
    # Asignar valores aleatorios de la lista proporcionada a 'characterType'
    #equipment_data['characterType'] = np.random.choice(list(CharacterType), size=N)
    equipment_data['characterType'] = characterType
    # Agregar objetos de la clase Personaje y calcular el desempeño
    personajes = []
    for index, row in equipment_data.iterrows():
        personaje = Character(row['characterType'],row['height'],row['strength'],row['agility'],row['expertise'],row['resistance'],row['life'])
        personajes.append(personaje)
        #print(f'Personaje creado: {personaje.characterType}')
    equipment_data['performance'] = [personaje.performance for personaje in personajes]

    poblacion_0 = equipment_data.sort_values(by='performance', ascending=False)
    poblacion_0.reset_index(drop=True, inplace=True)
    #print(poblacion_0)
    return poblacion_0

def eval_performace(generation, characterType):
    data=pd.DataFrame(generation)
    data['characterType'] = characterType
    personajes = []
    for index, row in data.iterrows():
        personaje = Character(row['characterType'],row['height'],row['strength'],row['agility'],row['expertise'],row['resistance'],row['life'])
        personajes.append(personaje)
    data['performance'] = [personaje.performance for personaje in personajes]

    poblacion_0 = data.sort_values(by='performance', ascending=False)

    return poblacion_0