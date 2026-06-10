from example.character import Character

class Mage(Character):

    def __init__(self, nome:str):
        super().__init__(nome, vida = 90)

    def atacar(self, inimigo: Character):
        if super().vida <= 40:
            inimigo.vida -= 40
        else:
            inimigo.vida -= 25
        
