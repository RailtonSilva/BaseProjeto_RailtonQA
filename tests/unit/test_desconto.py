import pytest
from src.desconto import calcular_desconto, calcular_frete


def test_aplica_10_por_cento_acima_de_100():
    # Arrange
    valor = 200.0

    # Act
    resultado = calcular_desconto(valor)

    # Assert
    assert resultado == 180.0


@pytest.mark.parametrize(
    "valor, esperado",
    [
        (0, 0.0),         
        (99.99, 99.99),    
        (100.0, 90.0),     
        (200.0, 180.0),    
    ],
)

def test_desconto_valores_limite(valor, esperado):
    assert calcular_desconto(valor) == esperado

def test_desconto_valor_negativo_gera_erro():
    with pytest.raises(ValueError, match="negativo"):
        calcular_desconto(-1)


#calcular frete------------------------

@pytest.mark.parametrize("valor_pedido", [200.0, 350.0])

def test_frete_gratis_a_partir_de_200(valor_pedido):
    assert calcular_frete(valor_pedido, 10) == 0.0

@pytest.mark.parametrize(
    "valor_pedido, distancia, esperado",
    [
        (199.99, 0, 10.0),    
        (150.0, 10, 25.0),    
        (50.0, 3.5, 15.25),   
    ],
)
def test_frete_cobrado_por_distancia_abaixo_de_200(valor_pedido, distancia, esperado):
    assert calcular_frete(valor_pedido, distancia) == esperado


def test_frete_valor_pedido_negativo_gera_erro():
    with pytest.raises(ValueError):
        calcular_frete(-10, 5)


def test_frete_distancia_negativa_gera_erro():
    with pytest.raises(ValueError):
        calcular_frete(250, -1)

# TODO (Prática 1):
# 1. Use @pytest.mark.parametrize para testar valores de borda: 0, 99.99, 100.0, 200.0
# 2. Use pytest.raises(ValueError) para validar valores negativos em calcular_desconto
# 3. Crie testes unitários para calcular_frete (valor >= 200 grátis, < 200 com distância e erros negativos)
