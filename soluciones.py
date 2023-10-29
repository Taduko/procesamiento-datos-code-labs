from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.tree import DecisionTreeClassifier


def ej_1_carga_dataset() -> Tuple[np.ndarray, np.ndarray]:
    """Cargar los dígitos y retornar las matrices de imágenes y etiquetas

    Returns:
        Tuple[np.ndarray, np.ndarray]: Tuple[np.array[shape=(n_imgs, 8, 8)], np.array[shape=(n_imgs,)]]
    """
    pass


def ej_2_exploracion_dataset(X: np.ndarray, Y: np.ndarray, rng: np.random.Generator):
    """Graficar 10 imágenes
    Esta función debe utilizar el generador de números aleatorios `rng` para selccionar
    10 números al azar en el rango (0, len(X)), para esto usa la función `rng.choice`,
    la cual retorna un array de índices que puedes usar para selccionar la imágenes y
    etiquetas a graficar
    
    Grafica cada imágen con `plt.imshow` y configura el título de cada gráfica de 
    la forma `Digito: <etiqueta>`

    Args:
        X (np.ndarray): Imágenes
        Y (np.ndarray): Etiquetas
        rng (np.random.Generator): Generador de números aleatorios
    """
    pass
        

def ej_3_entrenar_arbol(X: np.ndarray, y: np.ndarray) -> DecisionTreeClassifier:
    """Entrenar un árbol de decisiones y retornarlo como resultado de la función
    No olvides convertir la matriz X a las dimensiones correctas

    Args:
        X (np.ndarray): Matriz de dimensiones (n_imagenes, 8, 8)
        y (np.ndarray): Matriz de dimensiones (n_imagenes,)

    Returns:
        DecisionTreeClassifier: Modelo ajustado
    """
    pass


def ej_4_evaluacion_rendimiento(
    modelo: DecisionTreeClassifier, X_test: np.ndarray, y_test: np.ndarray
) -> float:
    """Calcula el accuracy del modelo y retornalo como resultado de la función

    Args:
        modelo (DecisionTreeClassifier): Modelo ya entrenado
        X_test (np.ndarray): Matriz con datos de test de dimensión (n_imagenes, 64)
        y_test (np.ndarray): Matriz con etiquetas de test de dimensión (n_imagenes,)

    Returns:
        float: accuracy calculada
    """
    pass
