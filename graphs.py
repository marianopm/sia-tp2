import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Grafico generaciones vs crossover
# Datos
""" i = 1
onePoint = []
twoPoint = []
anular = []
uniform = []
while(i<10):
    df_onePoint = pd.read_csv(f'motorAGP_one_point{i}.csv')
    valor_generacion = df_onePoint.iloc[-1][-1]
    onePoint.append(valor_generacion)
    
    df_twoPoint = pd.read_csv(f'motorAGP_two_point{i}.csv')
    valor_generacion = df_twoPoint.iloc[-1][-1]
    twoPoint.append(valor_generacion)
    
    df_anular = pd.read_csv(f'motorAGP_anular{i}.csv')
    valor_generacion = df_anular.iloc[-1][-1]
    anular.append(valor_generacion)
    
    df_uniform = pd.read_csv(f'motorAGP_uniform{i}.csv')
    valor_generacion = df_uniform.iloc[-1][-1]
    uniform.append(valor_generacion)
    
    i+=1
    
print(onePoint)
print(np.mean(onePoint))
print(np.std(onePoint))

categorias = ['One point', 'Two point', 'Anular', 'Uniform']

valores = [np.mean(onePoint), np.mean(twoPoint), np.mean(anular), np.mean(uniform)]
errores = [np.std(onePoint), np.std(twoPoint), np.std(anular), np.std(uniform)]

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Crear las barras de error
ax.bar(categorias, valores, yerr=errores, capsize=5, color = ['blue', 'green', 'red', 'purple'])

# Etiquetas y título
ax.set_ylabel('Average generations')
ax.set_xlabel('Crossover methods')
ax.set_title('Crossover method per Average generations for Archer')

# Mostrar el gráfico
plt.show() """


# Gráfico avg fitness vs crossover
# Datos
""" i = 1
onePoint = []
twoPoint = []
anular = []
uniform = []
while(i<10):
    df_onePoint = pd.read_csv(f'motorAGP_LastGeneration_one_point{i}.csv')
    valor_generacion = df_onePoint.iloc[:,-1].values
    onePoint.append(valor_generacion)
    
    df_twoPoint = pd.read_csv(f'motorAGP_LastGeneration_two_point{i}.csv')
    valor_generacion = df_twoPoint.iloc[:,-1].values
    twoPoint.append(valor_generacion)
    
    df_anular = pd.read_csv(f'motorAGP_LastGeneration_anular{i}.csv')
    valor_generacion = df_anular.iloc[:,-1].values
    anular.append(valor_generacion)
    
    df_uniform = pd.read_csv(f'motorAGP_LastGeneration_uniform{i}.csv')
    valor_generacion = df_uniform.iloc[:,-1].values
    uniform.append(valor_generacion)
    
    i+=1
    
print(onePoint)
print(np.mean(onePoint))
print(np.std(onePoint))

categorias = ['One point', 'Two point', 'Anular', 'Uniform']

valores = [np.mean(onePoint), np.mean(twoPoint), np.mean(anular), np.mean(uniform)]
errores = [np.std(onePoint), np.std(twoPoint), np.std(anular), np.std(uniform)]

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Crear las barras de error
barras = ax.bar(categorias, valores, yerr=errores, capsize=5, color = ['blue', 'green', 'red', 'purple'])

# Etiquetas y título
ax.set_ylabel('Average fitness')
ax.set_xlabel('Crossover methods')
ax.set_title('Crossover method per Average fitness for Archer')

# Imprimie el valor numerico arriba de cada barra
for barra in barras:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width() / 2, altura, str(altura), ha='center', va='bottom')

# Mostrar el gráfico
plt.show() """

