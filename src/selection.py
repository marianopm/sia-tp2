import math
import random
import pandas as pd
import numpy as np

#funcion auxiliar
def add_relative_accumulate(population):
    # Crear una copia del DataFrame original para evitar modificar el DataFrame original
    population2 = population.copy()
    
    # Calcular el performance relativo
    sum_performance = population2['performance'].sum()
    print(f'sum: {sum_performance}')
    population2['performance_relative'] = population2['performance'] / sum_performance 
    
    # Calcular la frecuencia relativa acumulada
    population2['performance_accumulated'] = population2['performance_relative'].cumsum()

    return population2

def elitist_selection(population, elite_factor):
    N = len(population)
    k = elite_factor
    #elite_size = int(N * k)

    if elite_factor <= 0:
        raise ValueError('k debe ser mayor que cero.')
    #elif k > N:
    #    raise ValueError('k debe ser menor o igual a N.')
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
                #individuals[key].append(population[key][selected_index])   #el uso de key esta deprecado
                individuals[key].append(population.iloc[selected_index][key])
        
        # Create DataFrame from selected individuals
        selected_df = pd.DataFrame(individuals)

        return selected_df
    
def boltzmann_selection(population, k, generation, T_0, T_offset, m):
    """
    This function makes a [k]-individuals selection by applying the
    Boltzmann selection method through an iterative code that draws inspiration
    from physics, particularly from statistical mechanics and the concept of
    Boltzmann distribution. It introduces a probabilistic selection mechanism that
    encourages exploration by providing a way to escape local optima.

    Boltzmann selection offers a balance between exploration and exploitation,
    making it particularly useful for problems with rugged fitness landscapes or
    where maintaining diversity is important. By introducing randomness controlled
    by the temperature parameter, Boltzmann selection enables the algorithm to
    escape local optima and explore the search space more thoroughly.

    However, Boltzmann selection also has its challenges, such as choosing an
    appropriate temperature schedule and dealing with convergence issues. Careful
    tuning of the temperature parameter and annealing schedule is necessary to
    ensure good performance on a given problem.
    """
    if k <= 0:
        # For wrong cases when is selected a negative number for k-individuals selection:
        raise ValueError('k value must be greater than selected one...')
    else:
        # Temperature equation in function of the generation instant:
        T = T_offset + (T_0 - T_offset) * np.exp(-m * generation)
        # Pseudo-fitness function (along temperature):
        popu = population.loc[:, ['strength','agility','expertise','resistance','life','height','type','performance']]
        popu['performance'] = np.exp(popu['performance'] / T) / np.sum(np.exp(popu['performance'] / T))
        
        poblacion_rel_acu = add_relative_accumulate(popu)
        
        print(poblacion_rel_acu)

        selected = roulette_wheel_selection(poblacion_rel_acu, k)
    return selected

