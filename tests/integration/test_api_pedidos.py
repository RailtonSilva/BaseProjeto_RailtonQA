from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_health_check_retorna_200():
    resp = client.get("/health")

    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_criar_pedido_com_desconto_e_frete():

    payload = {"item": "Camisa", "valor": 150.0, "distancia_km": 10}

    resp = client.post("/pedidos", json=payload)

   
    assert resp.status_code == 201 corpo = resp.json()
    assert corpo["item"] == "Camisa"
    assert corpo["valor_original"] == 150.0
    assert corpo["total_com_desconto"] == 135.0   
    assert corpo["frete"] == 25.0                 
    assert corpo["total_final"] == 160.0          


def test_criar_pedido_valor_negativo_retorna_400():
    payload = {"item": "Camisa", "valor": -50.0, "distancia_km": 5}

    resp = client.post("/pedidos", json=payload)

    assert resp.status_code == 400
    assert resp.json()["detail"] == "Valor não pode ser negativo"


def test_criar_pedido_item_vazio_retorna_400():
    payload = {"item": "   ", "valor": 100.0, "distancia_km": 5}

    resp = client.post("/pedidos", json=payload)

    assert resp.status_code == 400
    assert resp.json()["detail"] == "Nome do item é obrigatório"


def test_listar_pedidos_contem_pedido_criado():
  
    criado = client.post( "/pedidos", json={"item": "Tênis", "valor": 300.0, "distancia_km": 20} ).json()

    resp = client.get("/pedidos")


    assert resp.status_code == 200
    assert criado in resp.json()

# TODO (Prática 2):
# 1. Testar POST /pedidos com valor >= 100 e distância > 0 (status 201 e total_final calculado)
# 2. Testar POST /pedidos com valor negativo (status 400 e mensagem de erro)
# 3. Testar POST /pedidos com item vazio (status 400)
# 4. Testar GET /pedidos verificando se o pedido criado aparece na lista
