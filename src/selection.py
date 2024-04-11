import math
import random
import pandas as pd
import numpy as np

def elitist_selection(population, k):
    N = len(population)
    #elite_size = int(N * k)

    if k <= 0:
        raise ValueError('k debe ser mayor que cero.')
    elif k > N:
        raise ValueError('k debe ser menor o igual a N.')
    # Ordenar la población según el rendimiento
    #sorted_population = sorted(population, key=lambda x: x['performance'], reverse=True)
    sorted_population = population.sort_values(by='performance', ascending=False)

    # Seleccionar los mejores individuos como élite
    elite = sorted_population[:k]

    # Crear nueva población
    new_population = pd.DataFrame(columns=elite.columns)

    # Agregar élites múltiples veces según n(i)
    for i in range(k):
        ni = math.ceil((k - i) / N)  # Calcular n(i)
        #print(f"ni para el individuo {i}: {ni}")
        for _ in range(ni):
            new_population = pd.concat([new_population, elite.iloc[i].to_frame().T], ignore_index=True)
    
    # Completar la población con individuos aleatorios si es necesario
    #while len(new_population) < N:
    #    new_population.append(random.choice(elite))

    return new_population

def add_relative_acumulate(population):
    # Calcular el performance relativo
    sum_performance = population['performance'].sum()
    population['performance_relative'] = (population['performance'] / sum_performance) 
    # Calcular la frecuencia relativa acumulada
    population['performance_accumulated'] = population['performance_relative'].cumsum()

    return population

def roulette_wheel_selection(population, k):
    """
    This function makes a selection of [k] individuals by applying the roulette-wheel
    method through an iterative code where a random number between 0 and 1 (uniformly
    distributed) is used as a roulette wheel spin and the cumulative sum of relative
    performance that exceeds this random number is selected.
    """

    if k <= 0:
        # For wrong cases when a negative number is selected for k individuals selection:
        raise ValueError('k value must be greater than zero...')
    else:
        individuals = {
            'strength': [],
            'agility': [],
            'expertise': [],
            'resistance': [],
            'life': [],
            'height': [],
            'type': [],
            'performance': [],
            'performance_relative': [],
            'performance_accumulated': []
        }
        for i in range(k):
            # Roulette spin inside the loop to generate a new value in each iteration:
            roulette_spin = np.random.uniform(0, 1)  
            #print(roulette_spin)
            # Looking for values greater than roulette spin:
            found_values = np.where(population['performance_accumulated'] >= roulette_spin)[0]
            #print(found_values)
            # Getting the maximum within the found subset:
            selected_index = found_values[0]
            for key in individuals.keys():
                individuals[key].append(population[key][selected_index])
        
        # Create DataFrame from selected individuals
        selected_df = pd.DataFrame(individuals)

        return selected_df
