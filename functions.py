## FUNCIONES DE UTILIDAD PARA EL ETL Y EDA
# Importaciones
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

def verificar_tipo_variable(df):
    '''
    Realiza un análisis de los tipos de datos y la presencia de valores nulos en un DataFrame.

    Esta función toma un DataFrame como entrada y devuelve un resumen que incluye información sobre
    los tipos de datos en cada columna.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        pandas.DataFrame: Un DataFrame que contiene el resumen de cada columna, incluyendo:
        - 'nombre_campo': Nombre de cada columna.
        - 'tipo_datos': Tipos de datos únicos presentes en cada columna.
    '''

    mi_dict = {"nombre_campo": [], "tipo_datos": []}

    for columna in df.columns:
        mi_dict["nombre_campo"].append(columna)
        mi_dict["tipo_datos"].append(df[columna].apply(type).unique())
    df_info = pd.DataFrame(mi_dict)
        
    return df_info

def convertir_a_time(x):
    '''
    Convierte un valor a un objeto de tiempo (time) de Python si es posible.

    Esta función acepta diferentes tipos de entrada y trata de convertirlos en objetos de tiempo (time) de Python.
    Si la conversión no es posible, devuelve None.

    Parameters:
        x (str, datetime, or any): El valor que se desea convertir a un objeto de tiempo (time).

    Returns:
        datetime.time or None: Un objeto de tiempo (time) de Python si la conversión es exitosa,
        o None si no es posible realizar la conversión.
    '''
    if isinstance(x, str):
        try:
            return datetime.strptime(x, "%H:%M:%S").time()
        except ValueError:
            return None
    elif isinstance(x, datetime):
        return x.time()
    return x

def verifica_duplicados_por_columna(df, columna):
    '''
    Verifica y muestra filas duplicadas en un DataFrame basado en una columna específica.

    Esta función toma como entrada un DataFrame y el nombre de una columna específica.
    Luego, identifica las filas duplicadas basadas en el contenido de la columna especificada,
    las filtra y las ordena para una comparación más sencilla.

    Parameters:
        df (pandas.DataFrame): El DataFrame en el que se buscarán filas duplicadas.
        columna (str): El nombre de la columna basada en la cual se verificarán las duplicaciones.

    Returns:
        pandas.DataFrame or str: Un DataFrame que contiene las filas duplicadas filtradas y ordenadas,
        listas para su inspección y comparación, o el mensaje "No hay duplicados" si no se encuentran duplicados.
    '''
    # Se filtran las filas duplicadas
    duplicated_rows = df[df.duplicated(subset=columna, keep=False)]
    if duplicated_rows.empty:
        return "No hay duplicados"
    
    # se ordenan las filas duplicadas para comparar entre sí
    duplicated_rows_sorted = duplicated_rows.sort_values(by=columna)
    return duplicated_rows_sorted

def ingresa_valor_frecuente(df, columna):
    '''
    Ingresa los valores faltantes en una columna de un DataFrame con el valor más frecuente.

    Esta función reemplaza los valores "SD" con NaN en la columna especificada,
    luego calcula el valor más frecuente en esa columna y utiliza ese valor
    para modificar los valores faltantes (NaN).

    Parameters:
        df (pandas.DataFrame): El DataFrame que contiene la columna a ser imputada.
        columna (str): El nombre de la columna en la que se realizará la imputación.

    Returns:
        None
    '''
    #Se reemplaza 'SD' con NaN en la columna especificada
    df[columna]=df[columna].replace('SD', pd.NA)
    
    #Verifica el valor más frecuente en la columna
    valor_frecuente= df[columna].mode().iloc[0]
    print('El valor más frecuente de', columna, 'es:', valor_frecuente)

    #Se modifican los valores NaN, con el valor más frecuente
    df[columna].fillna(valor_frecuente, inplace=True)

def ingresa_edad_media_segun_sexo(df):
    '''
    Imputa valores faltantes en la columna 'Edad' utilizando la edad promedio según el género.

    Esta función reemplaza los valores "SD" con NaN en la columna 'Edad', calcula la edad promedio
    para cada grupo de género (Femenino y Masculino), imprime los promedios calculados y
    luego llena los valores faltantes en la columna 'Edad' utilizando el promedio correspondiente
    al género al que pertenece cada fila en el DataFrame.

    Parameters:
        df (pandas.DataFrame): El DataFrame que contiene la columna 'Edad' a ser imputada.

    Returns:
        None
    '''
    #Reemplaza 'SD' con NaN en la columna 'Edad'.
    df['Edad']= df['Edad'].replace('SD', pd.NA)

    #Se calcula el valor promedio de la edad, para cada género(es decir, agrupamos por género).
    promedio_por_genero=(df.groupby('Sexo')['Edad'].mean()).astype(int)
    print(f'La edad promedio de Femenino es {round(promedio_por_genero["FEMENINO"])} y de Masculino es {round(promedio_por_genero["MASCULINO"])}')

    #Modificamos los valores NaN en 'Edad', con los valores correspondientes en cada género.
    #Se verifica fila por fila, si el valor en 'Edad' es NaN, se aplica la función, sino se devuelve el valor original.
    df['Edad']= df.apply(lambda row: promedio_por_genero[row['Sexo']] if pd.isna(row['Edad']) else row['Edad'], axis=1)

    #Convertimos el valor ingresado a tipo int
    df['Edad']= df['Edad'].astype(int)


