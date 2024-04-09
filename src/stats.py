import numpy as np
import pandas as pd

def random_stats(N, maxStatsValue):
    """
    This function creates a DataFrame with N possible equipments arranged
    through uniform random stats for each one (by considering sum(stats) = 150),
    which will be subsequently provided to the battle rebel (class).

    All equipment items contain certain features (stats): strength, agility,
    expertise, resistance, and life, and they are established for generation 0
    as follows.
    """

    strength = []
    agility = []
    expertise = []
    resistance = []
    life = []
    

    # Other selections (0 to N-1):
    i = 0
    while i < N:
        strength_j = (int(np.round(np.random.uniform(1, maxStatsValue))))
        agility_j = (int(np.round(np.random.uniform(1, maxStatsValue))))
        expertise_J = (int(np.round(np.random.uniform(1, maxStatsValue))))
        resistance_J = (int(np.round(np.random.uniform(1, maxStatsValue))))
        life_J = (int(np.round(np.random.uniform(1, maxStatsValue))))
        # Establishing assignation condition:
        if ( sum([strength_j, agility_j, expertise_J, resistance_J, life_J]) == maxStatsValue ):
            i += 1
            strength.append(strength_j)
            agility.append(agility_j)
            expertise.append(expertise_J)
            resistance.append(resistance_J)
            life.append(life_J)
        

    equipmentIndex = list(range(0, N))
    data = {'equipmentIndex': equipmentIndex,
            'strength': strength,
            'agility': agility,
            'expertise': expertise,
            'resistance': resistance,
            'life': life}

    return pd.DataFrame(data)