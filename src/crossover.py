import numpy as np
import pandas as pd

def valid_offspring(cromosomas_decoded):
    df = pd.DataFrame(cromosomas_decoded)
    # Crear un DataFrame vacío para almacenar las filas que suman exactamente 150
    result_df = pd.DataFrame(columns=df.columns)
    valid = 0
    # Recorrer todas las filas
    for index, row in df.iterrows():
        # Calcular la suma de las columnas 'strength', 'agility', 'expertise', 'resistance' y 'life'
        sum_values = row[['strength', 'agility', 'expertise', 'resistance', 'life']].sum()
        # Verificar si la suma es exactamente 150
        if sum_values == 150:
            # Agregar la fila al nuevo DataFrame usando loc
            result_df.loc[index] = row
            valid += 1
    return valid, result_df

def single_point_crossover(individuals):
    if len(individuals) % 2 != 0:
        raise ValueError("El número de individuos seleccionados debe ser par...")
    else:
        # Crear un DataFrame para los cromosomas
        chromosomes = pd.DataFrame(individuals)

        new_chromosomes = []

        for i in range(0, len(chromosomes), 2):
            crossover_point = np.random.randint(0, len(chromosomes.columns))

            if crossover_point == 0:
                # Uno de los hijos toma todos los genes del padre y el otro hijo toma
                # el genotipo completo de la madre.
                offspring_1 = chromosomes.iloc[i]
                offspring_2 = chromosomes.iloc[i+1]
            else:
                # Se ejecuta el cruce de un solo punto
                offspring_1 = pd.concat([chromosomes.iloc[i][:crossover_point], chromosomes.iloc[i+1][crossover_point:]])
                offspring_2 = pd.concat([chromosomes.iloc[i+1][:crossover_point], chromosomes.iloc[i][crossover_point:]])

            new_chromosomes.append(offspring_1)
            new_chromosomes.append(offspring_2)

        # Concatenar los nuevos cromosomas y reiniciar los índices
        chromosomes = pd.DataFrame(new_chromosomes)
        chromosomes.reset_index(drop=True, inplace=True)

        return chromosomes
