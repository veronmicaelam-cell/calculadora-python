from calculadora import sumar, restar, multiplicar, dividir
import pytest

#Ejecutá pytest -v para correr el test
#Regla clave de Pytest: Todas las funciones de prueba deben comenzar obligatoriamente con la palabra 
# test_ para que Pytest las reconozca automáticamente.

#Pruebas para la función sumar
def test_sumar_positivo():
    assert sumar(2, 3) == 5
    assert sumar(2, 2) == 4

#Pruebas para función sumar negativos
def test_sumar_negativo():
    assert sumar(-2, -3) == -5
    assert sumar(-2, -2) == -4

#Pruebas para función restar
def test_restar():
    assert restar(4, 2) == 2
    assert restar(6, 3) == 3

#Pruebas para función multiplicar
def test_multiplicar():
    assert multiplicar(4, 3) == 12
    assert multiplicar(7, 2) == 14

#Pruebas para función dividir
def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(15, 3) == 5

#Prueba para verificar que la / por 0 lance la excepción
#Manejo de errores
#Pytest tiene esta forma especial de validar excepciones con pytest.raises(...).
def test_dividir_por_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(1, 0)

