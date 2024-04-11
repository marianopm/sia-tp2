import numpy as np
import pandas as pd

"""
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
"""
#funcion auxiliar
def valid_chromosome(individuals):
    df = pd.DataFrame(individuals)

    # Convertir las columnas a números enteros
    cols_to_sum = ['strength', 'agility', 'expertise', 'resistance', 'life']
    df[cols_to_sum] = df[cols_to_sum].apply(lambda x: x.apply(lambda y: int(y, 2)))

    # Calcular la suma de las columnas para cada fila
    df['sum'] = df[cols_to_sum].sum(axis=1)

    # Filtrar las filas donde la suma es igual a 150
    filtered_df = df[df['sum'] == 150]

    # Eliminar la columna 'sum'
    filtered_df = filtered_df.drop(columns=['sum'])

    # Convertir los valores de las columnas nuevamente a binario
    cols_to_convert = cols_to_sum 
    filtered_df[cols_to_convert] = filtered_df[cols_to_convert].map(lambda x: format(x, '08b' ))

    # Mostrar el DataFrame resultante
    return filtered_df

def single_point_crossover(individuals):
    if len(individuals) % 2 != 0:
        raise ValueError("El número de individuos seleccionados debe ser par...")
    else:
        # Crear un DataFrame para los cromosomas
        chromosomes = pd.DataFrame(individuals)
        columns_to_crossover = chromosomes.columns
        new_chromosomes = []

        for i in range(0, len(chromosomes), 2):
            # Seleccionar un punto de cruce aleatorio para cada columna
            crossover_points = {col: np.random.randint(0, 8 if col != 'height' else 3) for col in columns_to_crossover}

            offspring_1 = chromosomes.iloc[i].copy()
            offspring_2 = chromosomes.iloc[i+1].copy()

            for col, point in crossover_points.items():
                # Intercambiar los bits de cada columna en el punto de cruce
                offspring_1[col] = chromosomes.iloc[i][col][:point] + chromosomes.iloc[i+1][col][point:]
                offspring_2[col] = chromosomes.iloc[i+1][col][:point] + chromosomes.iloc[i][col][point:]

            new_chromosomes.extend([offspring_1, offspring_2])
        """
        # Mantener las columnas no afectadas
        unchanged_columns = [col for col in chromosomes.columns if col not in columns_to_crossover]
        for col in unchanged_columns:
            new_chromosomes[0][col] = chromosomes.iloc[0][col]
            new_chromosomes[1][col] = chromosomes.iloc[1][col]
        """
        # Concatenar los nuevos cromosomas y reiniciar los índices
        chromosomes = pd.DataFrame(new_chromosomes)
        chromosomes.reset_index(drop=True, inplace=True)

        return chromosomes

def two_point_crossover(individuals):
    if len(individuals) % 2 != 0:
        raise ValueError("El número de individuos seleccionados debe ser par...")
    else:
        # Crear un DataFrame para los cromosomas
        chromosomes = pd.DataFrame(individuals)
        columns_to_crossover = chromosomes.columns
        new_chromosomes = []

        for i in range(0, len(chromosomes), 2):
            # Seleccionar dos puntos de cruce aleatorios para cada columna
            crossover_points = {col: np.sort(np.random.randint(0, 8 if col != 'height' else 3, size=2)) for col in columns_to_crossover}

            offspring_1 = chromosomes.iloc[i].copy()
            offspring_2 = chromosomes.iloc[i+1].copy()

            for col, points in crossover_points.items():
                # Intercambiar los bits de cada columna entre los puntos de cruce
                offspring_1[col] = chromosomes.iloc[i][col][:points[0]] + chromosomes.iloc[i+1][col][points[0]:points[1]] + chromosomes.iloc[i][col][points[1]:]
                offspring_2[col] = chromosomes.iloc[i+1][col][:points[0]] + chromosomes.iloc[i][col][points[0]:points[1]] + chromosomes.iloc[i+1][col][points[1]:]

            new_chromosomes.extend([offspring_1, offspring_2])
        """
        # Mantener las columnas no afectadas
        unchanged_columns = [col for col in chromosomes.columns if col not in columns_to_crossover]
        for col in unchanged_columns:
            new_chromosomes[0][col] = chromosomes.iloc[0][col]
            new_chromosomes[1][col] = chromosomes.iloc[1][col]
        """
        # Concatenar los nuevos cromosomas y reiniciar los índices
        chromosomes = pd.DataFrame(new_chromosomes)
        chromosomes.reset_index(drop=True, inplace=True)

        return chromosomes
    
def uniformCrossover(individuals,M):
    pass

def annularCrossover(individuals,M):
    pass