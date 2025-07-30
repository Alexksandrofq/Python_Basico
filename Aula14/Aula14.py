import re

padrao = r'\w+@\w+\.\w+'
strings = [string_de_teste, string_de_teste2, string_de_teste3]

for s in strings:
    encontrados = re.findall(padrao, s)
    if encontrados:
        print(encontrados)
    else:
        print("Padrão não encontrado")