def accidentes_mensuales(df):
    '''
    Crea gráficos de línea para la cantidad de víctimas de accidentes mensuales por año.

    Esta función toma un DataFrame que contiene datos de accidentes, extrae los años únicos
    presentes en la columna 'Año', y crea gráficos de línea para la cantidad de víctimas por mes
    para cada año. Los gráficos se organizan en una cuadrícula de subgráficos de 2x3.

    Parameters:
        df (pandas.DataFrame): El DataFrame que contiene los datos de accidentes, con una columna 'Año'.

    Returns:
        None
    '''
    # Se obtiene una lista de años únicos
    años = df['Año'].unique()

    # Se define el número de filas y columnas para la cuadrícula de subgráficos
    n_filas = 3
    n_columnas = 2

    # Se crea una figura con subgráficos en una cuadrícula de 2x3
    fig, axes = plt.subplots(n_filas, n_columnas, figsize=(14, 8))

    # Se itera a través de los años y crea un gráfico por año
    for i, year in enumerate(años):
        fila = i // n_columnas
        columna = i % n_columnas
        
        # Se filtran los datos para el año actual y agrupa por mes
        data_mensual = (df[df['Año'] == year]
                        .groupby('Mes')
                        .agg({'Cantidad víctimas':'sum'}))
        
        # Se configura el subgráfico actual
        ax = axes[fila, columna]
        data_mensual.plot(ax=ax, kind='line')
        ax.set_title('Año ' + str(year)) ; ax.set_xlabel('Mes') ; ax.set_ylabel('Cantidad de Víctimas')
        ax.legend_ = None
        
    # Se muestra y acomoda el gráfico
    plt.tight_layout()
    plt.show()

def cantidad_de_victimas_por_mes(df):
    '''
    Crea un gráfico de barras que muestra la cantidad de víctimas de accidentes por mes.

    Esta función toma un DataFrame que contiene datos de accidentes, agrupa los datos por mes
    y calcula la cantidad total de víctimas por mes. Luego, crea un gráfico de barras que muestra
    la cantidad de víctimas para cada mes.

    Parameters:
        df (pandas.DataFrame): El DataFrame que contiene los datos de accidentes con una columna 'Mes'.

    Returns:
        None
    '''
    data= df.groupby('Mes').agg({'Cantidad víctimas':'sum'}).reset_index()
    # Selecciona una paleta de colores aleatoria
    random_palette = sns.color_palette("husl", len(data))
    #Se realiza el gráfico de barras
    plt.figure(figsize=(6,4))
    ax= sns.barplot(data=data, x='Mes', y='Cantidad víctimas', palette= random_palette)
    ax.set_xlabel('Mes')
    ax.set_ylabel('Cantidad de accidentes')

    #Se imprime el resumen
    print(f'El mes con menor cantidad de víctimas tiene {data.min()[1]} víctimas')
    print(f'El mes con mayor cantidad de víctimas tiene {data.max()[1]} víctimas')

    #Se muestra el gráfico
    plt.show()


def cantidad_accidentes_semana_fin_de_semana(df):
    '''
    Genera un gráfico de barras que muestra la cantidad de accidentes por tipo de día (semana o fin de semana).

    Parameters:
        df: El conjunto de datos de accidentes.

    Returns:
        Un gráfico de barras.
    '''
    # Se convierte la columna 'fecha' a tipo de dato datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    
    # Se extrae el día de la semana (0 = lunes, 6 = domingo)
    df['Dia semana'] = df['Fecha'].dt.dayofweek
    
    # Se crea una columna 'tipo_dia' para diferenciar entre semana y fin de semana
    df['Tipo de día'] = df['Dia semana'].apply(lambda x: 'Fin de Semana' if x >= 5 else 'Semana')
    
    # Se cuenta la cantidad de accidentes por tipo de día
    data = df['Tipo de día'].value_counts().reset_index()
    data.columns = ['Tipo de día', 'Cantidad de accidentes']
    
    # Se crea el gráfico de barras
    plt.figure(figsize=(6, 4))
    ax = sns.barplot(x='Tipo de día', y='Cantidad de accidentes', data=data)
    
    ax.set_title('Cantidad de accidentes por tipo de día') ; ax.set_xlabel('Tipo de día') ; ax.set_ylabel('Cantidad de accidentes')
    
    # Se agrega las cantidades en las barras
    for index, row in data.iterrows():
        ax.annotate(f'{row["Cantidad de accidentes"]}', (index, row["Cantidad de accidentes"]), ha='center', va='bottom')
    
    # Se muestra el gráfico
    plt.show()

