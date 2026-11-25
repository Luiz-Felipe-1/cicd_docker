import pytest
from app.main import app, calcular_total


def test_desconto_10_por_cento():
    assert calcular_total(1000, 10) == 900


def test_sem_desconto():
    assert calcular_total(500, 0) == 500


def test_desconto_invalido():
    with pytest.raises(ValueError):
        calcular_total(100, 150)


def test_health():
    resposta = app.test_client().get("/health")
    assert resposta.status_code == 200
    assert resposta.get_json() == {"status": "ok"}
