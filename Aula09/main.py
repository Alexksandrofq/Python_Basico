from veiculo import Veiculo #de arquivo veiculo importa da classe Veiculo
from carro import Carro

caminhoa_rosa = Veiculo('rosa', 6, 'ford', 10 )

print("Caminhão Rosa")
print("Cor: ", caminhoa_rosa.cor)
print("Rodas: ",  caminhoa_rosa.rodas)
print("Marca: ", caminhoa_rosa.marca)
print("Tanque: ", caminhoa_rosa.tanque)

print("")

carro_azul = Carro('azul', 'BMW', 30)

print("Carro Azul")
print("Cor: ", carro_azul.cor)
print("Rodas: ",  carro_azul.rodas)
print("Marca: ", carro_azul.marca)
print("Tanque: ", carro_azul.tanque)
carro_azul.abastecer(10)
print("Tanque: ", carro_azul.tanque)
carro_azul.abastecer(70)
print("Tanque: ", carro_azul.tanque)