
import pandas as pd
import configparser
from collections import defaultdict
import matplotlib.pyplot as plt

    
# Grafico Performance vs Generacion
df = pd.read_csv('datos.csv')

# Graficar cada X filas (Cantidad de poblacion + 1)
X = 200 + 1

# Seleccionar cada X filas
df_seleccionado = df.iloc[::X]

# Graficar
plt.figure(figsize=(8, 6))
plt.plot(df_seleccionado['generation'], df_seleccionado['performance'], marker='o', color='blue', linestyle='-')
plt.xlabel(f'Generación')
plt.ylabel('Performance')
plt.title(f'Performance vs. Generaciones')
plt.xticks(df_seleccionado['generation'], df_seleccionado['generation'])
plt.grid(True)
plt.show()





# Grafico Cruce vs Fitness
""" dfAnnular = pd.read_csv('datosAnnular.csv')
dfOnePoint = pd.read_csv('datosOnePoint.csv')
dfUniform = pd.read_csv('datosUniform.csv')
dfTwoPoint = pd.read_csv('datosTwoPoint.csv')
 """
# Graficar cada X filas (Cantidad de poblacion + 1)
X = 200 + 1

# Seleccionar cada X filas
df_seleccionado = df.iloc[::X]

# Graficar
plt.figure(figsize=(8, 6))
plt.plot(df_seleccionado['generation'], df_seleccionado['performance'], color='blue')
plt.xlabel(f'Generación')
plt.ylabel('Performance')
plt.title(f'Performance vs. Generaciones')
plt.xticks(df_seleccionado['generation'], df_seleccionado['generation'])
plt.grid(True)
plt.show()
