arquivo = open('arquivo.txt', 'r')

for i in range(1, 101):
    arquivo.write("eu amo voce " + str(i) + "\n") #para escrever
print(arquivo.read()) #para mostrar o conteudo