def ej_1_statmodels_intervalo_confianza() -> tuple[float, tuple[float, float]]:
    """Esta función realiza lo siguiente
    * Carga el archivo que contiene el dataset (datos.csv)
    * Ajusta un modelo de regresión lineal con statsmodels (x1, x2, x4 como predictores)
    * Realiza una predicción de x3 con el nuevo punto (x1=100, x2=12, x4=9.2)
    * Para esta predicción se obtiene el valor predicho y el intérvalo de confianza
    NOTA: ten mucho cuidado con los tipos de datos que retorna statsmodels (son arrays)

    Returns:
        tuple[float, tuple[float, float]]: La tupla contiene como primer valor
        la predicción media, y como segundo valor una tupla que representa el
        intérvalo de confianza.
    """
    pass


def ej_2_sklearn_coeficientes() -> tuple[float, float, float]:
    """Esta función realiza lo siguiente
    * Carga el dataset
    * Ajusta un modelo de regresión lineal usando x1, x2, x4 como atributos
    * Retorna los coeficientes como una tupla

    Returns:
        tuple[float, float, float]: Coeficientes de la regresión como una tupla
        de longitud=3.
    """
    # Definir las variables X y y
    pass
