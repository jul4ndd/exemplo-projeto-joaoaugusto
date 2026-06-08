class Gato:

    pelagem:str
    porte:str
    nome:str 
    idade:int


    def __init__(self, pelagem:str, porte:str, nome:str, idade:int):
        self.pelagem = pelagem
        self.porte = porte
        self.nome = nome
        self.idade = idade

    def miar(self):
        print("Miau!")