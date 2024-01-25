import pandas as pd


def ej_1_cargar_csv() -> pd.DataFrame:
   df = pd.read_csv('datos.csv')
   return df


def ej_2_puntuacion_promedio(df: pd.DataFrame) -> float: 
    puntuacion_promedio = df[df['Edad'] > 20]['Puntuacion'].mean()
    return puntuacion_promedio

def ej_3_nombre_estudiantes(df: pd.DataFrame) -> list[str]:
    # Filtrar los estudiantes con puntuación mayor a 85 y edad menor a 22
    estudiantes_filtrados = df[(df['Puntuacion'] > 85) & (df['Edad'] < 22)]
    # Obtener el nombre de los estudiantes filtrados
    nombre_estudiantes = estudiantes_filtrados['Nombre'].tolist()

    return nombre_estudiantes 

 


def ej_4_edad_y_cantidad(df: pd.DataFrame) -> pd.DataFrame:
    edad_y_cantidad = df.groupby('Edad')['Nombre'].count().reset_index(name='Cantidad')
    edad_y_cantidad = edad_y_cantidad.sort_values(by='Edad', ascending=False).reset_index(drop=True)
    return edad_y_cantidad


def ej_5_edad_promedio(df: pd.DataFrame) -> float:
    edad_promedio_puntuacion_mayor_80 = df[df['Puntuacion'] > 80]['Edad'].mean()
    return edad_promedio_puntuacion_mayor_80