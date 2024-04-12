import configparser
from collections import defaultdict
from src.population import generate_init_population, eval_performace
from src.character import CharacterType 
from src.stats import random_stats
from src.selection import add_relative_accumulate
from src.selection import elitist_selection, roulette_wheel_selection, universal_selection
import numpy as np

def main():
    print("TP2")
    config_params = read_config('config_file.config')
    
    populationNumber = eval(config_params['N']['n'])
    type = CharacterType.ARCHER
    maxStatsValue = eval(config_params['M']['m'])
    k = eval(config_params['K']['k'])
    method1Percentage = eval(config_params['METHOD1PERCENTAGE']['percentage'])

    #equipment_data = random_stats(N, maxStatsValue)
    initialPopulation = generate_init_population(populationNumber,maxStatsValue,type)
    # Imprime una tabla mostrando la poblacion inicial
    #print(initialPopulation)
    
    # Agrega la performance a la población inicial
    initialPopulation = eval_performace(initialPopulation, type)
    
    poblacion_rel_acu = add_relative_accumulate(initialPopulation)
    # Imprime la tabla con las columnas de desempeño relativo y acumulado
    print(poblacion_rel_acu)
    
    N1, N2 = method_selector(k, method1Percentage)
    
    newPopulationElitist = elitist_selection(poblacion_rel_acu, N1)
    print(newPopulationElitist)
    
    newPopulationRoulette = roulette_wheel_selection(poblacion_rel_acu, N2)
    print(newPopulationRoulette)
    
    newPopulationUniversal = universal_selection(poblacion_rel_acu, N2)
    print(newPopulationUniversal) 
    
def method_selector(K, method1Percentage): 
    # Selecciono K individuos
    # Utilizo el porcentaje para cada método
    N1 = int(np.round(K * method1Percentage))
    N2 = K - N1
    return N1, N2

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
