import requests
import json

cidade = input ("Escreva sua cidade: ")

requisicao = requests.get('htttp://api.openweathermap.org/data/2.5/ weather?q='+cidade+'&appd')

tempo = json.loads(requisicao.text)

print('Condição do tempo', tempo['weather'] [0] ['main'])