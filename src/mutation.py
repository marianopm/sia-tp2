import numpy as np
import pandas as pd

def one_gene_mutation(individuals, mutation_rate):
    if mutation_rate < 0 or mutation_rate > 1:
        # For wrong cases when is selected a negative number, 0 or greater than 1
        # for mutationRate value:
        raise ValueError("Selected mutation_rate value must be between 0 and 1...")
    else:
        # Making a copy of individuals chromosome data:
        chromosomes = individuals.copy()
        # Selection of each offspring's individual:
        for i in range(len(chromosomes)):
            gene_index = np.random.randint(0, len(chromosomes.columns))    # Selecting a random gene.
            gene = chromosomes.iloc[i, gene_index]
            mutated_gene = ""
            for bit in gene:  # Iterate over each bit in the gene
                mutation = np.random.uniform(0, 1)  # Making mutation according mutation rate.
                if mutation <= mutation_rate:
                    # Mutation by flipping bit.
                    mutated_bit = '1' if bit == '0' else '0'
                    mutated_gene += mutated_bit
                else:
                    mutated_gene += bit
            chromosomes.iloc[i, gene_index] = mutated_gene  # Adding mutation to the offspring.
    return chromosomes

#Mutación Multigen Completa
def multi_gene_mutation(individuals, mutation_rate):
    if mutation_rate < 0 or mutation_rate > 1:
        raise ValueError('La tasa de mutación seleccionada debe estar entre 0 y 1...')
    else:
        chromosomes = individuals.copy()
        chromosomes = chromosomes.reset_index(drop=True)
        print(chromosomes)
        for i in range(len(chromosomes)):
            #print(i)
            for col in chromosomes.columns:
                #print(col)
                if np.random.uniform(0, 1) < mutation_rate:  # Probabilidad de mutación
                    gene = list(chromosomes.loc[i, col])  # Convertir la cadena binaria en lista de bits
                    #print(gene)
                    for j in range(len(gene)):  # Iterar sobre cada bit del gen
                        if np.random.uniform(0, 1) < mutation_rate:  # Probabilidad de mutación para cada bit
                            gene[j] = '1' if gene[j] == '0' else '0'  # Cambiar el bit
                    chromosomes.loc[i, col] = ''.join(gene)  # Convertir la lista de bits nuevamente a cadena binaria
        return chromosomes
    
#Mutación Multigen Uniforeme
def multi_gene_mutation_uniform(individuals, mutation_rate):
    """
    Implementa la mutación multi-gen uniforme.
    """
    if mutation_rate < 0 or mutation_rate > 1:
        raise ValueError('La tasa de mutación seleccionada debe estar entre 0 y 1...')
    else:
        chromosomes = individuals.copy()
        chromosomes = chromosomes.reset_index(drop=True)
        print(chromosomes)
        for i in range(len(chromosomes)):
            for col in chromosomes.columns:
                # Genera un número aleatorio entre 0 y 1 para cada gen
                if np.random.uniform(0, 1) <= mutation_rate:
                    # Aplica la mutación al gen seleccionado
                    gene = chromosomes.loc[i, col]
                    mutated_gene = mutate_gene_uniform(gene)
                    chromosomes.loc[i, col] = mutated_gene
        return chromosomes

def mutate_gene_uniform(gene):
    """
    Realiza la mutación de un gen de forma uniforme.
    """
    mutated_gene = ''.join(['1' if bit == '0' else '0' for bit in gene])
    return mutated_gene