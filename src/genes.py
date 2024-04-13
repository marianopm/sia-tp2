import pandas as pd

def height_to_bin(valor):
    switch = {
        1.3: '000',
        1.4: '001',
        1.5: '010',
        1.6: '011',
        1.7: '100',
        1.8: '101',
        1.9: '110',
        2.0: '111'
    }
    return switch.get(valor,'no valido')

def height_to_dec(valor):
    switch = {
        '000': 1.3,
        '001': 1.4,
        '010': 1.5,
        '011': 1.6,
        '100': 1.7,
        '101': 1.8,
        '110': 1.9,
        '111': 2.0
    }
    valor_str = str(valor).zfill(3)
    return switch.get(valor_str,'no valido!')

def encode_genes(individuals_orig):
    individuals = individuals_orig.copy()
    # Encoding strengths:
    strength = individuals['strength'].apply(lambda x: format(int(x), '08b'))

    # Encoding agilities:
    agility = individuals['agility'].apply(lambda x: format(int(x), '08b'))

    # Encoding expertises:
    expertise = individuals['expertise'].apply(lambda x: format(int(x), '08b'))

    # Encoding resistances:
    resistance = individuals['resistance'].apply(lambda x: format(int(x), '08b'))

    # Encoding lifes:
    life = individuals['life'].apply(lambda x: format(int(x), '08b'))

    # Encoding heights:
    height = individuals['height'].apply( height_to_bin) 

    # Arranging variables into a DataFrame:
    chromosomes = pd.DataFrame({
        'strength': strength,
        'agility': agility,
        'expertise': expertise,
        'resistance': resistance,
        'life': life,
        'height': height
    })

    chromosomes.index = [str(i) for i in range(1, len(chromosomes) + 1)]

    return chromosomes

def decode_genes(individuals_orig):
    individuals = individuals_orig.copy()
    # Encoding strengths:
    strength = individuals['strength'].apply(lambda x: float(int(x,2)))
    
    # Encoding agilities:
    agility = individuals['agility'].apply(lambda x: float(int(x,2)))

    # Encoding expertises:
    expertise = individuals['expertise'].apply(lambda x: float(int(x,2)))

    # Encoding resistances:
    resistance = individuals['resistance'].apply(lambda x: float(int(x,2)))

    # Encoding lifes:
    life = individuals['life'].apply(lambda x: float(int(x,2)))

    # Encoding heights:
    height = individuals['height'].apply(height_to_dec)

    # Arranging variables into a DataFrame:
    chromosomes = pd.DataFrame({
        'strength': strength,
        'agility': agility,
        'expertise': expertise,
        'resistance': resistance,
        'life': life,
        'height': height,
        'height': height
    })

    chromosomes.index = [str(i) for i in range(1, len(chromosomes) + 1)]

    return chromosomes

"""


def encode_norm_genes(individuals, min_height, max_height, max_stats_value):
    # Encoding strengths:
    strength = (individuals['strength'] * 255 / max_stats_value).astype(int)
    strength = strength.apply(lambda x: format(x, '08b'))

    # Encoding agilities:
    agility = (individuals['agility'] * 255 / max_stats_value).astype(int)
    agility = agility.apply(lambda x: format(x, '08b'))

    # Encoding expertises:
    expertise = (individuals['expertise'] * 255 / max_stats_value).astype(int)
    expertise = expertise.apply(lambda x: format(x, '08b'))

    # Encoding resistances:
    resistance = (individuals['resistance'] * 255 / max_stats_value).astype(int)
    resistance = resistance.apply(lambda x: format(x, '08b'))

    # Encoding lifes:
    life = (individuals['life'] * 255 / max_stats_value).astype(int)
    life = life.apply(lambda x: format(x, '08b'))

    # Encoding heights:
    height = ((individuals['height'] - min_height) * 255 / (max_height - min_height)).astype(int)
    height = height.apply(lambda x: format(x, '08b'))

    # Arranging variables into a DataFrame:
    chromosomes = pd.DataFrame({
        'strength': strength,
        'agility': agility,
        'expertise': expertise,
        'resistance': resistance,
        'life': life,
        'height': height
    })

    chromosomes.index = [str(i) for i in range(1, len(chromosomes) + 1)]

    return chromosomes

def norm_genes_dec(individuals, min_height, max_height, max_stats_value):
    # Encoding strengths:
    strength = (individuals['strength'] / 255 * max_stats_value).astype(int)

    # Encoding agilities:
    agility = (individuals['agility'] / 255 * max_stats_value).astype(int)

    # Encoding expertises:
    expertise = (individuals['expertise'] / 255 * max_stats_value).astype(int)

    # Encoding resistances:
    resistance = (individuals['resistance'] / 255 * max_stats_value).astype(int)

    # Encoding lifes:
    life = (individuals['life'] / 255 * max_stats_value).astype(int)

    # Encoding heights:
    height = ((individuals['height'] - min_height) / (max_height - min_height) * max_height ).astype(int)

    # Arranging variables into a DataFrame:
    chromosomes = pd.DataFrame({
        'strength': strength,
        'agility': agility,
        'expertise': expertise,
        'resistance': resistance,
        'life': life,
        'height': height
    })

    chromosomes.index = [str(i) for i in range(1, len(chromosomes) + 1)]

    return chromosomes
"""
