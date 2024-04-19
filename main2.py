import numpy as np
import pandas as pd
pd.options.display.float_format = '{:.8e}'.format

import configparser
from collections import defaultdict
from src.character import Character, CharacterType 
from src.stats import random_stats
from src.genes import  encode_genes, decode_genes
from src.mutation import one_gene_mutation, multi_gene_mutation, multi_gene_mutation_uniform

import sys
sys.path.append("src")

from src.population import generate_init_population, eval_performace
from src.selection import stochastic_tournament_selection, deterministic_tournament_selection, add_relative_accumulate, elitist_selection, roulette_wheel_selection, universal_selection, boltzmann_selection, rank_based_selection
from src.crossover import single_point_crossover, two_point_crossover, uniform_crossover, annular_crossover, normalize_chromosome

def read_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    params = defaultdict(dict)
    for section in config.sections():
        for key, value in config.items(section):
            params[section][key] = value
    return params

#params = read_config('config_file.config')

from collections import namedtuple

def parameters():
    
    config_params = read_config('config_file.config')

    # Personaje 
    type = eval(config_params['CHARACTER']['type'])
    
    # sum( stats ) = 150
    maxStatsValue = eval(config_params['M']['m'])
    
    # N
    populationNumber = eval(config_params['N']['n'])
    # K
    k = eval(config_params['K']['k'])

    # Numero máximo de generaciones - criterio de corte
    numberOfGenerations = eval(config_params['GENERATIONS']['number'])
    
    # A%
    method1Percentage = eval(config_params['METHOD1PERCENTAGE']['percentage'])
    selectionMethod1 = eval(config_params['SELECTION_METHOD']['method1'])
    selectionMethod2 = eval(config_params['SELECTION_METHOD']['method2'])
   
    # CrossOver
    metodo_cruza = eval(config_params['metodo_cruza']['crossover'])
 
    # Mutation
    mutation_type = eval(config_params['MUTATION']['mutation_type'])
    mutation_rate = eval(config_params['MUTATION']['mutation_rate'])

    # B%
    methodReplacePercentage = eval(config_params['METHODRePERCENTAGE']['percentage'])
    metodo_reemplazo3 = eval(config_params['metodo_reemplazo']['metodo1'])
    metodo_reemplazo4 = eval(config_params['metodo_reemplazo']['metodo2'])

    cutCriteria = eval(config_params['CUT_CRITERIA']['criteria_type'])
    
    # Selector parameters
    # M
    tournament_size = eval(config_params['deterministic_tournament_selection']['tournament_size'])
    # stochastic_tournament_selection
    threhold = eval(config_params['stochastic_tournament_selection']['threshold'])
    # Boltzmann parameters
    boltzmannT_0 = eval(config_params['BOLTZMANN']['t_0'])
    boltzmannT_c = eval(config_params['BOLTZMANN']['t_c'])
    boltzmannM = eval(config_params['BOLTZMANN']['m'])

    Param = namedtuple('Param',[
        'character',
        'maxStatsValue',
        'populationNumber',
        'k',
        'numberOfGenerations',
        'method1Percentage',
        'selectionMethod1',
        'selectionMethod2',
        'metodo_cruza',
        'mutation_type',
        'mutation_rate',
        'methodReplacePercentage',
        'metodo_reemplazo3',
        'metodo_reemplazo4',
        'cutCriteria',
        'tournament_size',
        'threhold',
        'boltzmannT_0',
        'boltzmannT_c',
        'boltzmannM'
    ])    

    parametros = Param(
                character=type,
                maxStatsValue=maxStatsValue,
                populationNumber=populationNumber,
                k=k,
                numberOfGenerations=numberOfGenerations,
                method1Percentage=method1Percentage,
                selectionMethod1=selectionMethod1,
                selectionMethod2=selectionMethod2,
                metodo_cruza=metodo_cruza,
                mutation_type=mutation_type,
                mutation_rate=mutation_rate,
                methodReplacePercentage=methodReplacePercentage,
                metodo_reemplazo3=metodo_reemplazo3,
                metodo_reemplazo4=metodo_reemplazo4,
                cutCriteria=cutCriteria,
                tournament_size=tournament_size,
                threhold=threhold,
                boltzmannT_0=boltzmannT_0,
                boltzmannT_c=boltzmannT_c,
                boltzmannM=boltzmannM
    )
    return parametros

def method_selector(Kt, method1Percentage): 
    # Selecciono K individuos
    # Utilizo el porcentaje para cada método
    K1 = int(np.round(Kt * method1Percentage))
    K2 = Kt - K1
    return K1, K2

def selection_method(poblacion, ki, params, method, generation):

    if(method == 'elitist'):
        selected = elitist_selection(poblacion, ki)
    elif(method == 'roulette_wheel'):
        selected = roulette_wheel_selection(poblacion, ki)
    elif(method == 'boltzmann'):
        selected = boltzmann_selection(poblacion, ki, generation, params.boltzmannT_0,params.boltzmannT_c,params.boltzmannM)
    elif(method == 'universal_selection'):
        selected = universal_selection(poblacion, ki)
    elif(method == 'deterministic_tournament'):
        selected = deterministic_tournament_selection(poblacion, params.tournament_size, ki)
    elif(method == 'stochastic_tournament'):
        selected = stochastic_tournament_selection(poblacion, ki, params.threhold)
    elif(method == 'rank_based'):
        selected = rank_based_selection(poblacion, ki)
    return selected

