import oauth2
import json
import urllib.parse

consumer_key =''
consumer_secret =''

token_key =''
token_secret =''

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

query = input("Novo tweet: ")
query_codificada = urllib.parse.quote(query, safe='')
requisicao = cliente.request('' + query_codificada, method='POST')

decodificar = requisicao[1].decode()

objeto = json.loads(decodificar)
print(objeto)