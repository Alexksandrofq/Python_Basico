from veiculo import Veiculo

class Carro(Veiculo):#herança esta em ()

    def __init__(self, cor, marca, tanque):
        Veiculo.__init__(self, cor, 4, marca, tanque)
    
    def abastecer(self, litros):
        if self.tanque + litros > 50:
            print("Erro: tanque cheio")
        else:   
            self.tanque += litros