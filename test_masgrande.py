import pytest
from main import MasGrande

#CASOS DE PRUEBA 2 VÁLIDOS Y 8 INVÁLIDOS POR ENTRADAS INCORRECTAS
def test_MasGrande_valido():
    assert MasGrande("Café,12,16,20,24,32") == (True, "Entrada Válida")
def test_MasGrande_valido_con_espacios():
    assert MasGrande("Café con Leche,12,16,20") == (True, "Entrada Válida")
    
def test_MasGrande_rango_invalido():
    assert MasGrande("Café,12,16,20,24,50") == (False, "Tamaño '50' fuera del rango permitido")

def test_MasGrande_invalido_orden():
    assert MasGrande("Té,12,10,8") == (False, "Tamaños deben ser ingresados en orden ascendente")

def test_MasGrande_invalido_tamaño_articulo():
    assert MasGrande("T,12,16,20,24,32") == (False, "Nombre de artículo inválido")
    
def test_MasGrande_muchos_tamaños():
    assert MasGrande("Té,12,16,20,24,32,23,53,1") == (False, "Debe haber entre 1 y 5 tamaños")

def test_MasGrande_invalido_caracteres_especiales():
    assert MasGrande("Café$Latte,12,16,20") == (False, "Nombre de artículo inválido")

def test_MasGrande_invalido_numeros_enteros():
    assert MasGrande("Café,12.5,16,20") == (False, "Tamaño '12.5' no es un número entero")

def test_MasGrande_invalido_numero_duplicados():
    assert MasGrande("Café,10,12,12,20") == (False, "Tamaños deben ser ingresados en orden ascendente")

def test_MasGrande_invalido_coma_faltante():
    assert MasGrande("Café12,16,20") == (False, "Formato de entrada inválido")
