
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datos.csv')

# Graficar cada X filas (Cantidad de poblacion + 1)
X = 201

# Seleccionar cada X filas
df_seleccionado = df.iloc[::X]

# Graficar
plt.figure(figsize=(8, 6))
plt.plot(df_seleccionado.index, df_seleccionado['performance'], marker='o', color='blue', linestyle='-')
plt.xlabel(f'Generación')
plt.ylabel('Performance')
plt.title(f'Performance vs. Generaciones')
plt.xticks(df_seleccionado.index, df_seleccionado.index + 1)
plt.grid(True)
plt.show()