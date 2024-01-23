import pandas as pd
import pandas.api.types as ptypes
from solucion import (
    ej_1_cargar_csv,
    ej_2_convertir_fecha,
    ej_3_convertir_cantidad,
    ej_4_fecha_como_indice,
    ej_5_filtrar_por_fecha,
    ej_6_filtrar_por_producto
)
from unittest import mock


class TestEjercicio1:
    def test_load_dataframe(self):
        df = ej_1_cargar_csv()
        assert isinstance(df, pd.DataFrame)
        
        expected = pd.DataFrame({
            'Fecha': ['2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06'],
            'Producto': ['Producto A', 'Producto B', 'Producto A', 'Producto C', 'Producto B'],
            'Cantidad': [10, 5, 8, 3, 6],
            'Precio': [15.99, 10.99, 12.99, 8.99, 9.99]
        })
        assert (df == expected).all().all()
    
    @mock.patch("solucion.pd.read_csv")
    def test_call_load_csv(self, mock_read_csv):
        ej_1_cargar_csv()
        mock_read_csv.assert_called_once()
        

def test_sol_2():
    df = ej_1_cargar_csv()
    ej_2_convertir_fecha(df)
    assert ptypes.is_datetime64_ns_dtype(df["Fecha"])
    
    
def test_sol_3():
    df = ej_1_cargar_csv()
    ej_3_convertir_cantidad(df)
    assert ptypes.is_int64_dtype(df["Cantidad"])


def test_sol_4():
    df = ej_1_cargar_csv()
    ej_2_convertir_fecha(df)
    ej_4_fecha_como_indice(df)
    
    assert ptypes.is_datetime64_dtype(df.index)
    
    expected = pd.DatetimeIndex(
        [
            "2023-01-02",
            "2023-01-03",
            "2023-01-04",
            "2023-01-05",
            "2023-01-06"
        ],
        dtype='datetime64[ns]',
        name='Fecha',
        freq=None
    )
    assert (df.index == expected).all()
    
    
def test_sol_5():
    df = ej_1_cargar_csv()
    ej_2_convertir_fecha(df)
    ej_3_convertir_cantidad(df)
    ej_4_fecha_como_indice(df)
    
    ej_5_filtrar_por_fecha(df)
    
    actual = pd.read_csv("resultado_1.csv")
    actual['Fecha'] = pd.to_datetime(actual['Fecha'])
    actual.set_index('Fecha', inplace=True)
    
    expected = pd.DataFrame.from_dict({
        'Producto': {
            pd.Timestamp('2023-01-04 00:00:00'): 'Producto A',
            pd.Timestamp('2023-01-05 00:00:00'): 'Producto C',
            pd.Timestamp('2023-01-06 00:00:00'): 'Producto B'
        },
        'Cantidad': {
            pd.Timestamp('2023-01-04 00:00:00'): 8,
            pd.Timestamp('2023-01-05 00:00:00'): 3,
            pd.Timestamp('2023-01-06 00:00:00'): 6
        },
        'Precio': {
            pd.Timestamp('2023-01-04 00:00:00'): 12.99,
            pd.Timestamp('2023-01-05 00:00:00'): 8.99,
            pd.Timestamp('2023-01-06 00:00:00'): 9.99
        }
    })
    
    assert (actual == expected).all().all()


def test_sol_6():
    df = ej_1_cargar_csv()
    ej_2_convertir_fecha(df)
    ej_3_convertir_cantidad(df)
    ej_4_fecha_como_indice(df)
    
    ej_6_filtrar_por_producto(df)
    
    actual = pd.read_csv("resultado_2.csv")
    actual['Fecha'] = pd.to_datetime(actual['Fecha'])
    actual.set_index('Fecha', inplace=True)
    
    expected = pd.DataFrame.from_dict({
        'Producto': {
            pd.Timestamp('2023-01-02 00:00:00'): 'Producto A',
            pd.Timestamp('2023-01-04 00:00:00'): 'Producto A'
        },
        'Cantidad': {
            pd.Timestamp('2023-01-02 00:00:00'): 10,
            pd.Timestamp('2023-01-04 00:00:00'): 8
        },
        'Precio': {
            pd.Timestamp('2023-01-02 00:00:00'): 15.99,
            pd.Timestamp('2023-01-04 00:00:00'): 12.99
        }
    })
    
    assert (actual == expected).all().all()
