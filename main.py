import configparser
from collections import defaultdict
from src.population import generate_init_population, eval_performace
from src.character import CharacterType 
from src.stats import random_stats
from src.selection import stochastic_tournament_selection, deterministic_tournament_selection, add_relative_accumulate, elitist_selection, roulette_wheel_selection, universal_selection, boltzmann_selection
from src.genes import  encode_genes, decode_genes
from src.crossover import single_point_crossover, valid_chromosome, two_point_crossover
from src.mutation import one_gene_mutation, multi_gene_mutation, multi_gene_mutation_uniform
import numpy as np
import pandas as pd
import os

def main():
    print("TP2")
    config_params = read_config('config_file.config')
    
    populationNumber = eval(config_params['N']['n'])
    type = CharacterType.ARCHER
    maxStatsValue = eval(config_params['M']['m'])
    k = eval(config_params['K']['k'])
    method1Percentage = eval(config_params['METHOD1PERCENTAGE']['percentage'])
    numberOfGenerations = eval(config_params['GENERATIONS']['number'])
    selectionMethod1 = eval(config_params['SELECTION_METHOD']['method1'])
    selectionMethod2 = eval(config_params['SELECTION_METHOD']['method2'])

    #equipment_data = random_stats(N, maxStatsValue)
    initialPopulation = generate_init_population(populationNumber, maxStatsValue, type)
    # Imprime una tabla mostrando la poblacion inicial
    #print(initialPopulation)
    
    # Agrega la performance a la población inicial
    initialPopulation = eval_performace(initialPopulation, type)
    
    poblacion_rel_acu = add_relative_accumulate(initialPopulation)
    # Imprime la tabla con las columnas de desempeño relativo y acumulado
    print(poblacion_rel_acu)
    
    # Escribe la poblacion inicial.
    poblacion_rel_acu.insert(0, 'generation', 1)
    poblacion_rel_acu.to_csv('datos.csv', mode='w', index=False)
    
    N1, N2 = method_selector(k, method1Percentage)
    
    
    i = 1
    while i < numberOfGenerations:
        selection_method(poblacion_rel_acu, N1, i)        
        i+=1
    
    
        
def method_selector(K, method1Percentage): 
    # Selecciono K individuos
    # Utilizo el porcentaje para cada método
    N1 = int(np.round(K * method1Percentage))
    N2 = K - N1
    return N1, N2

def selection_method(poblacion_rel_acu, N1, N2, i):
    print(f' PROCESO {i}')
    newPopulationElitist = elitist_selection(poblacion_rel_acu, N1)
    #print(newPopulationElitist)
    
    newPopulationRoulette = roulette_wheel_selection(poblacion_rel_acu, N2)
    #print(newPopulationRoulette)
    
    newPopulationUniversal = universal_selection(poblacion_rel_acu, N2)
    #print(newPopulationUniversal) 
    
    """¡  # Ejemplo de uso:
    mutation_rate = 0.8
    resultmp = multi_gene_mutation(cromosomas_ok1, mutation_rate)
    print(resultmp)
    
    # Ejemplo de uso:
    mutation_rate = 0.7
    resultmu = multi_gene_mutation_uniform(cromosomas_ok1, mutation_rate)
    print(resultmu)
    
    
    
    # Example usage:
    max_generation = 18
    generation = 1
    k = 4                                  # Number of desired selected individuals.
    T_0 = 20                                 # Initial temperature.
    T_offset = 0.5                          # Offset value for temperature exponential function.
    reference_generation = max_generation   # Reference generation where 0 < (T_0 - T_offset) = 0.015 = deltaT is desired.
    deltaT = 0.015                          # 0 < (T_0 - T_offset) = deltaT at reference generation.
    m = - (np.log(deltaT) - np.log(T_0 - T_offset)) / reference_generation

    new_boltzmann_selection = boltzmann_selection(initialPopulation,k,generation,T_0,T_offset,m)
    print(new_boltzmann_selection)



    individualsT = deterministic_tournament_selection(initialPopulation, 4, 5)
    print(individualsT)
    
    individualsTd = stochastic_tournament_selection(initialPopulation, 4)
    print(individualsTd) """
    
    totalSelection = pd.concat([newPopulationElitist, newPopulationRoulette])
    #print(totalSelection) 

    # Codifica los genes
    chromosomes = encode_genes(totalSelection)
    #print(chromosomes)
    
    newIndividuals = single_point_crossover(chromosomes)
    cromosomas_ok1 = valid_chromosome(newIndividuals)
    while (len(cromosomas_ok1)<1):
        newIndividuals = single_point_crossover(chromosomes)
        cromosomas_ok1 = valid_chromosome(newIndividuals)
    #newIndividuals
    #print(cromosomas_ok1)
        
    #from genes import decode_genes
    #cromosomas_decoded = decode_genes(new_individuals)
    #cromosomas_decoded
        

    new_individuals2 = two_point_crossover(chromosomes)
    cromosomas_ok2 = valid_chromosome(new_individuals2)

    while (len(cromosomas_ok2)<1):
        new_individuals2 = single_point_crossover(chromosomes)
        cromosomas_ok2 = valid_chromosome(new_individuals2)
    #new_individuals2
    #print(cromosomas_ok2)
    
        
    #from genes import decode_genes
    #cromosomas_decoded2 = decode_genes(new_individuals2)
    #cromosomas_decoded2

    #from genes import decode_genes
    #cromosomas_decoded2 = decode_genes(cromosomas_ok)
    #cromosomas_decoded2
    
    
    mutation_rate = 0.1
    if( len(cromosomas_ok1) > len(cromosomas_ok2) ):

        print("single_point_crossover won")
        result = one_gene_mutation(cromosomas_ok1, mutation_rate)
        cromosomas_okm = valid_chromosome(result)

        while (len(cromosomas_okm)<1):
            result = one_gene_mutation(cromosomas_ok1, mutation_rate)
            cromosomas_okm = valid_chromosome(result)
    else:     
        print("two_point_crossover won")   
        result = one_gene_mutation(cromosomas_ok2, mutation_rate)
        cromosomas_okm = valid_chromosome(result)

        while (len(cromosomas_okm)<1):
            result = one_gene_mutation(cromosomas_ok2, mutation_rate)
            cromosomas_okm = valid_chromosome(result)

    # print(cromosomas_okm)
    
    cromosomas_decoded2 = decode_genes(cromosomas_okm)
#    print(cromosomas_decoded2)
    
    new_generation = eval_performace(cromosomas_decoded2,type)
    print(new_generation)
    
def write_csv(dataFrame, generation):
    dataFrame['generation'] = generation
    dataFrame.to_csv('datos.csv', mode='a', index=False, header = 'False')

def read_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    params = defaultdict(dict)
    for section in config.sections():
        for key, value in config.items(section):
            params[section][key] = value
    return params

if __name__ == "__main__":
    main()

""" 
Por cada nueve generacion, se podria ir almacenado el individuo de maximo performance
 en un dataframe asi:

Generation strength	agility	expertise	resistance	life	height	type	                performance     m_sel1  m_sel2  m_cruce    m_mutation m_repl1  M_repl2	    
0	       72	    7	    60	        8	        3	    1.80	CharacterType.ARCHER	1.10397257e+03	roulete rank    oneponit   onegene    rank     tourn
1	       58	    4	    62	        11	        15	    1.80	CharacterType.ARCHER	9.54910635e+02	elite   tourn   multipoint multigen   roulete  elite

guardarlo en .csv
y con eso podriamos construir interesantes graficos, creo jeje
"""