def crea_categoria_momento_dia(hora):
  """
  Devuelve la categoría de tiempo correspondiente a la hora proporcionada.

  Parameters:
    hora: La hora a clasificar.

  Returns:
    La categoría de tiempo correspondiente.
  """
  if hora.hour >= 6 and hora.hour <= 10:
    return "Mañana"
  elif hora.hour >= 11 and hora.hour <= 13:
    return "Medio día"
  elif hora.hour >= 14 and hora.hour <= 18:
    return "Tarde"
  elif hora.hour >= 19 and hora.hour <= 23:
    return "Noche"
  else:
    return "Madrugada"  

def cantidad_accidentes_por_categoria_tiempo(df):
    '''
    Calcula la cantidad de accidentes por categoría de tiempo y muestra un gráfico de barras.

    Esta función toma un DataFrame que contiene una columna 'Hora' y utiliza la función
    'crea_categoria_momento_dia' para crear la columna 'Categoria tiempo'. Luego, cuenta
    la cantidad de accidentes por cada categoría de tiempo, calcula los porcentajes y
    genera un gráfico de barras que muestra la distribución de accidentes por categoría de tiempo.

    Parameters:
        df (pandas.DataFrame): El DataFrame que contiene la información de los accidentes.

    Returns:
        None
    '''
    # Se aplica la función crea_categoria_momento_dia para crear la columna 'categoria_tiempo'
    df['Categoria tiempo'] = df['Hora'].apply(crea_categoria_momento_dia)

    # Se cuenta la cantidad de accidentes por categoría de tiempo
    data = df['Categoria tiempo'].value_counts().reset_index()
    data.columns = ['Categoria tiempo', 'Cantidad accidentes']
    # Reordenar las categorías en el orden deseado (por ejemplo, 'Mañana', 'Tarde', 'Noche')
  
    # Se calculan los porcentajes
    total_accidentes = data['Cantidad accidentes'].sum()
    data['Porcentaje'] = (data['Cantidad accidentes'] / total_accidentes) * 100
    
    # Se crea el gráfico de barras
    plt.figure(figsize=(6, 4))
    ax = sns.barplot(x='Categoria tiempo', y='Cantidad accidentes', data=data)

    ax.set_title('Cantidad de Accidentes por Categoría de Tiempo') ; ax.set_xlabel('Categoría de Tiempo') ; ax.set_ylabel('Cantidad de Accidentes')

    # Se agrega las cantidades en las barras
    for index, row in data.iterrows():
        ax.annotate(f'{row["Cantidad accidentes"]}', (index, row["Cantidad accidentes"]), ha='center', va='bottom')
        
    # Se muestra el gráfico
    plt.show()

def rango_etario(edad):
    """
    Devuelve el rango etario correspondiente a una edad.

    Args:
        edad: La edad de la víctima.

    Returns:
        El rango etario de la víctima.
    """

    if edad <= 15:
        return 'Infantes'
    elif edad >= 16 and edad <= 25:
        return 'Jóvenes'
    elif edad >= 26 and edad <= 50:
        return 'Adultos'
    elif edad >= 51 and edad <= 70:
        return 'Adultos mayores'
    else:
        return 'Ancianos'
    
