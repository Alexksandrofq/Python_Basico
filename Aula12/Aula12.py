import requests
requisicao = None

try:
    requisicao = requests.get('http://gi.com.br')
    print(requisicao.text)
except Exception as e:
    print("Requisição deu erro:", e)

# ou

import requests

requisicao = None

requisicao = requests.get('http://g1.com.br')
print(requisicao.text)