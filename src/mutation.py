import numpy as np
import pandas as pd

def one_gene_mutation(individuals, mutation_rate):
    """
    In genetic algorithms, mutation is an operator used to introduce random changes
    in individuals (or chromosomes) within the population. Mutation plays a crucial
    role in maintaining diversity within the population and helping the algorithm
    explore new regions of the search space. A "one gene mutation" typically refers
    to a mutation operation where only one gene (or allele) in the chromosome is
    altered.

    You can adjust the mutation rate according to your problem domain and requirements.
    A low mutation rate ensures that only a small proportion of individuals undergo
    mutation in each generation, preventing excessive disruption to good solutions.

    If you're working with a representation where each gene encodes multiple bits,
    the mutation operation needs to be adjusted accordingly. The mutation rate
    determines the probability of mutation occurring for each bit within the selected
    gene. The gene is selected randomly, and then each bit within that gene has
    a chance to be flipped based on the mutation rate.
    """
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