def victimas_por_rango_etario(df):
    """
    Crea una nueva columna llamada 'Rango etario' en el dataframe recibido, 
    y luego crea un gráfico de barras para mostrar la cantidad de víctimas registradas por rango etario.

    Args:
        df: El dataframe a procesar.

    Returns:
        El gráfico de barras creado.
    """

    # se crea una nueva columna llamada 'Rango etario'

    df['Rango etario'] = df['Edad'].apply(lambda edad: rango_etario(edad))

    # Se agrupan los registros por rango etario

    grupos = df.groupby('Rango etario')
       
    # Se crea un gráfico de barras

    return grupos['Edad'].size().plot.bar(figsize=(10, 6), color=['yellow','blue','red', 'green','purple'],
                                           xlabel= 'Rango etario', ylabel='Cantidad de registros')
    
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def cantidad_victimas_sexo_rol_victima(df):
    '''
    Genera un resumen de la cantidad de víctimas por sexo, rol y tipo de vehículo en un accidente de tráfico.

    Esta función toma un DataFrame como entrada y genera un resumen que incluye:

    * Gráficos de barras que muestran la cantidad de víctimas por sexo, rol y tipo de vehículo en orden descendente.
    * DataFrames que muestran la cantidad y el porcentaje de víctimas por sexo, rol y tipo de vehículo.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        None
    '''
    # Se convierten las categorías de sexo a minúsculas
    df['Sexo'] = df['Sexo'].str.lower()

    # Se crea el gráfico
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Diccionario de colores para 'masculino' y 'femenino'
    colores_sexo = {'masculino': 'blue', 'femenino': 'pink'}

    # Colores invertidos para los gráficos 2 y 3
    colores_invertidos = ['pink', 'blue']

    # Gráfico 1: Sexo
    sns.countplot(data=df, x='Sexo', ax=axes[0], palette=colores_sexo)
    axes[0].set_title('Cantidad de víctimas por sexo') ; axes[0].set_ylabel('Cantidad de víctimas')

    # Gráfico 2: Rol
    df_rol = df.groupby(['Rol', 'Sexo']).size().unstack(fill_value=0)
    df_rol.plot(kind='bar', stacked=True, ax=axes[1], color=colores_invertidos)
    axes[1].set_title('Cantidad de víctimas por rol') ; axes[1].set_ylabel('Cantidad de víctimas') ; axes[1].tick_params(axis='x', rotation=45)
    axes[1].legend().set_visible(False)
    
    # Gráfico 3: Tipo de vehículo
    df_victima = df.groupby(['Víctima', 'Sexo']).size().unstack(fill_value=0)
    df_victima.plot(kind='bar', stacked=True, ax=axes[2], color=colores_invertidos)
    axes[2].set_title('Cantidad de víctimas por tipo de vehículo') ; axes[2].set_ylabel('Cantidad de víctimas') ; axes[2].tick_params(axis='x', rotation=45)
    axes[2].legend().set_visible(False)

    # Se muestran los gráficos
    plt.show()

def accidentes_tipo_de_calle(df):
    '''
    Genera un resumen de los accidentes de tráfico por tipo de calle y cruce.

    Esta función toma un DataFrame como entrada y genera un resumen que incluye:

    * Un gráfico de barras que muestra la cantidad de víctimas por tipo de calle.
    * Un gráfico de barras que muestra la cantidad de víctimas en cruces.
    
    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        None
    '''
    # Se crea el gráfico
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    
    sns.countplot(data=df, x='Tipo de calle', ax=axes[0])
    axes[0].set_title('Cantidad de víctimas por tipo de calle') ; axes[0].set_ylabel('Cantidad de víctimas')

    sns.countplot(data=df, x='Cruce', ax=axes[1])
    axes[1].set_title('Cantidad de víctimas en cruces') ; axes[1].set_ylabel('Cantidad de víctimas')
    
    # Mostramos los gráficos
    plt.show()


#-------------------------
    
def cantidad_acusados(df):
    '''
    Genera un resumen de la cantidad de acusados en un accidente de tráfico.

    Esta función toma un DataFrame como entrada y genera un resumen que incluye:

    * Un gráfico de barras que muestra la cantidad de acusados en orden descendente.
    * Un DataFrame que muestra la cantidad y el porcentaje de acusados.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        None
    '''
    # Se ordenan los datos por 'Participantes' en orden descendente por cantidad
    ordenado = df['Acusado'].value_counts().reset_index()
    ordenado = ordenado.rename(columns={'Cantidad': 'Acusado'})
    ordenado = ordenado.sort_values(by='count', ascending=False)
    
    plt.figure(figsize=(15, 4))
    
    # Crear el gráfico de barras
    ax = sns.barplot(data=ordenado, x='Acusado', y='count', order=ordenado['Acusado'])
    ax.set_title('Cantidad de acusados en los hechos') ; ax.set_ylabel('Cantidad de acusados') ; ax.set_xlabel('Tipo vehiclo')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

    # Se muestra el gráfico
    plt.show()
    #------------------------------
    # # Se calcula la cantidad de acusados
    acusados_counts = df['Acusado'].value_counts().reset_index()
    acusados_counts.columns = ['Tipo vehiclo', 'Cantidad de acusados']

    # # Se calcula el porcentaje de acusados
    total_acusados = acusados_counts['Cantidad de acusados'].sum()
    acusados_counts['Porcentaje de acusados'] = round((acusados_counts['Cantidad de acusados'] / total_acusados) * 100,2)

    # # Se ordenan los datos por cantidad de acusados en orden descendente
    acusados_counts = acusados_counts.sort_values(by='Cantidad de acusados', ascending=False)
    # # Se imprimen resumen
    print("Resumen de acusados:")
    print(acusados_counts)
