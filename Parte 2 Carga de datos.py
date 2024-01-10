import pandas as pd

# Convertir la estructura Dataset en un DataFrame de Pandas
df = pd.DataFrame(dataset)

# Separar el DataFrame en dos: uno para personas que perecieron (is_dead=1) y otro para el complemento.
df_perecieron = df[df['is_dead'] == 1]
df_no_perecieron = df[df['is_dead'] == 0]

# Calcular los promedios de las edades de cada dataset e imprimir
promedio_edades_perecieron = df_perecieron['Edad'].mean()
promedio_edades_no_perecieron = df_no_perecieron['Edad'].mean()

print(f'Promedio de edades de personas que perecieron: {promedio_edades_perecieron}')
print(f'Promedio de edades de personas que no perecieron: {promedio_edades_no_perecieron}')