def crossover_method(poblacion, method):
    
    if(method == 'one_point'):
        crossed = single_point_crossover(poblacion)
    elif(method == 'two_point'):
        crossed = two_point_crossover(poblacion)
    elif(method == 'uniform'):
        crossed = uniform_crossover(poblacion)
    elif(method == 'annular'):
        crossed = annular_crossover(poblacion)
    
    return crossed

def mutation_method(poblacion, rate, method):
    
    if(method == 'one_gene'):
        mutated = one_gene_mutation(poblacion, rate)
    elif(method == 'multi_gene'):
        mutated = multi_gene_mutation(poblacion, rate)
    elif(method == 'multi_gene_mutation_uniform'):
        mutated = multi_gene_mutation_uniform(poblacion, rate)
    
    return mutated

def main():
    # Lectura de parametros
    params = read_config('config_file.config')
    p = parameters()
    print(f'N = {p.populationNumber}')
    print(f'K = {p.k}')
    max_generations = p.numberOfGenerations
    print(f'max_generations = {p.numberOfGenerations}')

    # Generacion 0
    generation_0 = generate_init_population(p.populationNumber,p.maxStatsValue,p.character)
    generacion = 1

    current_generation = generation_0

    # GUARDO EL MAS APTO DE LA GENERACION 0
    # Escribe la poblacion inicial.
    generation_0['generation'] = generacion
    mas_apto_G0 = generation_0.head(1)
    mas_apto_G0.to_csv(f'datos-Prueba1.csv', mode='w', index=False)
    generation_0.drop(columns=['generation'], inplace=True)

    #MOTOR AG START!
    while(generacion < max_generations):
        # SELECCION DE PADRES
        k1, k2 = method_selector(p.k, p.method1Percentage)
        
        generacion_sel1 = selection_method(current_generation, k1, p, p.selectionMethod1, generacion)
        generacion_sel2 = selection_method(current_generation, k2, p, p.selectionMethod2, generacion)

        # SELECCION TOTAL: K padres
        selection_total = pd.concat([generacion_sel1, generacion_sel2])

        #selection_total.drop(columns=['performance_relative'], inplace=True)
        #selection_total.drop(columns=['performance_accumulated'], inplace=True)
        selection_total = selection_total.sort_values(by='performance', ascending=False)
        selection_total.reset_index(drop=True, inplace=True)

        selection_total.to_csv(f'selection_total.csv', mode='w', index=False)

        # CROSSOVER
        cromosomas = encode_genes(selection_total)
        crossed_result = crossover_method(cromosomas, p.metodo_cruza)
        #print(f'tamanio cross: {len(crossed_result)}')

        # MUTACION
        mutation_result = mutation_method(crossed_result, p.mutation_rate, p.mutation_type)
        cromosomas_norm = normalize_chromosome(mutation_result)
        #print(f'tamanio mutacion: {len(mutation_result)}')
        #print(f'tamanio normalizaion: {len(cromosomas_norm)}')

        # Decodifico los valores de los stats
        cromosomas_norm_decode = decode_genes(cromosomas_norm)
        #print(f'tamanio normalizaion decode: {len(cromosomas_norm_decode)}')

        # Calculo el PERFORMANCE
        offspring = eval_performace(cromosomas_norm_decode,p.character)

        offspring = offspring.sort_values(by='performance', ascending=False)
        offspring.reset_index(drop=True, inplace=True)
        # OFFSPRING son los hijos

        #print(f'tamanio padre = {len(selection_total)}')
        #print(f'tamanio hijos = {len(offspring)}')

        # REEMPLAZO
        # CRITERIO DE REEMPLAZO
        # padres:  selection_total de tamaño K
        # hijos: offspring  de tamaño K
        # tomo K de los hijos
        k_reemplazo_metodo3 = round(p.k * p.methodReplacePercentage)
        
        # el resto para completar N
        k_reemplazo_metodo4 = p.populationNumber - k_reemplazo_metodo3

        #print(f'k_reemplazo_metodo3 R = (k * {p.methodReplacePercentage}) = {k_reemplazo_metodo3}')
        #print(f'k_reemplazo_metodo4 (N - R)= {k_reemplazo_metodo4}')

        # REEMPLAZO DE INDIVIDUOS
        generacion_reemp1 = selection_method(offspring, k_reemplazo_metodo3, p, p.metodo_reemplazo3, generacion)
        generacion_reemp2 = selection_method(current_generation, k_reemplazo_metodo4, p, p.metodo_reemplazo4, generacion)
        
        #print(f'k_reemplazo_metodo3 (k) = {len(generacion_reemp1)}')
        #print(f'k_reemplazo_metodo4 (N - k)= {len(generacion_reemp2)}')

        # INDIVIDUOS TOTAL
        new_generation = pd.concat([generacion_reemp1, generacion_reemp2])

        #new_generation.drop(columns=['performance_relative'], inplace=True)
        #new_generation.drop(columns=['performance_accumulated'], inplace=True)
        new_generation = new_generation.sort_values(by='performance', ascending=False)
        new_generation.reset_index(drop=True, inplace=True)

        generacion += 1

        current_generation = new_generation

        # GUARDO EL MAS APTO DE LA GENERACION NUEVA
        new_generation['generation'] = generacion
        mas_apto_NG = new_generation.head(1)
        mas_apto_NG.to_csv(f'datos-Prueba1.csv', mode='a', header=False, index=False)
        new_generation.drop(columns=['generation'], inplace=True)

if __name__ == "__main__":
    main()
