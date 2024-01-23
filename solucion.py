import pandas as pd


def ej_1_cargar_csv() -> pd.DataFrame:
    df = pd.read_csv('datos.csv')  # Cargamos el csv
    return df

def ej_2_convertir_fecha(df: pd.DataFrame) -> None:
    df['Fecha'] = pd.to_datetime(df['Fecha']) # Cambiamos el tipo de dato de la columna Fecha a datetime

def ej_3_convertir_cantidad(df: pd.DataFrame) -> None:
    df['Cantidad'] = df['Cantidad'].astype('int64')  # Cambiamos el tipo de dato de la columna Cantidad a int64

def ej_4_fecha_como_indice(df: pd.DataFrame) -> None:
    df.set_index('Fecha', inplace=True) # inplace=True para que se guarde en el mismo dataframe

def ej_5_filtrar_por_fecha(df: pd.DataFrame) -> pd.DataFrame:
    filtered_df = df[df.index >= '2023-01-04']
    filtered_df.to_csv('resultado_1.csv') # Guardamos el resultado en un csv
    return filtered_df

def ej_6_filtrar_por_producto(df: pd.DataFrame) -> pd.DataFrame:
    filtered_df = df[df['Producto'] == 'Producto A'] # Filtramos por producto
    filtered_df.to_csv('resultado_2.csv')
    return filtered_df