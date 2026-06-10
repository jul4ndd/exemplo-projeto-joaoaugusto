from dispositivo import Dispositivo

class Celular(Dispositivo):
    
    bateria:int

    def __init__(self, nome:str, bateria:int):
        super().__init__(nome)
        self.bateria = bateria