# Grafico generaciones vs mutacion
# Datos
""" i = 1
one_gene = []
multi_gene = []
multi_gene_mutation_uniform = []
while(i<10):
    df_one_gene = pd.read_csv(f'motorAGP_one_gene{i}.csv')
    valor_generacion = df_one_gene.iloc[-1][-1]
    one_gene.append(valor_generacion)
    
    df_multi_gene = pd.read_csv(f'motorAGP_multi_gene{i}.csv')
    valor_generacion = df_multi_gene.iloc[-1][-1]
    multi_gene.append(valor_generacion)
    
    df_multi_gene_mutation_uniform = pd.read_csv(f'motorAGP_multi_gene_mutation_uniform{i}.csv')
    valor_generacion = df_multi_gene_mutation_uniform.iloc[-1][-1]
    multi_gene_mutation_uniform.append(valor_generacion)
    
    i+=1
    
print(one_gene)
print(np.mean(one_gene))
print(np.std(one_gene))

categorias = ['one gene', 'multi gene', 'multi gene mutation uniform']

valores = [np.mean(one_gene), np.mean(multi_gene), np.mean(multi_gene_mutation_uniform)]
errores = [np.std(one_gene), np.std(multi_gene), np.std(multi_gene_mutation_uniform)]

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Crear las barras de error
ax.bar(categorias, valores, yerr=errores, capsize=5, color = ['blue', 'green', 'red', 'purple'])

# Etiquetas y título
ax.set_ylabel('Average generations')
ax.set_xlabel('Mutation methods')
ax.set_title('Mutation methods per Average generations for Archer')

# Mostrar el gráfico
plt.show() """



# Gráfico avg fitness vs mutación
# Datos
""" i = 1
one_gene = []
multi_gene = []
multi_gene_mutation_uniform = []
while(i<10):
    df_one_gene = pd.read_csv(f'motorAGP_LastGeneration_one_gene{i}.csv')
    valor_generacion = df_one_gene.iloc[:,-1].values
    one_gene.append(valor_generacion)
    
    df_multi_gene = pd.read_csv(f'motorAGP_LastGeneration_multi_gene{i}.csv')
    valor_generacion = df_multi_gene.iloc[:,-1].values
    multi_gene.append(valor_generacion)
    
    df_multi_gene_mutation_uniform = pd.read_csv(f'motorAGP_LastGeneration_multi_gene_mutation_uniform{i}.csv')
    valor_generacion = df_multi_gene_mutation_uniform.iloc[:,-1].values
    multi_gene_mutation_uniform.append(valor_generacion)
    
    i+=1
    
print(one_gene)
print(np.mean(one_gene))
print(np.std(one_gene))

categorias = ['one gene', 'multi gene', 'multi gene mutation uniform']

valores = [np.mean(one_gene), np.mean(multi_gene), np.mean(multi_gene_mutation_uniform)]
errores = [np.std(one_gene), np.std(multi_gene), np.std(multi_gene_mutation_uniform)]

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Crear las barras de error
barras = ax.bar(categorias, valores, yerr=errores, capsize=5, color = ['blue', 'green', 'red'])

# Etiquetas y título
ax.set_ylabel('Average fitness')
ax.set_xlabel('Mutation methods')
ax.set_title('Mutation methods per Average fitness for Archer')

# Imprimie el valor numerico arriba de cada barra
 for barra in barras:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width() / 2, altura, str(altura), ha='center', va='bottom')

# Mostrar el gráfico
plt.show() """

# Grafico generaciones vs métodos de seleccion para Boltzmann
# Datos
i = 1
boltzmann = []
rank_based = []
stochastic_tournament = []
roulette_wheel = []
deterministic_tournament = []
universal_selection = []
while(i<10):
    df_boltzmann = pd.read_csv(f'motorAGP_boltzmann-elitist{i}.csv')
    valor_generacion = df_boltzmann.iloc[-1][-1]
    boltzmann.append(valor_generacion)
    
    df_rank_based = pd.read_csv(f'motorAGP_rank_based-elitist{i}.csv')
    valor_generacion = df_rank_based.iloc[-1][-1]
    rank_based.append(valor_generacion)
    
    df_multi_stochastic_tournament = pd.read_csv(f'motorAGP_stochastic_tournament-elitist{i}.csv')
    valor_generacion = df_multi_stochastic_tournament.iloc[-1][-1]
    stochastic_tournament.append(valor_generacion)
    
    df_roulette_wheel= pd.read_csv(f'motorAGP_roulette_wheel-elitist{i}.csv')
    valor_generacion = df_roulette_wheel.iloc[-1][-1]
    roulette_wheel.append(valor_generacion)
    
    df_deterministic_tournament = pd.read_csv(f'motorAGP_deterministic_tournament-elitist{i}.csv')
    valor_generacion = df_deterministic_tournament.iloc[-1][-1]
    deterministic_tournament.append(valor_generacion)
    
    df_universal_selection = pd.read_csv(f'motorAGP_universal_selection-elitist{i}.csv')
    valor_generacion = df_universal_selection.iloc[-1][-1]
    universal_selection.append(valor_generacion)
    
    i+=1
    
