from example.character import Character

class Warrior(Character):

    def __init__(self, nome:str):
        super().__init__(nome, vida = 150)

    def atacar(self, inimigo: Character):
        inimigo.vida -= 20
        
