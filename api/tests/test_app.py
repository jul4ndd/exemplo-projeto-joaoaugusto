from http import HTTPStatus

from fastapi.testclient import TestClient

from viajei_api.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    # Arrange / Given 
    client = TestClient(app)
    
    # Act / When
    response = client.get("/")

    # Assert / Then
    assert response.status_code == HTTPStatus.ACCEPTED
    assert response.json() == {"message": "Bem vindo!"}
