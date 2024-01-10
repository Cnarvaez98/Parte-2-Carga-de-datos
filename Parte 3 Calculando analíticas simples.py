import pandas as pd


# Verificar tipos de datos y corregir si es necesario
df['Edad'] = pd.to_numeric(df['Edad'], errors='coerce')  # Convertir 'Edad' a numérico, manejar errores
df['Fumador'] = df['Fumador'].astype(str)  # Convertir 'Fumador' a cadena
# Asegúrate de hacer conversiones similares según las necesidades de tu dataset

# Verificar tipos de datos después de las conversiones
print(df.dtypes)

# Calcular cantidad de hombres fumadores vs mujeres fumadoras
resultados = df.groupby(['Sexo', 'Fumador']).size().unstack()
print(resultados)
