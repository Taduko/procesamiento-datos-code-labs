import pytest
import numpy as np

from solucion import (
    ej_1_get_array,
    ej_2_media_std,
    ej_3_temperaturas,
    ej_4_min_max,
    ej_5_diferencias,
    ej_6_cuadrado,
    ej_7_suma,
    ej_8_raiz,
)


def test_solucion_1():
    np.testing.assert_array_equal(
        ej_1_get_array(),
        [25, 30, 27, 22, 29, 31, 26, 28],
    )
    
    
def test_solucion_2():
    array = ej_1_get_array()
    
    media, std = ej_2_media_std(array)
    
    assert (27.25, 2.7271780286589284) == pytest.approx((media, std))
    
    
def test_solucion_3():
    array = ej_1_get_array()
    
    np.testing.assert_allclose(
        ej_3_temperaturas(array),
        [77., 86., 80.6, 71.6, 84.2, 87.8, 78.8, 82.4],
    )


def test_solucion_4():
    array = ej_1_get_array()
    temperaturas = ej_3_temperaturas(array)
    
    temp_min, temp_max = ej_4_min_max(temperaturas)
    
    assert (71.6, 87.8) == pytest.approx((temp_min, temp_max))
    

def test_solucion_5():
    array = ej_1_get_array()
    media, _ = ej_2_media_std(array)
    temperaturas = ej_3_temperaturas(array)
    
    np.testing.assert_allclose(
        ej_5_diferencias(temperaturas, media),
        [49.75, 58.75, 53.35, 44.35, 56.95, 60.55, 51.55, 55.15],
    )
    

def test_solucion_6():
    array = ej_1_get_array()
    media, _ = ej_2_media_std(array)
    temperaturas = ej_3_temperaturas(array)
    diferencias = ej_5_diferencias(temperaturas, media)
    
    np.testing.assert_allclose(
        ej_6_cuadrado(diferencias),
        [
            2475.0625,
            3451.5625,
            2846.2225,
            1966.9225,
            3243.3025,
            3666.3025,
            2657.4025,
            3041.5225,
        ],
    )
    
    
def test_solucion_7():
    array = ej_1_get_array()
    media, _ = ej_2_media_std(array)
    temperaturas = ej_3_temperaturas(array)
    diferencias = ej_5_diferencias(temperaturas, media)
    cuadrados = ej_6_cuadrado(diferencias)
    
    assert 23348.299999999996 == pytest.approx(ej_7_suma(cuadrados))
    
    
def test_solucion_8():
    array = ej_1_get_array()
    media, _ = ej_2_media_std(array)
    temperaturas = ej_3_temperaturas(array)
    diferencias = ej_5_diferencias(temperaturas, media)
    cuadrados = ej_6_cuadrado(diferencias)
    suma = ej_7_suma(cuadrados)
    
    assert 152.8015052281881 == pytest.approx(ej_8_raiz(suma))
