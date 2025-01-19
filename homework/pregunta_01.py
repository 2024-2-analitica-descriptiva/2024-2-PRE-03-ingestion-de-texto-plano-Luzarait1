"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


import pandas as pd

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requisitos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.
    """
    with open('files/input/clusters_report.txt', 'r') as file:
        lines = file.readlines()

    lines = lines[4:]
    
    clusters = []
    cantidad_palabras_clave = []
    porcentaje_palabras_clave = []
    palabras_clave = []

    current_keywords = [] 

    for line in lines:
        line = line.strip()
        
        if line[0].isdigit():
            if current_keywords:
                palabras_clave.append(", ".join(current_keywords).replace(" ,", ","))
                current_keywords = []

            parts = line.split()
            clusters.append(int(parts[0]))
            cantidad_palabras_clave.append(int(parts[1]))
            porcentaje_palabras_clave.append(float(parts[2].replace(',', '.')))
            
            if len(parts) > 3:
                current_keywords.extend(parts[3:])
        else:
            current_keywords.extend(line.split())

    if current_keywords:
        palabras_clave.append(", ".join(current_keywords).replace(" ,", ","))

    data = {
        "cluster": clusters,
        "cantidad_de_palabras_clave": cantidad_palabras_clave,
        "porcentaje_de_palabras_clave": porcentaje_palabras_clave,
        "principales_palabras_clave": palabras_clave,
    }
    df = pd.DataFrame(data)
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    
    return df
df_resultado = pregunta_01()
print(df_resultado)

