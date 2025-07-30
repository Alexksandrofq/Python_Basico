class Cliente:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        

    def __str__(self):
        return "Nome: " + self.nome + "\nIdade: " + str(self.idade) + "\nCPF: " + self.cpf 
 