print(boltzmann)
print(np.mean(boltzmann))
print(np.std(boltzmann))

categorias = ['boltzmann', 'rank_based', 'stochastic_tournament','roulette_wheel', 'deterministic_tournament', 'universal_selection']

valores = [np.mean(boltzmann), np.mean(rank_based), np.mean(stochastic_tournament), np.mean(roulette_wheel), np.mean(deterministic_tournament), np.mean(universal_selection)]
errores = [np.std(boltzmann), np.std(rank_based), np.std(stochastic_tournament), np.std(roulette_wheel), np.std(deterministic_tournament), np.std(universal_selection)]

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Crear las barras de error
ax.bar(categorias, valores, yerr=errores, capsize=5, color = ['blue', 'green', 'red', 'purple', 'orange', 'gray'])

# Etiquetas y título
ax.set_ylabel('Average generations')
ax.set_xlabel('Selection methods')
ax.set_title('Selection methods per Average generations for Archer and elitist')

# Mostrar el gráfico
plt.show()


# Gráfico avg fitness vs método de selección para boltzmann
# Datos
i = 1
boltzmann = []
rank_based = []
stochastic_tournament = []
roulette_wheel = []
deterministic_tournament = []
universal_selection = []
while(i<10):
    df_boltzmann = pd.read_csv(f'motorAGP_LastGeneration_boltzmann-elitist{i}.csv')
    valor_generacion = df_boltzmann.iloc[:,-1].values
    boltzmann.append(valor_generacion)
    
    df_rank_based = pd.read_csv(f'motorAGP_LastGeneration_rank_based-elitist{i}.csv')
    valor_generacion = df_rank_based.iloc[:,-1].values
    rank_based.append(valor_generacion)
    
    df_multi_stochastic_tournament = pd.read_csv(f'motorAGP_LastGeneration_stochastic_tournament-elitist{i}.csv')
    valor_generacion = df_multi_stochastic_tournament.iloc[:,-1].values
    stochastic_tournament.append(valor_generacion)
    
    df_roulette_wheel= pd.read_csv(f'motorAGP_LastGeneration_roulette_wheel-elitist{i}.csv')
    valor_generacion = df_roulette_wheel.iloc[:,-1].values
    roulette_wheel.append(valor_generacion)
    
    df_deterministic_tournament = pd.read_csv(f'motorAGP_LastGeneration_deterministic_tournament-elitist{i}.csv')
    valor_generacion = df_deterministic_tournament.iloc[:,-1].values
    deterministic_tournament.append(valor_generacion)
    
    df_universal_selection = pd.read_csv(f'motorAGP_LastGeneration_universal_selection-elitist{i}.csv')
    valor_generacion = df_universal_selection.iloc[:,-1].values
    universal_selection.append(valor_generacion)
    
    i+=1
    
print(boltzmann)
print(np.mean(boltzmann))
print(np.std(boltzmann))

categorias = ['boltzmann', 'rank_based', 'stochastic_tournament','roulette_wheel', 'deterministic_tournament', 'universal_selection']

valores = [np.mean(boltzmann), np.mean(rank_based), np.mean(stochastic_tournament), np.mean(roulette_wheel), np.mean(deterministic_tournament), np.mean(universal_selection)]
errores = [np.std(boltzmann), np.std(rank_based), np.std(stochastic_tournament), np.std(roulette_wheel), np.std(deterministic_tournament), np.std(universal_selection)]

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Crear las barras de error
barras = ax.bar(categorias, valores, yerr=errores, capsize=5, color = ['blue', 'green', 'red', 'purple', 'orange', 'gray'])

# Etiquetas y título
ax.set_ylabel('Average fitness')
ax.set_xlabel('Selection methods')
ax.set_title('Selection methods per Average fitness for Archer and elitist')

# Imprimie el valor numerico arriba de cada barra
""" for barra in barras:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width() / 2, altura, str(altura), ha='center', va='bottom')
 """
# Mostrar el gráfico
plt.show()