from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier


def ej_1_prepraracion_dataset() -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    from sklearn.model_selection import train_test_split
    """Cargar los dígitos y particionar los datos.
    Nota: Recuerda hacer la transfomación para aplanar las imágenes a vectores de 64 elementos

    Returns:
        Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]: X_train, y_train, X_test, y_test
    """
    pass


def ej_2_entrenar_random_forest(
    X_train: np.ndarray,
    y_train: np.ndarray,
) -> RandomForestClassifier:
    """Entrenar un random forest y retornarlo como resultado de la función
    No olvides convertir la matriz X a las dimensiones correctas

    Args:
        X_train (np.ndarray): Matriz de dimensiones (n_imagenes_train, 64)
        y_train (np.ndarray): Matriz de dimensiones (n_imagenes_train,)

    Returns:
       RandomForestClassifier : Modelo ajustado
    """
    pass


def ej_3_evaluacion_rendimiento(
    modelo: RandomForestClassifier, X_test: np.ndarray, y_test: np.ndarray
) -> Tuple[float, np.ndarray]:
    """Calcula el accuracy del modelo y la matriz de confusión
    retornalos como resultado de la función

    Args:
        modelo (DecisionTreeClassifier): Modelo ya entrenado
        X_test (np.ndarray): Matriz con datos de test de dimensión (n_imagenes, 64)
        y_test (np.ndarray): Matriz con etiquetas de test de dimensión (n_imagenes,)

    Returns:
        float: accuracy calculada
        np.ndarray: matriz de confusión
    """
    pass


def ej_4_metricas_balanceadas(
    y_test: np.ndarray,
    y_pred: np.ndarray
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Calcula las métricas precision, recall y f1-score para cada clase

    Args:
        y_test (np.ndarray)
        y_pred (np.ndarray)

    Returns:
        precision: np.ndarray (n_classes,)
        recall: np.ndarray (n_classes,)
        f1: np.ndarray (n_classes,)
    """
    pass
