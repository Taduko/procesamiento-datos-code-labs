import pytest

import pandas as pd
from solucion import (
    ej_1_cargar_csv,
    ej_2_puntuacion_promedio,
    ej_3_nombre_estudiantes,
    ej_4_edad_y_cantidad,
    ej_5_edad_promedio,
)
from unittest import mock


class TestEjercicio1:
    def test_load_dataframe(self):
        df = ej_1_cargar_csv()
        assert isinstance(df, pd.DataFrame)

        expected = pd.DataFrame.from_dict({
            "Nombre": [
                "Estudiante1",
                "Estudiante2",
                "Estudiante3",
                "Estudiante4",
                "Estudiante5",
                "Estudiante6",
                "Estudiante7",
                "Estudiante8",
                "Estudiante9",
                "Estudiante10"
            ],
            "Edad": [20, 21, 19, 22, 20, 21, 19, 22, 20, 21],
            "Puntuacion": [85.5, 75.0, 92.5, 80.2, 88.9, 76.8, 94.2, 82.1, 87.3, 77.6]
        })
        
        assert (df == expected).all().all()
    
    @mock.patch("solucion.pd.read_csv")
    def test_call_load_csv(self, mock_read_csv):
        ej_1_cargar_csv()
        mock_read_csv.assert_called_once()
        

def test_sol_2():
    df = ej_1_cargar_csv()
    promedio = ej_2_puntuacion_promedio(df)
    
    assert 78.34 == pytest.approx(promedio)
    
    
def test_sol_3():
    df = ej_1_cargar_csv()
    estudiantes = list(ej_3_nombre_estudiantes(df))
    
    expected = [
        "Estudiante1",
        "Estudiante3",
        "Estudiante5",
        "Estudiante7",
        "Estudiante9",
    ]
    assert estudiantes == expected


def test_sol_4():
    df = ej_1_cargar_csv()
    
    filtered = ej_4_edad_y_cantidad(df)
    
    expected = pd.DataFrame.from_dict({
        "Edad": {0: 22, 1: 21, 2: 20, 3: 19},
        "Cantidad": {0: 2, 1: 3, 2: 3, 3: 2}
    })
    assert (filtered == expected).all().all()
    
    
def test_sol_5():
    df = ej_1_cargar_csv()
    
    promedio = ej_5_edad_promedio(df)
    
    assert 20.285714285714285 == pytest.approx(promedio)
