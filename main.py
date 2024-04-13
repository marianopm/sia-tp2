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

## ideas (esto es para vos, luego borra esto)
""" 
Por cada nueve generacion, se podria ir almacenado el individuo de maximo performance
 en un dataframe asi:

Generation strength	agility	expertise	resistance	life	height	type	                performance     m_sel1  m_sel2  m_cruce    m_mutation m_repl1  M_repl2	    
0	       72	    7	    60	        8	        3	    1.80	CharacterType.ARCHER	1.10397257e+03	roulete rank    oneponit   onegene    rank     tourn
1	       58	    4	    62	        11	        15	    1.80	CharacterType.ARCHER	9.54910635e+02	elite   tourn   multipoint multigen   roulete  elite

guardarlo en .csv
y con eso podriamos construir interesantes graficos, creo jeje
"""