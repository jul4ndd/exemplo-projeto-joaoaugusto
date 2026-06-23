from http import HTTPStatus

from fastapi import FastAPI

from viajei_api.schemas import Message


app = FastAPI()


@app.get("/", 
        status_code=HTTPStatus.ACCEPTED, 
        response_model=Message)
def bem_vindo():
    return {"message": "Bem vindo!"}


@app.get("/hello")
def ola_mundo():
    return {"message": "Olá! Turma!"}
