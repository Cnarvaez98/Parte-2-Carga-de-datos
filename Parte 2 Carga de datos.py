import pandas as pd

# Crear el DataFrame desde la estructura dataset
data = {
    'Nombre': ['Persona1', 'Persona2', 'Persona3'],
    'Edad': [25, 32, 28],
    'is_dead': [0, 1, 0]
}

df = pd.DataFrame(data)

# Separar el DataFrame en dos: uno para personas que perecieron (is_dead=1) y otro para el complemento.
df_perecieron = df[df['is_dead'] == 1]
df_no_perecieron = df[df['is_dead'] == 0]

# Calcular los promedios de las edades de cada dataset e imprimir.
promedio_edades_perecieron = df_perecieron['Edad'].mean()
promedio_edades_no_perecieron = df_no_perecieron['Edad'].mean()

# Imprimir resultados
print(f'Promedio de edades de personas que perecieron: {promedio_edades_perecieron}')
print(f'Promedio de edades de personas que no perecieron: {promedio_edades_no_perecieron}')
